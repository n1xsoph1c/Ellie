import eel
import os
import pickle
import json
from misc import files
from Ellie import Say, get_reply
from connector import XML, Connector

CURRET_DIRECTORY = os.getcwd()
LIB_DIRECTORY = os.path.join(CURRET_DIRECTORY, "Lib")
WEB_DIRECTORY = os.path.join(LIB_DIRECTORY, "GUI")
SETTINGS_DIRECTORY = os.path.join(LIB_DIRECTORY, "Settings")

Settings_file = os.path.join(SETTINGS_DIRECTORY, "data.xml")
User_settings_file = os.path.join(SETTINGS_DIRECTORY, "userSetting.json")

with open(User_settings_file) as settings:
	SETTINGS = json.loads(settings.read())

eel.init(WEB_DIRECTORY)

def set_btn_states():
	Tts = SETTINGS['talk']
	OnlineMode = SETTINGS['online']
	OfflineMode = SETTINGS['offline']
	DiscordMode = SETTINGS['discord']

	eel.btn_switch(Tts, OnlineMode, OfflineMode, DiscordMode)

@eel.expose
def get_reply_from_ellie(msg):
	INPUT_REQUIRED = XML().read(Settings_file, "input_needed")

	if INPUT_REQUIRED:
		try:
			with open(files().open_file("Settings", "data.pickle"), "rb") as settings_file:
				FUNCTION = pickle.load(settings_file)
		except Exception:
			print("Error: ", Exception)

		Connector().send_input_text_to_function(msg.lower(), FUNCTION, MIDDLE_INPUT=msg.lower())
	else:
		Connector().send_input_text_to_function(msg.lower(), Say)
	return get_reply()

eel.start('index.html', size=(782, 622))    # Start
set_btn_states()