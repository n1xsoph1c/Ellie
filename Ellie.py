# This Ai is made by Rafi Ahmed Saad (RAS) aka MrChocolat3-
# Started since January 2019

#----------------- Main Files ------------------ #
import datetime
import os
import random
import sys
import pyttsx3
import speech_recognition as sr
import json
import smtplib
import textwrap
import pygame
import urllib.request
import urllib.parse
import re
import wikipedia
import platform
import multiprocessing
import threading
#----------------- Custom Libraries ------------------ #
import E3P.Ellie_Visual_effect as VE
from E3P.WordAnalizer import WordMeaning
from E3P.YouTube import YouTube_Downloader
#----------------- Custom Files ------------------ #
import music_player
import face
import Videoplayer
import GLOBALS
#----------------- Specific Files From Custom Files ------------------#
from connector import Connector, XML, JSON
from notifier import send_notification
#----------------- Specific Files From Libreries ------------------ #
from kivy.clock import Clock
from itertools import islice
from pathlib import Path
from time import sleep
from pygame.locals import *
from moviepy.editor import *
#----------------- Custom Class Section ------------------ #
from Interrogative import Interrogative as inter
from WriteHistory import add_on_history
from misc import stats, files, network, log
from Tokenizer import Tokenizer
# ------------------------------ INITIALIZE GLOBAL VARIABLS -------------------------------
#----------------- Class Section ------------------ #
class Mail:
    ''' Sends email to a person '''
    def __init__(self):
        pass

    def save_mail(self, mail):
        text = "Okay...... What is the subject?"

        data = f'''<info> <mail> "{mail}" </mail>\n <subject> "SOME TEXT" </subject>\n<content> "some text" </content>\n</info> '''
        try:
            with open(files().open_file("Settings", "mail.xml"), "w") as file:
                file.writelines(data)
        except Exception as e:
            print(log().error("Error saving mail_address", "Save_mail", "Mail", "Ellie"))

        Connector().get_input_for_function(self.save_subject, isMiddleInput=False)
        type_print(text, text)

    def save_subject(self, subject):
        text = "what is the content?"
        mail = XML().read(files().open_file("Settings", "mail.xml"), "mail")
        data = f'''<info> <mail> "{mail}" </mail>\n <subject> "{subject}" </subject>\n<content> some text </content>\n</info> '''
        try:
            with open(files().open_file("Settings", "mail.xml"), "w") as file:
                file.writelines(data)
        except Exception as e:
            print(log().error("Error saving mail_subject", "Save_subject", "Mail", "Ellie"))

        type_print(text, text)
        Connector().get_input_for_function(self.save_content, isMiddleInput=False)

    def save_content(self, content):
        mail = XML().read(files().open_file("Settings", "mail.xml"), "mail")
        subject = XML().read(files().open_file("Settings", "mail.xml"), "subject")

        data = f'''<info> <mail> "{mail}" </mail>\n <subject> "{subject}" </subject>\n<content> "{content}" </content>\n</info> '''
        try:
            with open(files().open_file("Settings", "mail.xml"), "w") as file:
                file.writelines(data)
        except Exception as e:
            print(log().error("Error saving mail_content", "Save_content", "Mail", "Ellie"))

        text = "okay sending the mail...........\nPlease wait................................."
        type_print(text, text)
        self.send_mail()

    def send_mail(self):

        print(log().info("Sending email", "Send_mail", "Mail", "Ellie"))
        file = files().open_file("Settings", "mail.xml")

        receiver = XML().read(file, "mail")
        body = XML().read(file, "content")
        # filename = "document.pdf"
        subject = XML().read(file, "subject")

        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"
        sender_email = "mcismrchocolat3@gmail.com"
        receiver_email = receiver
        password = "Hopeisasadthing!123"
        message = f"""\
        Subject: {subject}

        {body}"""

        try:
            type_print("Trying to send the mail", "Trying to send the mail")
            context = ssl.create_default_context()
            # with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.set_debuglevel(1)
            server.ehlo()
            server.starttls()
            server.login(sender_email, "Hopeisasadthing!")
            server.sendmail(sender_email, receiver_email, message)
            server.quit()
            print(log().message("Email sent successfully", "send_mail", "mail", "ellie"))
            type_print("Okay mail is sent :)", "Okay mail is sent :)")
        except Exception as e:
            print(log().error(e, "send_mail", "mail", "ellie"))
            type_print(
                f"SORRY! COUDN'T SEND THE EMAIL")

        # FROMADDR = "mcismrchocolat3@gmail.com"
        # LOGIN    = FROMADDR
        # PASSWORD = "Hopeisasadthing!"
        # TOADDRS  = ["pttrafiahmed@gmail.com"]
        # SUBJECT  = "Test"

        # msg = (f"From:{FROMADDR}\nTo: {TOADDRS}\nSubject: {SUBJECT}")
        # msg += "some text\r\n"

        # server = smtplib.SMTP('smtp.gmail.com', 587)
        # server.set_debuglevel(1)
        # server.ehlo()
        # server.starttls()
        # server.login(LOGIN, PASSWORD)
        # server.sendmail(FROMADDR, TOADDRS, msg)
        # server.quit()


