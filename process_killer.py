# this scrip will find the process ID and kill the process of a given process name

import os
import time
import sys

processName = sys.argv[1]
command = "ps -e | grep " + processName + " | awk ' {print $1} '"
totalLoops = 0

# this function will find all those processes associated with the given name in command argument
def findProcess():
    # os.popen(cmd).read() will save the output of the command to a variable in python
    processes = os.popen(command).read()

    #print(processes)
    list = makeList(processes)
    return list


# this function will make a list of all those found process ids
def makeList(myString):
    list = myString.split('\n')
    list.pop()
    return list


# this function will kill all the process in a loop
def killProcess():
    global totalLoops

    exitAfter()
    getMessage()
    list = findProcess()
    printTheList(list)
    for i in range(len(list)):
        os.system('sudo kill %s' % (str(list[i])))

    totalLoops += 1
    checkToKillProcesses()


def printTheList(list):
    for i in range(len(list)):
        print(list[i])


def checkToKillProcesses():
    tmpList = findProcess()

    if(len(tmpList) != 0):
        time.sleep(5)
        killProcess()
    else:
        #all processes are killed and exiting...
        print('** The script killed the process in ' + str(totalLoops) + " loops.")
        exitAfter()


def getMessage():
    if(totalLoops < 1):
        print('List of processes to be killed')
    else:
        print('Still working to kill the following processes')


def exitAfter():
    if(totalLoops > 9):
        print('*** The scripted tried ' + str(totalLoops) + ' loops in total.')
        sys.exit()


def main():
    killProcess()


main()