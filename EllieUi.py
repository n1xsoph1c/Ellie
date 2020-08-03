from kivy.app import App
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.behaviors import CoverBehavior
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.graphics import Ellipse, RoundedRectangle
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

from Ellie import Say, get_reply, checkValidity
from misc import files, log
from connector import Connector, XML

import os
import kivy
import pickle
import multiprocessing
import textwrap
import json

settings_file = files().open_file("Settings", "userSetting.json")
kivy_file = os.path.join(os.getcwd(), "Lib", "ELLIEUI", "ellie.kv")
# FaQ_file = files().open_file("")
Builder.load_file(kivy_file)

Window.borderless = False


class MainMenu(Image, CoverBehavior, Screen):
    def Music(self):
        self.msg = "Working!"
        print(log().message(self.msg, "customize", "EllieUI"))

    def Radio(self):
        self.msg = "Working!"
        print(log().message(self.msg, "settings", "EllieUI"))

    def Video(self):
        self.msg = "Working!"
        print(log().message(self.msg, "contact", "EllieUI"))

    def Theme(self):
        self.msg = "Working!"
        print(log().message(self.msg, "guide", "EllieUI"))

    label_wid = ObjectProperty()
    info = StringProperty()

    def get_text(self):
        self.label_wid.text = 'My label after button press'

    def text(self, val):
        self.text_analizer(val)
        self.value = textwrap.fill(get_reply().capitalize(), 50)
        # self.label_wid.text = get_reply().capitalize()
        self.label_wid.text = self.value

    def text_analizer(self, text):
        filename = files().open_file("Settings", "data.xml")
        self.INPUT_REQUIRED = XML().read(filename, "input_needed")

        if self.INPUT_REQUIRED == True:
            try:
                with open(files().open_file("Settings", 'data.pickle'), 'rb') as json_file:
                    self.FUNCTION_NAME = pickle.load(json_file)

            except Exception as e:
                print(f"ERROR_READING_DATA! REASON:{e}")

            # Get the function name where input is required
            function_name = self.FUNCTION_NAME

            Connector().send_input_text_to_function(
                text.lower(), function_name, MIDDLE_INPUT=text.lower())
        else:
            Connector().send_input_text_to_function(text.lower(), Say)


class SettingsMenu(Screen, Image, CoverBehavior):

    def __get_btn_name(self, btn):
        if btn == "tts":
            return "talk"

        if btn == "voice":
            return "voice"

        if btn == "network":
            return "online"

    def change_btn_state(self, btn):
        try:
            with open(settings_file, 'r') as file:
                self.settings = json.loads(file.read())
        except:
            msg = log().error("Couldn't open settings file", "SettingsMenu", "EllieUI")
            print(msg)

        tag = self.__get_btn_name(btn)
        self.settings[tag] = not self.settings[tag]
        try:
            with open(settings_file, 'w') as file:
                file.writelines(json.dumps(self.settings, indent=4))
        except Exception as e:
            # msg = log().error("Couldn't save settings file (userSettings.json)", "change_btn_state", "SettingsMenu", "EllieUI")
            print(e)

    def get_btn_state(self, btn_name, returnMenthod):
        try:
            with open(settings_file, 'r') as file:
                settings = json.loads(file.read())
        except:
            msg = log().error("Couldn't open settings file", "SettingsMenu", "EllieUI")
            return msg

        btn = self.__get_btn_name(btn_name)

        if returnMenthod == ">text<":
            text = " Offline Mode" if settings[btn] else " Online Mode"
            return text

        if returnMenthod == "text" and btn == "online":
            text = "Online" if settings[btn] else "Offline"
            return text
        elif (returnMenthod == "text") and (not btn == "online"):
            text = "Turn off" if settings[btn] else "Turn On"
            return text

        if returnMenthod == "btn_state":
            state = "down" if settings[btn] else "normal"
            return state


class FaQ(Screen):
    def get_document(self):
        msg = '''\n[size=40]Welcome[/size]
        \nAll frequent asked [b]questions[b] are given here:
        \n
        \n    **Question**: Some question
        \n    **Answer**: Answer for that question
        \n
        \n    **Question**: Some question
        \n    **Answer**: Answer for that question
        \n
        \n    **Question**: Some question
        \n    **Answer**: Answer for that question
        \n
        '''

        return msg



screen_manager = ScreenManager(transition=SlideTransition())
screen_manager.add_widget(MainMenu(name="main_menu"))
screen_manager.add_widget(SettingsMenu(name="settings_menu"))
screen_manager.add_widget(FaQ(name="faq_menu"))


class EllieApp(App):
    def build(self):
        checkValidity()
        return screen_manager


if __name__ == "__main__":
    # p4 = multiprocessing.Process(target=EllieApp().run)
    EllieApp().run()
#     # p4.start()5
# print(kivy/?)