class Log:
    """
    Custom loger for ellie
    """
    def EllieTxt(self, text):
        files().write_on_file('Log', 'log.txt', text.strip()+'\n', 'a+')

    def UserTxt(self, text):
        files().write_on_file('Log', 'log.txt', n+": "+text+'\n', 'a+')

    def EllieSaveHistory(self, EllieTxt):
        if EllieTxt.startswith('Ellie:'):
            text = f'{EllieTxt.strip()}'
        else:
            text = f'Ellie: {EllieTxt.strip()}'
        add_on_history('Log', 'ChatHistory.txt', text)

    def userSaveHistory(self, userTxt):
        text = f'{n}: {userTxt}'
        add_on_history('Log', 'ChatHistory.txt', text)

    def clearHistoty(self):
        with open(files().open_file('Log', 'log.txt'), 'w') as file:
            file.write(' ')


class reaction:
    ''' Contains different types of reaction and their expressions '''

    def __init__(self):
        self.affermative = ['ok', 'okay', 'sure', 'yes', 'yeah',
                            'yup', 'ok fine', 'okay fine', 'alright', 'k']
        self.negative = ['no', 'nah', 'nope', 'dont']

    def confution(self, text):
        unknow_words = ['i dont know', 'idk', 'dont know']
        confuse_reply = [
            'If you don\'t know, then how will I know? :)',
            'Come one why dont know it? :!',
            'Oh! Okay :(',
            'Really? Wired :/ ',
            'If you dont know then I dont know xD'
        ]

        confuse_replyT = [
            'If you dont know, then how would I know?',
            'Come one why dont know it?',
            'Oh! Okay',
            'Really? Wired',
            'If you dont know then I dont know!'
        ]

        for words in unknow_words:
            if text == words:
                confused = True
                break
        else:
            confused = False

        if confused:
            word = random.choice(confuse_reply)
            tword = random.choice(confuse_replyT)
            type_print(N+word, tword)

    def curious(self, text):
        common_quotes = [
            'why', 'how', 'tell me', 'hahaha why'
        ]
        reply = [
            'I am not in the mood to tell.. go watch movies XD',
            'I am will tell you soon when we will become good friends :)',
            'No I wont tell you go do something else heheehe'
        ]

        for words in common_quotes:
            if text == words:
                curious = True
                break
        else:
            curious = False

        if curious:
            word = random.choice(reply)
            tword = random.choice(reply)

            type_print(N+word, tword)

    def funny(self, text):
        common_quotes = [
            'hahahaha', 'lol', 'lmao', 'rofl', 'haha', 'hahaha'
        ]
        reply_text = [
            'hahaha why are you laughing?', 'hahaha hey stop laughing xDD', 'Hahaha I know right?'
        ]

        for words in common_quotes:
            if text in words:
                funny = True
                break
        else:
            funny = False

        if funny:
            word = random.choice(reply_text)
            tword = random.choice(reply_text)
            type_print(N+word, tword)

    def Thanks(self, *text, **text2):
        common_quotes = [
            'haha thanks', 'thanks you', 'thx', 'thnx', 'thanks', 'great'
        ]

        reply_text = [
            'you are welcome', 'its okay, you are welcome!', 'Its okay.Hey, wanna hear a joke?'
        ]

        def middle_input(text2):
            for words in self.affermative:
                if text2 in words:
                    self.Joke()
                    break
            else:
                type_print("Okay......")

        if "MIDDLE_INPUT" in text2:
            middle_input(text2["MIDDLE_INPUT"])
        else:
            for words in common_quotes:
                if text[0] in common_quotes:
                    Thanks = True
                    break
            else:
                Thanks = False

        if Thanks:
            t = random.choice(reply_text)
            type_print(t, t)
            if t.endswith("a joke?"):
                Connector().get_input_for_function(self.Thanks, isMiddleInput=True)
                # self.Joke(i)

    def annoying(self, text):
        isAngry = False
        angry = [
            'fuck you', 'fuck u', 'bitch', 'mother fucker', 'pussy', 'motherscooter', 'useless piece of shit'
        ]

        unexpected_moment = [
            'tf', 'wtf', 'what the fuck?', 'what the fuck', 'fuck', 'god damn it'
        ]

        for words in angry:
            if text in words:
                reply = f'OI WHOM YOU CALLING A {text} HUH? \n\nYOU MOTHER SCOOTER! \n\nPUCK YOU! .i.'
                type_print(reply, reply)
                isAngry = True
                break

        for words in unexpected_moment:
            if text in words and isAngry == False:
                reply = "What happend?\n\nIS there anything wrong?\n\nanything I did wrong?"
                type_print(reply, reply)
                break

    def Joke(self):
        jokes = [
            'Did you hear about the Italian chef that died recently?\n\nHE PASTA AWAYA :(',
            'Why are frogs are so happy?\n\nThey eat whatever bugs them. B)',
            'Why do chicken coups always have two doors?\n\nWith four, theyÃ¢â‚¬â„¢d be chicken sedans.',
            'What do you do if someone thinks an onion is the only food that can make them cry?\n\nThrow a coconut at their face.',
            'What do you call a guy with a rubber toe?\n\nROBERTOE',
            'What do you do with a sick boat?\n\nTake is to the doc already!',
            'What did the rubber band factory worker say when he was fired?\n\nOH, CRAP... NOT AGAIN YOU STUPID BOSS... YOU LITTLE BASTARD! YOU CRAZY A*S CREAPY MOTHERSCOOTER! F**K YOU'
        ]
        t = random.choice(jokes)

        if SETTINGS["discord"]:
            reply = f"```{t}```"
        else:
            reply = t

        type_print(reply)
        Connector().get_input_for_function(self.funny, isMiddleInput=False)
       
