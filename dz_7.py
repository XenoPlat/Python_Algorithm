# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы. Сортировка должна быть
# реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).

from random import randint

lst = [randint(-100, 100) for i in range(20)]
print(lst)

def bubble_sort(array):
    m = 0
    for j in range(len(array) - 1):
        for i in range(len(array) - j - 1):
            m += 1
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

    return array


bubble_sort(lst)
print(lst)

# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массив

lst = []

for i in range(50):
    lst.append(randint(0, 50))
print(lst)


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1

mergeSort(lst)
print(lst)

# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найти в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше ее.
# Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки,
# который не рассматривался на уроках.

from random import randint

m = int(input('Введите натуральное число:  '))
s = 2 * m + 1
array = [randint(0, 100) for i in range(s)]
print(f'Исходный массив\n {array}')
print()


def med(array):
    while len(array) > 1:
        array.remove(max(array))
        array.remove(min(array))
    return array[0]


print(f'Медиана равна {med(array)}')