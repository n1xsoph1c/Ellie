from fbchat import log, Client
from fbchat.models import *
# from Ellie import get_reply, Say, searchMusic
# from connector import XML, Connector
# from connector import Connector
# from misc import files

# import GLOBALS
import time
import pickle
import random
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
# INPUT_NEEDED = False
cookies = {}
# GLOBALS.initialize()

# GLOBALS.INPUT_NEEDED = False


class EllieBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):

        # self.INPUT_REQUIRED = XML().read(files().open_file(
        #     "Settings", "data.xml"), "input_needed")

        self.markAsDelivered(thread_id, message_object.uid)
        # self.markAsRead(thread_id)

        # If you're not the author, echo
        if author_id != self.uid:
            text = message_object.text
            # reply = "get_reply()"

            # if 'Ellie:' in reply:
            #     reply = reply.replace("Ellie:", "")

            # if self.INPUT_REQUIRED == True:
            #     try:
            #         with open(files().open_file("Settings", 'data.pickle'), 'rb') as json_file:
            #             self.FUNCTION_NAME = pickle.load(json_file)

            #     except Exception as e:
            #         print(f"ERROR_READING_DATA! REASON:{e}")

            #     # Get the function name where input is required
            #     function_name = self.FUNCTION_NAME
            #     print(
            #         f"INPUT NEEDED TO THE FUNCTION {function_name.__name__}\n")
            #     print(F"AND THE FUNCTION IS:{function_name}")

            #     # print(self.FUNCTION_DICT.get("searchMusic"))
            #     # data = json.loads(self.FUNCTION_DICT)

            #     Connector().send_input_text_to_function(
            #         text.lower(), function_name, MIDDLE_INPUT=text.lower())
            #     reply = get_reply()
            # else:
            #     print("NO INPUTS NEEDED TO ANY FUNCTION!\n")
            #     # print(f"INPUT NEEDED TO THE FUNCTION {function_name}\n")
            #     print(f"TYPE OF FUNCTION_DICT:{type(Say)}\n")
            #     print(F"AND THE FUNCTION IS:{Say}")
            #     Connector().send_input_text_to_function(text.lower(), Say)
            #     reply = get_reply()

            # print(f"GLOBAL TEXT: {reply}\n")
            self.send(Message(reply), thread_id=thread_id,
                      thread_type=thread_type)
            # GLOBALS.REPLY_ONLINE = False


client = EllieBot("mail", "pass",  user_agent=user_agent)
cookies = client.getSession()
client2 = fbchat.Client('email', 'password', user_agent=user_agent, session_cookies=cookies)
info = """Hey I am up for a new test!

Instruction on How to use me......

Start your chat by saying Hi or Hello And then continue
chatting

Always chat on proper Language! 
Dont use words like Hlw or plz or wbu
Its Hard for me to understand

If anything happens my Admin will be Monitoring me!

I dont have that much knowledge on sentences but hey
My Creator tought me some Interrogative sentences

Why are you running?
What is that?
How are you? (dont ask it yet got bugs)

I know I have some bugs but dont worry I will 
get imporved soon and everyday 

Things to TRY:
 - play a music
 - tell me a joke
"""

info2 = "Hey guys its time to go off... I will let you all know when I will be online again :D"

info3 = """https://cdn.discordapp.com/attachments/497627539770966036/738928274603901019/cabe783d42b5c8fb4eb8a37d54ea6cfc-1.gif"""

# Fetches a list of all users you're currently chatting with, as `User` objects
users = client.fetchAllUsers()

UID = [user.uid for user in users]
# NAMES = [user.name for user in users]
# UID = []



COUNT = 0

# print(UID)
# print(NAMES)

path_image = "/Users/elain/Desktop/EID.gif"

def send_to_all(message):
    for i in range(len(UID)):
        thread_id = UID[i]
        thread_type = ThreadType.USER
        # print(f"Sending message to {UID[i].name}")
        # client.send(Message(text=message), thread_id=thread_id,
        #             thread_type=thread_type)
        client.sendLocalImage(
            path_image,
            message=Message(text="Eid Mubarak :)"),
            thread_id=thread_id,
            thread_type=thread_type,
        )
        print(f"Message sent to {UID[i].name} | {i}/{len(UID)}")
        time.sleep(random.randint(0.8, 2))
    print("Done sending message to all the friends!")

def spam_MOYDA():
    thread_id = UID[1]
    thread_type = ThreadType.USER
    client.send(Message(text="ALRIGHT"), thread_id=thread_id,
                    thread_type=thread_type)
    client.send(Message(text="ITS TIME"), thread_id=thread_id,
                    thread_type=thread_type)
    client.send(Message(text="FOR REVENGE"), thread_id=thread_id,
                    thread_type=thread_type)
    client.send(Message(text='SPAM SHAKALAKA'), thread_id=thread_id,
                    thread_type=thread_type)

    # text = "FUCK U MOTHERSCOOTER"
    # j = range(199)

    # for i in range(100):
        
    #     client.send(Message(text=f'SPAM SHAKALAKA AND {text}'), thread_id=thread_id,
    #                 thread_type=thread_type)
    #     time.sleep(0.5)
        
# spam_MOYDA()
send_to_all(info3)
client2.listen()


# self.send(message_object, thread_id=thread_id, thread_type=thread_type)

# e = EchoBot("itsellietheai@gmail.com", "Hopeisasadthing!123")
# e.listen()
# print("users' names: {}".format([user.name for user in users]))


# If we have a user id, we can use `fetchUserInfo` to fetch a `User` object
# user = client.fetchUserInfo("<user id>")["<user id>"]
# # We can also query both mutiple users together, which returns list of `User` objects
# users = client.fetchUserInfo("<1st user id>", "<2nd user id>", "<3rd user id>")

# print("user's name: {}".format(user.name))
# print("users' names: {}".format([users[k].name for k in users]))


# `searchForUsers` searches for the user and gives us a list of the results,
# and then we just take the first one, aka. the most likely one:
# user = client.searchForUsers("<name of user>")[0]

# print("user ID: {}".format(user.uid))
# print("user's name: {}".format(user.name))
# print("user's photo: {}".format(user.photo))
# print("Is user client's friend: {}".format(user.is_friend))


# # Fetches a list of the 20 top threads you're currently chatting with
# threads = client.fetchThreadList()
# # Fetches the next 10 threads
# threads += client.fetchThreadList(offset=20, limit=10)

# print("Threads: {}".format(threads))


# # Gets the last 10 messages sent to the thread
# messages = client.fetchThreadMessages(thread_id="<thread id>", limit=10)
# # Since the message come in reversed order, reverse them
# messages.reverse()

# # Prints the content of all the messages
# for message in messages:
#     print(message.text)


# # If we have a thread id, we can use `fetchThreadInfo` to fetch a `Thread` object
# thread = client.fetchThreadInfo("<thread id>")["<thread id>"]
# print("thread's name: {}".format(thread.name))
# print("thread's type: {}".format(thread.type))


# # `searchForThreads` searches works like `searchForUsers`, but gives us a list of threads instead
# thread = client.searchForThreads("<name of thread>")[0]
# print("thread's name: {}".format(thread.name))
# print("thread's type: {}".format(thread.type))


# # Here should be an example of `getUnread`

# # client.listen()