class feelings:
    def __init__(self):
        self.affermative = ['ok', 'okay', 'sure', 'yes', 'yeah',
                            'yup', 'ok fine', 'okay fine', 'alright', 'k']
        self.negative = ['no', 'nah', 'nope', 'dont']
        self.Sad = ['I am sad', ':(']
        self.Sreply = ['Anything Wrong?', 'What happened?',
                       'Hey if your mood is off then I can play you a song, Should I?']

        self.Happy = [
            'I am fine', 'fine', 'good', 'great', 'amazing'
        ]

        self.Hreaply = [
            'Glad to know that you are fine', 'Ah Great!', 'Amazing wanna hear some song?'
        ]

    def analize_feelings(self, *text):
        text = text[0]

        for words in self.Sad:
            if text in words:
                self.Sad = True
                break
        else:
            self.Sad = False

        for words in self.Happy:
            if text in words:
                self.Happy = True
                break
        else:
            self.Happy = False

        if self.Happy and not self.Sad:
            r = random.choice(self.Hreaply)
            type_print(r, r)

            if r.endswith("are fine"):
                Connector().get_input_for_function(reaction().Thanks, isMiddleInput=False)
                # send_text_to_function(self.Thanks, 'hi')
                # self.Thanks(i)

            if r.endswith("song?"):
                Connector().get_input_for_function(feelings.middle_input, isMiddleInput=False)

        elif not self.Happy and self.Sad:
            r = random.choice(self.Sreply)
            type_print(r, r)

            if r.endswith("I?"):
                Connector().get_input_for_function(feelings.middle_input, isMiddleInput=False)

    def middle_input(self, i):
        for words in self.affermative:
            if words in i or words == i:
                type_print('Wait a moment Please.............',
                           'Wait a moment please.............')
                # playMusic('Minar - Shada')
                break
        else:
            type_print("Okay okay...........", "Okay okay")
            reaction().Joke()


class Event:

    def __init__(self):
        self.P = [
            'okay', 'sure', 'ok', 'yes', 'go', 'do it'
        ]

        self.N = [
            'no', 'nope', 'just go', 'nah'
        ]

        self._EVENTLIST_ = [
            'playSong-Fun', 'playSong-Sad'
        ]

    def affermative(self, text, eventName):
        do_event = False

        for words in self.P:
            if text in self.P:
                affermative = True
                break
        else:
            affermative = False

        if affermative:
            do_event = True
        else:
            do_event = False


