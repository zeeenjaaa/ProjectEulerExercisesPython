'''Наименьшее кратное
2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.

Какое самое маленькое число делится нацело на все числа от 1 до 20?'''

'''РЕШЕНИЕ ПЕРЕБОРОМ'''
import os
devidedBefore = 10

def checkNumber(i):
    count = 0 
    for k in range(1,devidedBefore+1):
        if i % k == 0:
            count +=1            
            print('Devided on-', count)
        else:
            return False
    if count == devidedBefore:        
        return True
    else:         
        return False 
def makeNumbers():
    good = False
    number = 0
    while not good:
        number += 1
        os.system('cls')
        print('testing number-', number)        
        if checkNumber(number) == True:
            good = True
            print('number is-', number)

makeNumbers()