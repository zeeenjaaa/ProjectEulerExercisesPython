'''Задача 4
Наибольшее произведение-палиндром
Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.

Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.'''

listAnswers = []

def checkLength(chkString):
    if len(chkString) % 2 == 0 :       
        return True
    else:         
        return False
def makeTwoStr(TaskNumber):
    mainStr = str(TaskNumber)
    middle = int(len(mainStr)/2)
    firstStr = mainStr[0:middle]
    secondStr = mainStr[middle:middle*2]
    secondStr = secondStr[::-1]
    if firstStr == secondStr:
        return True
    else:
        return False
def checkTestNumber(testNumber):
    if checkLength(str(testNumber)) == False:
        return False
    else: 
        if makeTwoStr(testNumber) == True:
            return True
        else:
            return False
def findingTask():    
    for i in range(100 , 999) :
        for k in range(100, 999):
            testNumber = i * k
            if checkTestNumber(testNumber) == True:
                listAnswers.append(testNumber)
    listAnswers.sort()
    listAnswers.reverse()
    print('answer is - ',listAnswers[0])
                
findingTask()
