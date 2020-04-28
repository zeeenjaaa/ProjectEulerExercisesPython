"""Задача 3
Наибольший простой делитель
Простые делители числа 13195 - это 5, 7, 13 и 29.

Каков самый большой делитель числа 600851475143, являющийся простым числом?
"""

taskNumber = 600851475143
devider = taskNumber -1 
finish = False
print('task number is ', taskNumber)

def checkSimple (value):    
    count = 0
    i = value -1 
    while i > 2: 
        count += 1
        i -= 1        
        if value % i == 0 : 
            print('not simple, number', value, 'devided on',i)
            return False                       
        if count == value - 3:
            print('Biggest simple ', value)
            return True

'''if checkSimple(taskNumber) == True:
        finish = True'''

while not finish:    
    while taskNumber % devider != 0 and devider > 2 : 
        devider -= 1 
    if checkSimple(devider) != True and devider > 2:
        devider -= 1
    else: finish= True
            
