#   RIDPWM(Random String Maker) made by Joseph Kim
import sys
import random
alpha_num = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
special = '!@#$%^&*()'

def getRandomString(charset, length) :
    randomString = ''
    for i in range(length):
        index = random.random() * int(len(charset) - 1)
        randomString = randomString + charset[int(index)]
    return randomString

def mainMenu():
    print('----------Select----------')
    print('1. Standard Output')
    print('2. File Output')
    print('#', end='')
    selection = int(input())
    if(selection == 1) :
        stdoutMode()
    return

def stdoutMode():
    print('Length(ID) :', end='')
    maxIndex_ID = int(input()) - 1
    print('Length(PW) :', end='')
    maxIndex_PW = int(input()) - 1
    randomID = getRandomString(alpha_num, maxIndex_ID).lower()
    randomPW = getRandomString(alpha_num + special + special + special + alpha_num, maxIndex_PW)
    print('Generated Random ID : ' + randomID)
    print('Generated Random PW : ' + randomPW)
    print('Regenerate(R) | Done(D) : ', end='')
    if(input().upper() == 'R') :
        stdoutMode()
        return
    elif(input().lower() == 'D') :
        sys.stdout.flush()
        exit(0)
    return



    exit(0)