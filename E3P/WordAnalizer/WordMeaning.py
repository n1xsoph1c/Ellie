"""
Word Meanings for Ellie Language
-------------------------------------------
Hi, Hello, Sup = greeting_word
How = event
are = something_object
you = self 
"""

import os
import json
import sys

THIS_DIR = os.path.dirname(__file__)
LIB_DIR = os.path.join(THIS_DIR, "Meanings")

wordListFiles = os.path.join(LIB_DIR, "words.json")

try:
    with open(wordListFiles) as file:
        WORDLIST = json.loads(file.read())
except Exception as e:
    print(e)


# ----------------------------- Dictionary ---------------------------------
ASK = WORDLIST["ask"]
IDENTITY = WORDLIST["identity"]
INFO = WORDLIST['info']
PERSON = WORDLIST['person']

# ------------------------------------ List ------------------------------------
Age = IDENTITY["age"]
Greetings = WORDLIST["greetings"]
Ellie = IDENTITY["self"]
Owner = IDENTITY["owner"]
Social_media = INFO["social_media"]
User = PERSON["user"]


Sentence = list()
temp_sentence = list()


def word_in_list(List: list, text: str):
    if List.__contains__(text):
        return True
    else:
        return False


def get_key(Dict: dict, text: list):
    for key, value in Dict.items():
        if text.__contains__(value):
            return key, value
    else:
        return None, None


def word_in(object):
    if object == "" or object == None:
        return False
    else:
        return True


def get_word_meaning(sentence: list):
    Sentence = sentence
    temp_sentence = sentence.copy()  # copy of original sentence
    event_list = list()

    isAsking = False
    isID = False
    isInfo = False
    isPerson = False

    # Check if word in any of the dictionaris and get the key
    ask, question = get_key(ASK, sentence)
    identity, ID = get_key(IDENTITY, sentence)
    info, intel = get_key(INFO, sentence)
    person, person_type = get_key(PERSON, sentence)

    if word_in(ask):
        event_list.append(ask)
        temp_sentence.__delitem__(temp_sentence.index(question))

    if word_in(identity):
        event_list.append(identity)
        temp_sentence.__delitem__(temp_sentence.index(ID))

    if word_in(info):
        event_list.append(info)
        temp_sentence.__delitem__(temp_sentence.index(intel))

    if word_in(person):
        event_list.append(person)
        temp_sentence.__delitem__(temp_sentence.index(person_type))

    # Check for word in Lists
    for word in Sentence:
        if word_in_list(Age, word):
            event_list.append("age")
            temp_sentence.__delitem__(temp_sentence.index(word))

        if word_in_list(Greetings, word):
            event_list.append("greet")
            temp_sentence.__delitem__(temp_sentence.index(word))

        if word_in_list(Ellie, word):
            event_list.append("self")
            temp_sentence.__delitem__(temp_sentence.index(word))

        if word_in_list(Social_media, word):
            event_list.append("social_media")
            temp_sentence.__delitem__(temp_sentence.index(word))

        if word_in_list(Owner, word):
            event_list.append("owner")
            temp_sentence.__delitem__(temp_sentence.index(word))

    return event_list
