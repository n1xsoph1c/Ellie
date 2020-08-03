""" CHECK IF A SENTENCE IS IN INTERROGATIVE FORM """

import os
from misc import files

def Write(folderName, fileName, text, openType):
    '''Writes some text to a file on a folder'''
    d = os.getcwd()

    file_to_Open = os.path.join(d, folderName, fileName)

    f = open(file_to_Open, openType)
    f.writelines(text)
    f.close()

def Open(folderName, fileName):
    '''Opens a specific file from a different directory'''
    d = os.getcwd()
    
    # data_folder = os.path.join(d, folderName)
    file_to_Open = os.path.join(d, folderName, fileName)
    return file_to_Open


class Interrogative():

    isTobeS = False
    isToHaveS = False
    isNoHelpVerbS = False
    isWhS = False

    tbVerbs = ["am", "is", 'are', 'was', 'were']


    TVerbs = [line.strip() for line in open(files().open_file('wordNet','verb.exc'))]
    Verbs = [words.split() for a, words in enumerate(TVerbs)]
    VerbsA = list()
    VerbsB = list()

    Sub = ["he", "she", "you", "they", "that", "I"]
    Ext = list()

    for a, b in enumerate(Verbs):
        VerbsA.append(b[0])
        VerbsB.append(b[1])
 

    def is_tobe_sentance(self, sentence):
        """
        Verb + sub + Extention + ?\n
        Example: Are you okay?
        """

        s = sentence
        

        verb = str()
        sub = str()
        ext = ()

        a = bool()
        b = bool()
        c = bool()

        for verbs in self.tbVerbs:
            if s.startswith(verbs):
                verb = verbs
                sub = s.replace(verbs, "")
                a = True
                break
            else:
                a = False

        for subs in self.Sub:
            if subs in s:
                sub = subs
                b = True
                break
            else:
                b = False
     
        ext = s.replace(verb, "")
        ext = ext.replace(sub, "")
        ext = ext[ext.index(" "):]

        for verbs in self.VerbsA:
            if verbs in ext:
                c = False
                break
            else:
                c = True

        if a and b and c:
            self.isTobeS = True
        else:
            self.isTobeS = False

       

        return verb, sub, ext

    def is_tohave_sentance(self, sentence):
        """
        Do/does/did + subject + have + Ext + ?\n
        Example: Do you have a car?
        """
        
        s = sentence
        
        sub = str()
        ext = str()
        d = ["do", "did", "does"]
        hV = str()
        a = bool()
        b = bool()
      

        for verbs in d:
            if s.startswith(verbs):
                sub = s[s.index(" "): s.index(" ", s.index(" ") + 1)]
                a = True
                hV = verbs
                if "have" in s:
                    ext = s[s.index(" ", s.index("have")): ]
                    b = True

                    if ext.startswith(" "):
                        ext.replace(" ", "")
                    else:
                        ext = ext
                else:
                    b = False
                break
            else:
                a = False

        if a and b:
            self.isToHaveS = True
        else:
            self.isToHaveS = False
        
        return hV, sub, ext

    def is_no_helping_verb_sentance(self, sentence):
        """
        Do/Did/Does + subject + verb + Ext + ?\n
        Example: Do you like to play games?
        """
        
        s = sentence

        sub = str()

        ts = str()
        
        a = bool()
        b = bool()
        c = bool()

        d = ["do", "did", "does"]
        hV = str()

        
        for words in d:
            if s.startswith(words):
                hV = words
                a = True
                st = s[s.index(" ") + 1: s.index(" ", s.index(" ") + 1)]
                for subs in self.Sub:
                    if subs == st:
                        sub = subs
                        b = True
                        break
                    else:
                        b = False
                break
            else:
                a = False
            
        ts = s[s.index(sub, s.index(" ")):]

        if ts.startswith(sub):
            ts = ts[ts.index(" ") + 1 :]


        for v in self.tbVerbs:
            if v not in ts:
                c = True
                ext = ts
                
            else:
                c = False

        if a and b and c and not self.isToHaveS:
            self.isNoHelpVerbS = True
        else:
            self.isNoHelpVerbS = False

        return hV, sub, ext

    def is_wh_sentance(self, sentence):
        """
        who, which, whom, when, why, what, where, whoes, how + verb + sentnce\n
        Example: Who did this?
        """
        
        s = sentence
    
        ext = str()
        verb = str()
        q = str()
        wh_Q = ["who", "which", "whom", "why", "what", 'where', 'whoes', 'how']
        
        for qs in wh_Q:
            if s.startswith(qs):
                self.isWhS = True
                q = qs
                verb = s[s.index(" ") + 1: s.index(" ", s.index(" ") + 1)]
                
                ext = s[s.index(verb) + len(verb) + 1: ]
                
                break
            else:
                self.isWhS = False

        return q, verb, ext
