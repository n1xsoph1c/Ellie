""" Holds some classes to open files and show some stats """
import os
import textwrap
import socket


class network:
    """ Network
    ===========
    Checks if the device is connected to the internet or not

    is_connected()
    -----------------------
    Returns True if connected to the internet else it returns False

    ```python
    >>>> print(network().is_connected())
    >>>> True #If connected to the internet
    >>>> False #else
    ```
    """
    def is_connected():
        try:
            # connect to the host -- tells us if the host is actually
            # reachable
            socket.create_connection(("www.google.com", 80))
            return True
        except OSError:
            pass
        return False


class log:
    """ 
    Log
    ====
    Logger for ellie with different color

    error(msg, loc):
    --------------------------
    Returns the msg in red color

    ```
    >>>> log().error("test", "log") 
    >>>> [Error | Log] test<- Red colored
    ```
    warning(msg, loc):
    --------------------------
    Returns the msg in orange color

    ```    
    >>>> log().error("test", "log") 
    >>>> [Warning | Log] test<- Red colored
    ```

    info(msg, loc):
    --------------------------
    Returns the msg in blue color
    
    ```
    >>>> log().error("test", "log") 
    >>>> [Info | Log] test <- Blue colored
    ```

    message(msg, loc):
    --------------------------
    Returns the msg in Green color

    ```
    >>>> log().error("test", "log") 
    >>>> [Message | Log] test<- Green colored
    ```
    """

    def __init__(self):
        self.__end = '\33[0m'
        self.__redAlt = '\33[41m'  # boxed
        self.__red = '\33[91m'
        self.__green = '\33[32m'
        self.__greenAlt = '\33[42m'  # boxed
        self.__orange = '\33[33m'
        self.__orangeAlt = '\33[43m'  # boxed
        self.__blue = '\33[36m'
        self.__blueAlt = '\33[46m'  # boxed

    def error(self, msg, *loc):
        return f"[{self.__red} ERROR | {loc}{self.__end} ] [ {msg} ]"

    def warning(self, msg, *loc):
        return f"[{self.__orange} WARNING | {loc}{self.__end} ] [ {msg} ]"

    def message(self, msg, *loc):
        return f"[{self.__green} MESSAGE | {loc}{self.__end} ] [ {msg} ]"

    def info(self, msg, *loc):
        return f"[{self.__blue} INFO | {loc}{self.__end} ] [ {msg} ]"


class files:
    ''' Opens or Writes on any files from Library folder (Lib) '''

    def write_on_file(self, folderName, fileName, text, openType):
        '''Writes some text to a file on a folder'''
        currentDir = os.getcwd()
        LibraryFiles = "Lib"

        file_to_Open = os.path.join(
            currentDir, LibraryFiles, folderName, fileName)
        f = open(file_to_Open, openType)
        f.writelines(text)
        f.close()

    def open_file(self, folderName, fileName):
        '''Opens a specific file from a different directory'''
        currentDir = os.getcwd()
        LibraryFiles = "Lib"

        # data_folder = os.path.join(d, folderName)
        file_to_Open = os.path.join(
            currentDir, LibraryFiles, folderName, fileName)
        return file_to_Open


class stats:
    def Updates(self):
        '''Gives the update stats\n
                Returns Elleis Update'''
        updates = [line for line in open(
            files().open_file('Settings', 'updates'))]
        test = ""

        for line in updates:
            test = test + line

        return test

    def Goals(self):
        '''Gets the goals from _GOALS_ files\n
        Prints goals from goals.ellie files'''

        goals = [line.strip() for line in open(
            files().open_file("Log", '_GOALS_'))]
        for lines in goals:
            print(lines)
