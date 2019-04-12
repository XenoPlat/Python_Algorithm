# 1. В диапазоне натуральных чисел от 2 до 100 определить, сколько из них кратны
# каждому из чисел в диапазоне от 2 до 9

a = [0]*9
for i in range(2,100):
    for j in range(2,10):
        if i%j == 0:
            a[j-2] += 1
i = 0
while i < len(a):
    print(i+2, ' - ', a[i])
    i += 1

# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
# надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация
# начинается с нуля), т.к. именно в этих позициях первого массива стоят четные
# числа

import random
n = 10
arr = [0]*n
even = []
for i in range(n):
    arr[i] = random.randint(1, 100)
    if arr[i] % 2 == 0:
        even.append(i)
print(arr)
print('Четные элементы: ', even)

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный
# элементы

print('исходный массив')
import random
n = 10
arr = [0]*n
for i in range(n):
    arr[i] = random.randint(1,100)
    print(arr[i],end=' ')
print()

mn = min(arr)
mx = max(arr)

imn = arr.index(mn)
imx = arr.index(mx)
mn = min(arr)
mx = max(arr)
imn = arr.index(mn)
imx = arr.index(mx)

print('позиция и величина мин. элеиента[',imn+1,']=',mn,'позиция и величина max элеиента [',imx+1,']=',mx)
arr[imn],arr[imx] = arr[imx],arr[imn]

print('стало')
for i in range(n):
    print(arr[i],end=' ')
print()

# 4. Определить, какое число в массиве встречается чаще всего

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

# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его
# значение и позицию в массиве.

import random
n = 20
arr = []
for i in range(n):
        arr.append(random.randint(-50,50))
print(arr)
 
i = 0
index = -1
while i < n:
        if arr[i] < 0 and index == -1:
                index = i
        elif arr[i] < 0 and arr[i] > arr[index]:
                index = i
        i += 1
 
print('№ элемента',index+1,'значение:',arr[index])
 
# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным
# и максимальным элементами. Сами минимальный и максимальный элементы в сумму
# не включать

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

# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и
# различаться

import random
n = 20
a = []
for i in range(n):
    a.append(random.randint(1,100))
    print("%3d" % a[i], end='')
print()
 
if a[0] > a[1]:
    min1 = 0
    min2 = 1
else:
    min1 = 1
    min2 = 0
    
for i in range(2,n):
    if a[i] < a[min1]:
        b = min1
        min1 = i
        if a[b] < a[min2]:
            min2 = b
    elif a[i] < a[min2]:
        min2 = i
        
print(min1+1,':',a[min1])
print(min2+1,':',a[min2])

# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и
# записывать ее в последнюю ячейку строки. В конце следует вывести полученную
# матрицу

n = 5
m = 4
a = []
for i in range(m):
    b = []
    c = 0
    print('заполнить строку')
    for j in range(n-1):
        d = int(input())
        c += d
        b.append(d)
    b.append(c)
    a.append(b)
 
for i in a:
    print(i)

# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы

import random
M = 10
N = 5
a = []
for i in range(N):
    b = []
    for j in range(M):
        n = random.randint(1,100)
        b.append(n)
        print('%4d' % n,end='')
    a.append(b)
    print()
 
mx = -1
for j in range(M):
    mn = 200
    for i in range(N):
        if a[i][j] < mn:
            mn = a[i][j]
    if mn > mx:
        mx = mn
print("Максимальный среди минимальных: ", mx)

 



