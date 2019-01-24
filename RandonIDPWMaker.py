#   RIDPWM(Random String Maker) made by Joseph Kim
import sys
alpha_num = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
special = '!@#$%^&*()'


def manualMode():
    print('----------Select----------')
    print('1. Standard Output')
    print('2. File Output')
    return

def fileMode():
    file = open()
    return

def outputMode():

    return


if (len(sys.argv) == 1) :
    manualMode()
elif(len(sys.argv) == 2) :
    outputMode()
elif(len(sys.argv) == 3) :
    fileMode()
else :
    print('****Unexpected****\n--help for manual')
    exit(0)