import os
import pickle
import json
from misc import files, log
from xml.dom.minidom import parse


class XML:
    def __init__(self):
        pass

    def read(self, file, tag_name):
        DOMTree = parse(file)
        collection = DOMTree.documentElement

        tag = collection.getElementsByTagName(tag_name)[0]
        value = tag.childNodes[0].data

        return eval(value)


class JSON:
    def __init__(self):
        pass

    def read(self, file):
        self.fileName = file

        try:
            with open(file, "r") as settings:
                self.JFile = json.loads(settings.read())
        except Exception as e:
            self.JFile = None
            print(log().error("Error Reading Json: " + e, "connector", "Ellie"))

        return self.JFile

    def write(self, Dict, file):

        try:
            with open(file, 'w+') as outfile:
                json.dump(Dict, outfile)
        except Exception as e:
            print(log().error("Error Writing Json: " + e, "connector", "Ellie"))


class Connector:
    def __init__(self):
        self.function_name = str
        self.input_text_for_function = str
        self.input_int_for_function = int

    def get_input_for_function(self, func, isMiddleInput):
        """ 
        Description:
        ------------------------------------------
        Sends a input request for a function.\n
        
        Usage:
        -----------------------------------------
        ```py
        # If input required in the middle of function
            Connector().get_input_for_function(function_name, True)
        #else
            Connector().get_input_for_function(function_name, False)
        ```
        """
        self.function_name = func

        try:
            filename = files().open_file("Settings", "data.pickle")
            outfile = open(filename, 'wb')
            pickle.dump(func, outfile)
            outfile.close()
        except Exception as e:
            print(log().error("Error writing on pickle file:", "Connector", "Ellie"), e)

        if isMiddleInput == True:
            new_data = f"<info>\n\t<input_needed> {True} </input_needed>\n\t<isMiddleInput> {True} </isMiddleInput>\n</info>"
        else:
            new_data = f"<info>\n\t<input_needed> {True} </input_needed>\n\t<isMiddleInput> {False} </isMiddleInput>\n</info>"

        try:
            with open(files().open_file("Settings", "data.xml"), "w") as xml:
                xml.write(new_data)
        except Exception as e:
            print(log().error(f"Error Editing xml data: {e}", "Connector", "connector"))

    def send_input_text_to_function(self, input_text, function_name, **onther_inputs):
        """
        It sends the input text to the desired funtion
        ---------------------------------------------------------------
        `IF THE FUNCTION SUPPORTS MIDDLE_INPUT THEN THE FIRST ARG SHOULD BE *ARGS`
        
        Example:
        ============

        Functions without input in the middle:
        ------------------------------------------------------
        ```py
            from connector import Connector
            def a(text):
                print(a)
                Connector.send_input_text_to_function("Hello", a)
        ```
        Functions with input in the middle:
        ------------------------------------------------------
        from connector import Connector
        ```py
        def a(*text, **text2):
        
           #First define your inputs and its works
           def middle_input(text2):
               print(text2)
        
           if "MIDDLE_INPUT" in text2:
               middle_input(text2["MIDDLE_INPUT"])
        
          #then define normal functions work
           if not len(text) == 0:
               print(text[0])
        
        Connector.send_input_text_to_function(
                    "FIRST_TEXT", MIDDLE_INPUT="SECONDARY_TEXT")
        ```
        """
        file_name = files().open_file("Settings", "data.xml")
        # xml_file = os.path.join(os.getcwd(), file_name)
        isMiddleInput = XML().read(file_name, "isMiddleInput")
        isInputedNeeded = XML().read(file_name, "input_needed")

        if isInputedNeeded == True:
            # self.function_name = XML.read()
            try:
                infile = open(files().open_file(
                    "Settings", "data.pickle"), "rb")
                self.function_name = pickle.load(infile)
                infile.write("")
                infile.close()
            except Exception as e:
                print(log().error(f"Error writing pickle file", "send_input_to_function", "Connector"))
        else:
            self.function_name = function_name

        self.input_text = input_text

        new_data = f"<info>\n\t<input_needed> {False} </input_needed>\n\t<isMiddleInput> {False} </isMiddleInput>\n</info>"


        try:
            with open(files().open_file("Settings", "data.xml"), 'w') as xml:
                xml.writelines(new_data)
        except Exception as e:
            print(log().error(f"Error Editing xml data: {e}", "send_input_to_function", "connector"))

        # if type(self.function_name) == str:
        #     print(f"Sending data to {function_name.__name__}\n")
        #     function_name(self.input_text)
        # else:
        msg = log().message(f"Sending data to {self.function_name.__name__}", "send_input_text", "connector")
        print(msg)
        if isMiddleInput == True:
            if onther_inputs["MIDDLE_INPUT"]:
                self.function_name(MIDDLE_INPUT=self.input_text)
            else:
                self.function_name(self.input_text)
        else:
            self.function_name(self.input_text)

# file = files().open_file("Settings", "data.xml")
# XML().read(file, "isMiddleInput")
