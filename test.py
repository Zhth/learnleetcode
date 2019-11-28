import random
import os
import time

N = 4
playPerson = 2

def getNums():
    nums = []
    for _ in range(N):
        t = str(random.randint(0, 9))
        while t in nums:
            t = str(random.randint(0, 9))
        nums.append(t)
    return nums


def play(nums):
    contStep = 0
    flag = True
    while flag:
        contStep += 1
        temp = list(input('Please gauss the number (0000 ~ 9999):'))
        contA, contB = 0, 0
        for ind in range(N):
            if temp[ind] == nums[ind]:
                contA += 1
            elif temp[ind] in nums:
                contB += 1
        print('Your anser :' + str(contA) + 'A' + str(contB) + 'B')
        if contA == 4:
            print('You win!')
            print('You use ' + str(contStep) + ' steps.')
            flag = False
        else:
            print('Try again!')
    return contStep


def writeScore(filename, numOfperson, score, playtime):
    numOfperson += 1
    with open(filename, 'a+') as f:
        f.write('the score of Person '+str(numOfperson)+' is : '+str(score)+'\n')
        f.write('the time of Person '+str(numOfperson)+' is : '+str(playtime)+'\n')
    return


def clearFile(filename):
    with open(filename, 'w'):
        pass


nums = getNums()
filename = 'score.txt'
clearFile(filename)
for num in range(playPerson):
    starttime = time.time()
    score = play(nums)
    endtime = time.time()
    playtime = str(endtime - starttime)
    writeScore(filename, num, score, playtime)
    input('Please put enter before next person play.')
    os.system('cls')