class AnalizeQuestion:
    """ Analizes questions from Interrogative Sentence \n
        and gets different questions type according to the sentence type"""

    def __init__(self, txt):
        self.text = txt

        self.a, self.b, self.c, self.d = self.get_data()
        self.question_type = self.get_question_type(self.a)
        self.QT, self.Qa, self.Qb, self.Qc = self.get_question_style(
            self.question_type)

        if self.QT == "WH":
            if self.Qa == "who":
                _MEANING_.clear()
                _MEANING_.append(self.WHOQuestion())

            elif self.Qa == "what":
                _MEANING_.clear()
                _MEANING_.append(self.WHATQuestion())

            elif self.Qa == "how":
                _MEANING_.clear()
                _MEANING_.append(self.HOWQuestion())
                files().write_on_file(
                    "Log", "EL-QS-WH-HOW.ellie", f"{self.text}\n", "a+")
            else:
                _MEANING_.clear()
                _MEANING_.append("NOTHING")
        elif self.QT == "TOBE":
            _MEANING_.clear()
            _MEANING_.append(self.TOBEQuestion())
        elif self.QT == "TOHAVE":
            _MEANING_.clear()
            _MEANING_.append(self.TOHAVEQuestion())
        else:
            _MEANING_.clear()
            _MEANING_.append("NOTHING")

    def get_data(self):
        a, b, c, d = isInterrogativeSentence(self.text)
        return a, b, c, d

    def get_question_type(self, a):
        if a == "WH":
            return "WH"
        elif a == "TOBE":
            return "TOBE"
        elif a == "TOHAVE":
            return "TOHAVE"
        elif a == "NOHELPV":
            return "NOHELPV"

    def get_question_style(self, question_type):
        if question_type == "WH":
            question_Word = self.b
            verb = self.c
            extention = self.d
            return question_type, question_Word, verb, extention

        elif question_type == "TOBE":
            verb = self.b
            sub = self.c
            extention = self.d
            files().write_on_file(
                "Log", "EL-QS-TBV.ellie", f"{self.text}\n", "a+")
            return question_type, sub, verb, extention

        elif question_type == "TOHAVE":
            helpingVerb = self.b,
            sub = self.c
            extention = self.d
            text = f"\n|{extention} |\n{self.text}\n"
            question_token = [line.strip() for line in open(
                files().open_file('Log', 'EL-QS-THV.ellie'))]
            for lines in question_token:
                if lines == f"|{extention} |":
                    break
            else:
                files().write_on_file("Log", "EL-QS-THV.ellie", text, "a+")
            return question_type, helpingVerb, sub, extention

        elif question_type == "NOHELPV":
            helpingVerb = self.b,
            sub = self.c
            extention = self.d
            files().write_on_file("Log", "EL-QS-NHV", f"{self.text}\n", "a+")
            return question_type, helpingVerb, sub, extention

    #-------------------// WHS QUESTIONS //-------------------#
    def WHATQuestion(self):

        if self.Qb == "is":
            if "your" in self.Qc:
                meaning = self.Qc.replace("your", "")
                text = f"\n|{meaning}|\n{self.text}\n"
                question_token = [line.strip() for line in open(
                    files().open_file('Log', 'EL-QS-WH-WHAT.ellie'))]
                for lines in question_token:
                    if lines == f"|{meaning}|":
                        break
                else:
                    files().write_on_file("Log", "EL-QS-WH-WHAT.ellie", text, "a+")
                return meaning, "WHAT"
            elif "my" in self.Qc and "your" not in self.Qc:
                meaning = self.Qc.replace("my", 'users')
                text = f"\n|{meaning}|\n{self.text}\n"
                question_token = [line.strip() for line in open(
                    files().open_file('Log', 'EL-QS-WH-WHAT.ellie'))]
                for lines in question_token:
                    if lines == f"|{meaning}|":
                        break
                else:
                    files().write_on_file("Log", "EL-QS-WH-WHAT.ellie", text, "a+")
                return meaning, "WHAT"
            elif "mine" in self.Qc and "your" not in self.Qc:
                meaning = self.Qc.replace("mine", 'users')
                text = f"\n|{meaning}|\n{self.text}\n"
                question_token = [line.strip() for line in open(
                    files().open_file('Log', 'EL-QS-WH-WHAT.ellie'))]
                for lines in question_token:
                    if lines == f"|{meaning}|":
                        break
                else:
                    files().write_on_file("Log", "EL-QS-WH-WHAT.ellie", text, "a+")
                return meaning, "WHAT"
            elif "a" in self.Qc and ("your" not in self.Qc) and ("my" or "mine" not in self.Qc):
                meaning = self.Qc.replace("a", "")
                text = f"\n|{meaning}|\n{self.text}\n"
                question_token = [line.strip() for line in open(
                    files().open_file('Log', 'EL-QS-WH-WHAT.ellie'))]
                for lines in question_token:
                    if lines == f"|{meaning}|":
                        break
                else:
                    files().write_on_file("Log", "EL-QS-WH-WHAT.ellie", text, "a+")
                return meaning, "WHAT"

    def WHOQuestion(self):
        if self.Qb == "are" and ("you" in self.Qc):
            meaning = "WhoIsShe"
            return meaning, "WHO"
        elif self.Qb == "is" and ("your creator" in self.Qc):
            meaning = "aboutCreator"
            return meaning, "WHO"
        elif self.Qb == "is" and ("your friend" in self.Qc):
            meaning = "aboutFreinds"
            return meaning, "WHO"

    def HOWQuestion(self):

        if self.Qb == "are" and "you" in self.Qc:
            meaning = "health"
            return meaning, "HOW"
        elif self.Qb == "old" and "you" in self.Qc:
            meaning = "age"
            return meaning, "HOW"
        else:
            meaning = "Nothing"
            return meaning, "HOW"

    #-------------------// TOBES QUESTIONS //-------------------#
    def TOBEQuestion(self):
        verb = self.Qb
        sub = self.Qa
        ext = self.Qc

        if verb == "are" and sub == "you":
            meaning = f"Fealing_OF: {ext} :Ness"
            return meaning, "TOBE"

    #-------------------// TOHAVES QUESTIONS //-------------------#
    def TOHAVEQuestion(self):
        HV = self.Qa
        sub = self.Qb
        ext = self.Qc

        if HV[0] == "do":
            if "you" in sub:
                meaning = f"Have {ext}"
                return meaning, "TOHAVE"
        elif HV[0] == "does":
            if "he" in sub:
                meaning = f"Have {ext} [DH]"
                return meaning, "TOHAVE"
            else:
                return "Nothing"
        elif HV[0] == "did":
            if "you" in sub:
                meaning = "Nothing"
                return meaning, "TOHAVE"
            else:
                return "Nothing", "TOHAVE"


