# 1. Подсчитать, сколько было выделено памяти под переменные в ранее
# разработанных программах в рамках первых трех уроков. Проанализировать
# результат и определить программы с наиболее эффективным использованием памяти.

# ******************************************************************************

# Windows 10 64-bit,  Python 3.7

# ******************************************************************************

import sys

# Задача 4 к уроку 3: определить, какое число в массиве встречается чаще всего

# Исходный код:

import random
n = 20
arr = [0] * n
for i in range(n):
    arr[i] = random.randint(1,100)
print(arr)
 
num = arr[0]
max_frq = 1
for i in range(n-1):
    frq = 1
    for j in range(i+1,n):
        if arr[i] == arr[j]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = arr[i]
 
if max_frq > 1:
    print(max_frq, 'раз(-а) встречается число', num)
else:
    print('ни одно число не повторяется')

# определяем объем памяти для переменной num

print(sys.getsizeof(num))

# результат одной из итераций:

# [18, 62, 44, 99, 81, 6, 9, 95, 16, 26, 89, 12, 47, 25, 43, 50, 6, 43, 61, 15]
# 2 раз(-а) встречается число 6
# 14

# num (или число 6) заняла 14 b памяти

# *****************************************************************************

# Задача 6 к уроку 3: в одномерном массиве найти сумму элементов, находящихся между минимальным
# и максимальным элементами. Сами минимальный и максимальный элементы в сумму
# не включать

# Исходный код:

print('массив:')
import random
import math
n = 20
a = [0]*n
for i in range(n):
    a[i] = random.randint(1,100)
    print('%3d' % a[i], end='')
print()

mn = 0
mx = 0
for i in range(1,n):
    if a[i] < a[mn]:
        mn = i 
    elif a[i] > a[mx]:
        mx = i
print('мин.=',a[mn],'max=',a[mx])

if mn > mx:
    mn, mx = mx, mn

summa = 0
for i in range(mn, mx):
    summa += a[i]
print('сумма между ними:',summa)

# определяем объем памяти для переменной summa

print(sys.getsizeof(summa))

# результат одной из итераций:

# массив:
# 70 77 34 98 29 51 69 44 24 23 79  6 38 53 19 36 84 92 28 48
# мин.= 6 max= 98
# сумма между ними: 417
# 14

# summa (или число 417) заняла 14 b памяти

# *****************************************************************************

# Задача 2 к уроку 5: написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры
# числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
# [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

# Исходный код:

from collections import deque

a = deque(input('1-е число: '))
b = deque(input('2-е число: '))

def sum_deq(a, b):
    deq = deque('0123456789abcdef')
    summ = deque()
    if len(a) < len(b):
        n = len(b)
        for i in range(len(a), n):
            a.extendleft('0')
    else:
        n = len(a)
        for i in range(len(b), n):
            b.extendleft('0')
    a.reverse()
    b.reverse()
    noise = 0
    for i in range(n):
        elem = deq.index(a[i]) + deq.index(b[i]) + noise
        if elem <= 15:
            summ.extendleft(deq[elem])
            noise = 0
        else:
            summ.extendleft(deq[elem % 16])
            noise = elem // 16
    if noise > 0:
        summ.extendleft(deq[noise])
    a.reverse()
    b.reverse()
    return summ

print(sum_deq(a, b))

deq = deque('0123456789abcdef')
mult = deque()
noise_mult = deque()
noise = 0

if len(a) < len(b):
    n = len(b)
    for i in range(len(a), n):
        a.extendleft('0')
else:
    n = len(a)
    for i in range(len(b), n):
        b.extendleft('0')
a.reverse()
b.reverse()
for i in range(n):
    for j in range(n):
        elem = deq.index(a[j]) * deq.index(b[i]) + noise
        if elem <= 15:
            noise_mult.extendleft(deq[elem])
            noise = 0
        else:
            noise_mult.extendleft(deq[elem % 16])
            noise = elem // 16
    if noise > 0:
        noise_mult.extendleft(deq[noise])

    mult = sum_deq(mult, noise_mult)
    noise_mult.clear()
    noise_mult.extendleft(['0'] * (i + 1))
    noise = 0

print(mult)

# определяем объем памяти для переменных mult и '1-е число'

print(sys.getsizeof(mult),'', sys.getsizeof(a))

# результат:

# 1-е число: a2
# 2-е число: 4cf
# deque(['5', '7', '1'])
# deque(['3', '0', 'a', 'f', 'e'])
# 320 320

# mult (произведение чисел) и '1-е число' заняли 320 b памяти каждая

# первые 2 программы эффективнее используют память
