import datetime
from time import sleep
import os
from itertools import islice
from misc import files, log


def Write(folderName, fileName, text, openType):
    '''Writes some text to a file on a folder'''
    files().write_on_file(folderName, fileName, text, openType)


def Open(folderName, fileName):
    '''Opens a specific file from a different directory'''
    file = files().open_file(folderName, fileName)
    return file

# old_txt = list()
# new_text = list()


today = str()
time = str()
hour = str()
text = str()

dN = int()
hN = int()

isDateThere = False
isHourThere = False


def add_on_history(folderName, fileName, text):
    global isDateThere, isHourThere, today, time, hour

    old_txt = [line.strip() for line in open(Open(folderName, fileName), "r")]
    file = open(Open(folderName, fileName), 'r')
    new_text = [line.strip() for line in file]

    today = str(datetime.date.today())
    now = datetime.datetime.now()
    time = str(now.strftime('%H:%M'))
    hour = str(now.strftime('%H'))

    if (isDateThere == False) and (isHourThere == False):
        print(log().info("Setting up memory", "add_on_history", "writeHistory"))
        sleep(0.5)  # 500ms
        isDateThere = False
        isHourThere = False
        print(log().info("Memory is \33[32mReady\33[0m", "add_on_history", "writeHistory"))

    check_date(folderName, fileName, old_txt)
    check_hour(folderName, fileName, old_txt)
    write_history(folderName, fileName, text, new_text)


def check_date(folderName, fileName, old_txt):
    global isDateThere

    for dN, i in enumerate(old_txt):
        if str(today) in i:
            # print(f'<{today}> is already there\n')
            # print(dN)
            dN = dN

            if isDateThere == False:
                isDateThere = True

            break
    else:
        Write(folderName, fileName, f'\n\n<{today}>\n', 'a+')
        # print(f'Added <{today}>\n')

        if isDateThere == True:
            isDateThere = False

    # break


def check_hour(folderName, fileName, old_txt):
    global isHourThere

    for hN, i in enumerate(old_txt):
        if str(hour) in i:
            # print(f'[{hour}] is already there\n')
            print(hN)
            hN = hN

            if isHourThere == False:
                isHourThere = True
            break
    else:
        Write(folderName, fileName, f'\n\t[{hour}]', 'a+')
        # print(f'Added [{hour}]\n')
        if isHourThere == True:
            isHourThere = False


def write_history(folderName, fileName, text, new_text):

    if (isDateThere == True) and (isHourThere == True):
        for j in islice(new_text, hN + 1, len(new_text)):
            if str(time) in j:
                n = datetime.datetime.now()
                Write(folderName, fileName, f'\t\t\t{text}\n', 'a+')
                break
        else:
            Write(folderName, fileName,
                  f'\n\t\t[{time}]\n\t\t\t{text}\n', 'a+')
    else:
        print(log().error("Memory Error", "write_history", "WriteHistory"))
        sleep(.8)  # 800 miliseconds
        print(log().warning("Fixing Memory Error", "write_history", "WriteHistory"))