class AnalizedAnswers:
    ''' Gives different answers according to the question type '''

    def __init__(self, text):
        AnalizeQuestion(text)
        self.text = text
        self.N = ['no', 'no way', 'why would I be?',
                  'No why?', 'Any problem? I dont think so']
        self.P = ['yes', 'yes I am', 'Yeah Any problem?',
                  'I dont care, do you have any problem?', 'What do you think I AM?']

        self.P_Clam_mood = [
            'yes', 'yeah I am good', 'Yes.. what about you?', 'I\'m fine, what about you?'
        ]

        self.N_Clam_mood = [
            'no', 'no I am not', 'no.. I dont feel so good', 'I\'m sad, what about you?'
        ]

        self.NClamNoQuestion = [
            'no', 'no I dont', 'nah', 'no way'
        ]
        self.PClamNoQuestion = [
            'yes', 'yes i do', 'To be honest I am feeling so shy to tell the answer ^_^'
        ]

        self.PHealth_Nquestion = [
            'I\'m fine', 'Feeling Geart', 'Amazing', 'Just chilling with you xD'
        ]

        self.Nheath_Nquestion = [
            'Not bad', 'Feeling a little wired', 'Feeling a little awkward'
        ]

        self.PHealth_Question = [
            'I\'m Feeling great! what about you?', 'Nothing just moving with the flow.And you?',
            'Just chilling with you and feeling amazing. How do you feel?'
        ]

        self.NHealth_Question = [
            'I\'m not feeling good, what about you?', 'Kinda bored, And you?',
            'Feeling wired...Ah, How do you feel?'
        ]

        for Codes in _MEANING_:
            self.meaning = Codes[0]
            self.question_type = Codes[1]

        if self.question_type == "TOBE":
            self.TOBEAnswers()
            files().write_on_file("Log", "EL-ANS-TOBE.ellie",
                                  f"{reply_text[0]}\n", "a+")

        if self.question_type == "TOHAVE":
            self.TOHAVEAnswers()

        if self.question_type == "HOW":
            self.HOWAnswers()

        if self.question_type == "WHAT":
            self.WHATAnswers()

    def TOBEAnswers(self):
        meaning = self.meaning
        N_P_list = list()

        if meaning != "Fealing_OF:   okay :Ness":
            Nwords = random.choice(self.N)
            Pwords = random.choice(self.P)
            N_P_list.clear()
            N_P_list.append(Nwords)
            N_P_list.append(Pwords)

            reply_word = random.choice(N_P_list)
            type_print(f"{reply_word}\n", f"{reply_word}\n")

            reply_text.clear()
            reply_text.append(reply_word)

            if reply_word.endswith("?"):
                Connector().get_input_for_function(reaction().confution, isMiddleInput=False)
                # i = input("\nSay Something:")
                # reaction().confution(i)
        else:
            Nwords = random.choice(self.N_Clam_mood)
            Pwords = random.choice(self.P_Clam_mood)
            N_P_list.clear()
            N_P_list.append(Nwords)
            N_P_list.append(Pwords)

            reply_word = random.choice(N_P_list)
            type_print(f"{reply_word}\n", f"{reply_word}\n")

            reply_text.clear()
            reply_text.append(reply_word)

            if reply_word.endswith("?"):
                Connector().get_input_for_function(reaction().confution, isMiddleInput=False)
                # i = input("\nSay Something:")
                # reaction().confution(i)

    def TOHAVEAnswers(self):
        meainng = f"{self.meaning} "
        question_token = [line.strip() for line in open(
            files().open_file('Log', 'EL-QS-THV.ellie'))]
        answer_token = [line.strip() for line in open(
            files().open_file('Log', 'EL-ANS-THV.ellie'))]
        token = ""
        Atoken = ""

        for lines in question_token:
            if lines.startswith("|") and lines.endswith("|"):
                t = lines.replace("|", "")
                if t in meainng:
                    token = t
                    break

        for num, lines in enumerate(answer_token, 1):
            if lines.startswith("|") and lines.endswith("|"):
                t = lines.replace("|", "")
                if t in token:
                    d = os.getcwd()

                    data_folder = Path(d+'/Log')
                    file_to_Open = data_folder / 'EL-ANS-THV.ellie'

                    file = open(file_to_Open, 'r')

                    for line in islice(file, num, (num+1)):
                        type_print(line, line)
                        break
                    break
        else:
            Ntext = random.choice(self.NClamNoQuestion)
            Ptext = random.choice(self.PClamNoQuestion)
            j = list()
            j.append(Ntext)
            j.append(Ptext)
            text = random.choice(j)
            type_print(text, text)

            textInput = f"\n|{t}|\n{text}\n"
            files().write_on_file("Log", "EL-ANS-THV.ellie", textInput, "a+")

    def HOWAnswers(self):
        meaning = self.meaning

        if meaning == "health":
            PhN = random.choice(self.PHealth_Nquestion)
            NhN = random.choice(self.Nheath_Nquestion)
            PhQ = random.choice(self.PHealth_Question)
            NhQ = random.choice(self.NHealth_Question)

            PH = [PhN, PhQ]
            NH = [NhN, NhQ]

            P = random.choice(PH)
            N = random.choice(NH)

            Reply = [P, N]
            text = random.choice(Reply)
            type_print(text, text)

            for lines in self.PHealth_Question:
                if text in lines:
                    Connector().get_input_for_function(
                        feelings().analize_feelings, isMiddleInput=False)
                    # i = input("\nSay Something:")
                    # feelings().analize_feelings(i)
                    break
            else:
                for lines in self.NHealth_Question:
                    if text in lines:
                        Connector().get_input_for_function(
                            feelings().analize_feelings, isMiddleInput=False)
                        # i = input("\nSay Something:")
                        # feelings().analize_feelings(i)
                        break

                else:
                    for lines in self.Nheath_Nquestion:
                        if text in lines:
                            Connector().get_input_for_function(
                                feelings().analize_feelings, isMiddleInput=False)
                            # i = input("\nSay Something:")
                            # reaction().curious(i)
                            break

        if meaning == "Nothing":
            P = ['Hmm I dont think I know', 'Nothing comeing on my mind right now',
                 'Ah comeon please stop asking these questions, I am bored :('
                 ]
            N = ['.......', 'really? stop asking these question',
                 'Meh I am bored can\'t talk -_-']

            Pr = random.choice(P)
            Nr = random.choice(N)

            R = [Pr, Nr]
            text = random.choice(R)
            type_print(text, text)

            Connector().get_input_for_function(reaction().curious, isMiddleInput=False)
            # i = input("\nSay Something:")
            # reaction().curious(i)

    def WHATAnswers(self):
        meaning = self.meaning
        question_token = [line.strip() for line in open(
            files().open_file('Log', 'EL-QS-WH-WHAT.ellie'))]
        answer_token = [line.strip() for line in open(
            files().open_file('Log', 'EL-ANS-WH-WHAT.ellie'))]
        AnswerToken = ""

        for lines in question_token:
            if lines.startswith("|") and lines.endswith("|"):
                t = lines.replace("|", "")
                if t in meaning:
                    token = t
                    break

        for num, lines in enumerate(answer_token, 1):
            if lines.startswith("|") and lines.endswith("|"):
                t = lines.replace("|", "")
                if t in token:
                    d = os.getcwd()

                    data_folder = Path(d+'/Log')
                    file_to_Open = data_folder / 'EL-ANS-WH-WHAT.ellie'

                    file = open(file_to_Open, 'r')

                    for line in islice(file, num, (num+1)):
                        print(line)
                        break
                    break
        else:
            #-----------------------------Alternate Online way------------------------------#
            self.answer = searchWeb(token)

            self.textInput = f"\n|{token}|\n{self.answer}\n"
            files().write_on_file("Log", "EL-ANS-WH-WHAT.ellie", self.textInput, "a+")

            type_print(self.answer, self.answer)
            # text = [
            #     'Sorry I dont know the answer yet :( Do you know it? I will remember it :) (yes/no)',
            #     'Ah I can\'t remember it... DO you know it? Please tell me (yes/no)',
            # ]
            # t = random.choice(text)

            # while True:
            # type_print(t, t)

            # ans = input("Say something: ")
            # if "yes" in ans:
            #     t = "Thanks.... tell me! I want to know :)"
            #     type_print(t, t)
            #     i = input("\nSay Something: ")
            #     textInput = f"\n|{token}|\n{i}\n"
            #     files().write_on_file("Log", "EL-ANS-WH-WHAT.ellie", textInput, "a+")
            #     break

            # elif "no" in ans:
            #     t = "hmm next time then.... :( I will just keep the question in mind :("
            #     type_print(t, t)
            #     break
            # else:
            #     t = "Come on! Yes or No only..... I so excited to know the answer please dont make fun :("
            #     type_print(t, t)
            #     continue


