"""Задача 2
Четные числа Фибоначчи
Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих.
Начиная с 1 и 2, первые 10 элементов будут:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
"""
current = 0
previous = 2 
beforePrevious = 1
sumFibonaci = 2
orderFibonaci = 2
state = ''
while current < 4000000 :
    current = beforePrevious + previous
    beforePrevious = previous
    previous = current
    orderFibonaci = orderFibonaci + 1
    
    if current%2 == 0 : 
        state = 'even number' 
        sumFibonaci = sumFibonaci + current
    else:
        state = 'odd number'         
    print(orderFibonaci,'. ', current,' ', state)
print('Sum of even number is ', sumFibonaci)