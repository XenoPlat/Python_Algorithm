# 1. Пользователь вводит данные о количестве предприятий, их наименования и
# прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и
# вывести наименования предприятий, чья прибыль выше среднего и отдельно
# вывести наименования предприятий, чья прибыль ниже среднего.

companies = {}
n = int(input("Число предприятий: "))
s = 0
for i in range(n):
    name = input(str(i + 1) + "-е предприятие: ")
    income = 0
    for i in range(4):

        income += int(input("Прибыль за {}-й квартал: ".format(i + 1)))
    companies[name] = income
    s += income

avrg = s / n

print("Средния прибыль за год: {}. Предприятия, чья прибыль выше средней:".format(avrg))

for i in companies:
    if companies[i] > avrg:
        print(i)

print("Предприятия, чья прибыль ниже средней:".format(avrg))

for i in companies:
    if companies[i] < avrg:
        print(i)

# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры
# числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
# [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

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