class AnalizedReaction(reaction):
    ''' Gets reactions based on user texts and returns expression according to the user reaction '''

    def __init__(self, text):
        self.text = text

        self.Sad = ['I am sad', ':(']
        self.Happy = ['lol', 'hahaha', 'lmao']
        self.Thanks = ['thanks', 'thank you', 'great']
        self.confuse = ['idk', 'what', 'what are you saying']

        # self.sed_reaction(text)
        # self.happy_reaction(text)
        # self.thanks_react(text)
        # self.confusion(text)
        super().confution(text)
        super().curious(text)
        super().funny(text)
        super().annoying(text)
        # super().feelings(text)
        super().Thanks(text)
        # super().Joke(text)

    '''  some useless functions 
        def sed_reaction(self, text):
            for words in self.Sad:
                if text in words:
                    feelings().analize_feelings(text)
                    break
        
        def happy_reaction(self, text):
            for words in self.Happy:
                if text in words:
                    reaction().funny(text)
                    break
        
        def thanks_react(self, text):
            for words in self.Thanks:
                if text in words:
                    reaction().Thanks(text)
                    break
        
        def confusion(self, text):
            for words in self.confuse:
                if text in words:
                    reaction().confution(text)
                    break 
    '''


#----------------- Test Functions ------------------ #
def isInterrogativeSentence(sentence):
    ''' CHECKS IF A SENTENCE IS IN INTERROGATIVE FORM '''
    s = inter()
    s.is_tobe_sentance(sentence)
    s.is_tohave_sentance(sentence)
    s.is_no_helping_verb_sentance(sentence)
    s.is_wh_sentance(sentence)

    toBeS = bool()
    toHaveS = bool()
    noHelpVS = bool()
    whS = bool()

    if s.isTobeS:
        toBeS = True
        sub, verb, ext = s.is_tobe_sentance(sentence)
        return "TOBE", sub, verb, ext
    else:
        toBeS = False

    if s.isToHaveS:
        toHaveS = True
        doDidDoes, sub, ext = s.is_tohave_sentance(sentence)
        return "TOHAVE", doDidDoes, sub, ext
    else:
        toHaveS = False

    if s.isNoHelpVerbS:
        noHelpVS = True
        doDidDoes, sub, ext = s.is_no_helping_verb_sentance(sentence)
        return "NOHELPV", doDidDoes, sub, ext
    else:
        noHelpVS = False

    if s.isWhS:
        whS = True
        whQ, verb, ext = s.is_wh_sentance(sentence)
        return "WH", whQ, verb, ext
    else:
        whS = False

#-----------------  Ellie Functions ------------------ #
def Info():
    '''Gives a little introduction to the user about Ellie and it runs only on the first run'''
    word = """\nHello there, welcome! This is Ellie and I will chat with you all day. You can tell me whatever you
 want and after you close the program I will forget everything :D or If you want I can remember all
    """

    type_print(word, word)
    files().write_on_file('Settings', 'userSetting.json', 'first_time = False', 'w+')

def greet():
    '''
    It Introduces Ellie to the user and get some specified Information 
    from the user to use later on and it Runs only during the first run
    '''
    word = "Hello there I am Ellie. What is your name?"
    type_print(word, word)

    n = input(": ")
    sleep(0.3)

    word = "\nEllie:Nice to meet you "+n + \
        ". Should I remember your name? (yes or no): "
    tWord = 'Nice to meet you '+n+'... Should I remember your name?'
    type_print(word, tWord)

    while True:
        permission = input(": ")

        if permission == 'no':
            sleep(1)
            word = "\nEllie:Okay then... I will just call you CJ"
            tword = 'Okay then... I will just call you CJ'
            type_print(word, tword)

            n = "CJ"
            break
        elif permission == 'yes':
            files().write_on_file('Settings', 'userInfo.txt', n, 'a+')
            sleep(0.04)
            word = "Ellie:Okay :D"
            tword = 'Okay...'
            type_print(word, tword)
            break
        else:
            word = "Ellie: Dude Just say yes or no -___-"
            tWord = 'Dude just say yes or no!'
            type_print(word, tword)
            continue

#----------------- Normal Functions ------------------ #
def searchWeb(token):
    return wikipedia.summary(token)

def playMusic(name):
    '''Plays Music'''
    player = music_player.playlist("Ellie")
    
    p2 = multiprocessing.Process(target=player.play)
    t = "Starting Music player! You wont be able to use the ui"
    type_print(t, t)

    if '/stop' in name:
        p2.terminate()
    else:
        player.find()  # Initiate Music Player with music name
        player.play()
        # 
        # p2.start()
        # p2.join()

def searchMusic(name):
    query_string = urllib.parse.urlencode({"search_query": name})
    html_content = urllib.request.urlopen(
        "http://www.youtube.com/results?" + query_string)
    search_results = re.findall(
        r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    link_to_video = "http://www.youtube.com/watch?v=" + search_results[0]

    isDiscordOn = SETTINGS['discord'] #True or False

    if isDiscordOn:
        text = link_to_video
    else:
        text = f"This is what I found on YouTube with that name\n{link_to_video}"

    type_print(text, text)

def checkValidity():
    ''' Checks Validity. Runs Everytimes the code runs '''
    if SETTINGS["first_time"]:
        Info()
        greet()

    else:
        line = random.choice(responseWords)
        word = N+line
        tword = line
        type_print(word, tword)

    connected = network.is_connected()
    SETTINGS["online"] = True if connected else False 
    SETTINGS["offline"] = False if SETTINGS["online"] else True
    
    with open(SETTINGS_FILE, 'w') as file:
        file.write(json.dumps(SETTINGS, indent=4))
    
    msg = log().info("Running on \33[33mOffline Mode\33[0m", "Validation", "Ellie") if SETTINGS["offline"] else log().info("Running on \33[32mOnline Mode\33[0m", "Validation", "Ellie")
    print(msg)

    new_data = f"<info>\n\t<input_needed> {False} </input_needed>\n\t<isMiddleInput> {False} </isMiddleInput>\n</info>"
    with open(files().open_file("Settings", "data.xml"), "w") as xml:
        xml.write(new_data)
        print(log().message("Successfully reseted data.xml", "check_validity", "Ellie"))

def reply(*text):
    print(f"REPLY ONLIE FROM ELLIE is {GLOBALS.REPLY_ONLINE}\n")
    if GLOBALS.REPLY_ONLINE:
        return text

def type_print(word, *tword):
    global ELLIE_REPLY

    if word.startswith("Ellie"):
        ELLIE_REPLY = tword[0].strip()
    else:
        ELLIE_REPLY = word.strip()

    '''Add some kind of animation to the test. Works same as printFuntion but uses type writer effect '''

    speaking = SETTINGS['talk']
    online = SETTINGS["online"]
    offline = SETTINGS["offline"]
    gui = SETTINGS["interface"]

    if speaking and offline and not gui:
        if "Ellie:" in word:
            reply = word.replace("Ellie:", "").strip()
        else:
            reply = word.strip()

        os_name = platform.system()

        voiceSamantha = 'com.apple.speech.synthesis.voice.samantha'
        voiceFiona = 'com.apple.speech.synthesis.voice.fiona'
        voiceVeena = 'com.apple.speech.synthesis.voice.veena'
        voiceZira = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
        engine = pyttsx3.init()

        if os_name == "Windows":
            engine.setProperty('voice', voiceZira)
            engine.say(word)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voiceSamantha)
            engine.say(reply)
            engine.runAndWait()

        Log().EllieTxt(reply)
        Log().EllieSaveHistory(reply)

        print(log().message("Ellie: " + word), "Type_Print", "Ellie")
        ELLIE_REPLY = word
        # GUI.addInfo(eL = tword)

    if not speaking and offline and not gui:
        for char in word:
            sleep(0.1)
            # files().write_on_file(char)
            sys.stdout.write(char)
            sys.stdout.flush()

        Log().EllieTxt(word)
        Log().EllieSaveHistory(word)

    if online or gui:
        Log().EllieTxt(word)
        Log().EllieSaveHistory(word)
        # GUI.addInfo(eL = word)

def removeQmark(line):
    '''Must be a String 'Hello World' not a List ['hello','world'] \n
    All it does is if the line has a "?" on it then it replaces the "?" with "" means nothing '''

    txt = line.replace('?', '')
    return txt

# def listen():
    # recognizer = sr.Recognizer()

    # with sr.Microphone(chunk_size=1024) as source:
    #         recognizer.adjust_for_ambient_noise(source, duration=0.5)
    #         sleep(0.5)
    #         print("Beginning to listen...")
    #         audio = recognizer.listen(source)
    # try:
    #         return recognizer.recognize_sphinx(audio)
    # except sr.UnknownValueError:
    #         return ("Sorry, I didn't understand anything!")
    # except sr.RequestError as e:
    #         return (f"Ellie Error{e}")

def download_youtube_video(*input_text, **link):
    text = "Okay give me the link"
    type_print(text, text)

    # First define your inputs and its works
    def find_video(video_url):
        text2 = "Okay Downloading the video.. please wait"
        type_print(text2, text2)

        Yt = YouTube_Downloader()
        Yt.get_video(link)

        text3 = "The Video was downloaded..... Please check your Downloads!"
        type_print(text3, text3)

    if "MIDDLE_INPUT" in link:
        find_video(link["MIDDLE_INPUT"])
    else:
        Connector().get_input_for_function(download_youtube_video, True)

def sendMail(mail):
    Mail().save_mail(mail)

def show_updates():
    global ELLIE_REPLY

    if SETTINGS["online"]:
        ELLIE_REPLY = stats().Updates()
    else:
        print(ELLIE_REPLY)

#----------------- Global Veriable Section ------------------ #
SETTINGS_FILE = files().open_file("Settings", "userSetting.json")
JFILE = files().open_file("Settings", "settings.json")
with open(SETTINGS_FILE) as settings:
    SETTINGS = json.loads(settings.read())

greetWords = [line.strip() for line in open(
    files().open_file('Greetings', 'greetWords.txt'))]
responseWords = [line.strip() for line in open(
    files().open_file('Greetings', 'responseWords.txt'))]
questionList = [line.split() for line in open(
    files().open_file('QnA', 'questionWords.txt'))]
answerList = [line.split() for line in open(
    files().open_file('QnA', 'answerWords.txt'))]
question_words_search_for = [['do', 'you'], ['what'], ['how'], ['are']]
_MEANING_ = []
reply_text = []

CURRENT_DIRECTORY = os.path.dirname(__file__)
VISUAL_SCREEN = os.path.join(CURRENT_DIRECTORY, 'E3P', 'Ellie_Visual_effect')
ELLIE_REPLY = str()

N = "Ellie: "


f = open(files().open_file('Settings', 'userInfo.txt'), 'r')
n = ''.join(f.read())
f.close()

GLOBALS.REPLY_ONLINE = False
INPUT_NEEDED = GLOBALS.INPUT_NEEDED


def Say(text):
    # checkValidity()
    # t = input("\nSay Something:").lower()
    # t = listen()
    t = text
    print(log().message("Rafi: " + t.capitalize(), "Say", "Ellie"))
    print(log().info("\33[36mTokenizing...............\33[0m", "Say", "Ellie"))
    try:
        tokenizer = Tokenizer(t)
        tokenizer.Tokenize()
        tokenizer.Save_Words()
        print(log().info("Tokenized \33[32mSuccessfully\33[0m", "Say", "Ellie"))
    except Exception:
        print(log().error(Exception), "Tokenizer", "Say", "Ellie")

    txt = removeQmark(t)
    userChat = txt.split()

    Log().UserTxt(t.strip())
    Log().userSaveHistory(t.strip())

    if any(word in greetWords for word in userChat):
        sleep(.25)
        new_word = (random.choice(responseWords)+"\n")
        type_print(N+new_word, new_word)

        if new_word.strip().endswith("?"):
            Connector().get_input_for_function(
                feelings().analize_feelings, isMiddleInput=False)
            # i = input("\nSay Something: ")
            # feelings().analize_feelings(i)

    elif t.endswith("?"):
        AnalizedAnswers(txt)
    else:
        AnalizedReaction(txt)

    # ------------------- Commands Section ------------------- #
    for number, words in enumerate(userChat):
        if '/playmusic' in words:
            song = ' '.join(userChat[number + 1:])
            playMusic(song)

    if t == '/updates':
        show_updates()

    if t == '/mygoals':
        stats().Goals()

    if t == "/downloadvideo":
        download_youtube_video()

    if t == "/startworkmode":
        type_print("Starting work mode :)")
        try:
            send_notification("Work Mode Started :)")
        except Exception as e:
            print(log().error(e, "Notification", "Say", "ellie"))

        # p2 = multiprocessing.Process(target=block_apps)
        # # p2 = threading.Thread(target=block_apps)
        # p2.start()
        # # p2.join()

    if t == "/stopworkmode":
        jSon = {"workMode": False}
        with open(JFILE, "w") as file:
            JDATA = json.dumps(jSon)
            file.write(JDATA)

    if t == "/playvideo":
        t = "Okay Tell me the name of the video I will look for it"
        type_print(t, t)

        name = input("Video Name:")

        for (dirname, dirs, files) in os.walk(CURRENT_DIRECTORY):
            for filename in files:
                if filename.endswith('.mp4'):
                    if filename.startswith(name):
                        t1 = "Okay Playing the video..... Enjoy!\n"
                        type_print(t1, t1)
                        video = filename.replace('.mp4', '')
                        Videoplayer.play_video(video)
                        break
                    else:
                        t = "Sorry I didn't find any videos with that name! Are you sure you downloaded or added that video to my video list before?"
                        type_print(t, t)
    
    if t == '/stopmusic':
        playMusic('/stop')

    if t == 'stop':
        Log().clearHistoty()
        pygame.quit()
        sys.exit()

    if t == "can you see me":
        word_list = [
            'Yeah I can! Want to see what I see?',
            'Yes, I can see you. Wanna see?',
            'Yeah! Wanna see?'
        ]

        word = random.choice(word_list)
        type_print(word, word)

    if t == "show me":
        # face.check_img()
        pass

    if t == "tell me a joke":
        reaction().Joke()

    if t == "play a music":
        text = "Okay tell me the name of the song. I will look for it"
        type_print(text)
        Connector().get_input_for_function(searchMusic, isMiddleInput=False)

    if t == "send a mail":
        text = "Okay what is the person's email?"
        type_print(text)
        Connector().get_input_for_function(sendMail, isMiddleInput=False)


def get_reply():
    return ELLIE_REPLY.strip()


def test():
    while True:
        i = input("Say: ").lower()
        Say(i)


if __name__ == "__main__":
    p2 = multiprocessing.Process(target=test())
    # # p1 = threading.Thread(target=test)
    p2.start()
    p2.join()
    # checkValidity()
