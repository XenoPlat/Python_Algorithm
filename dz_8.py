# 1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
# состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.

S = str(input("Введите строку: "))

substr = set()

for i in range(len(S)):
    for j in range(len(S) - 1 if i == 0 else len(S), i, -1):
        substr.add(hash(S[i:j]))

print(f'Количество подстрок в данной строке: {len(substr)}')

# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.

import collections


class MyNode:

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def hoffman(string):
    count = collections.Counter(string)
    sort = collections.deque(sorted(count.items(), key=lambda item: item[1]))

    while len(sort) > 1:
        weight = sort[0][1] + sort[1][1]
        node = MyNode(left=sort.popleft()[0], right=sort.popleft()[0])

        for i, item in enumerate(sort):
            if weight > item[1]:
                continue
            else:
                sort.insert(i, (node, weight))
                break
        else:
            sort.append((node, weight))

    return sort[0][0]


def code_table(tree, path=''):
    if not isinstance(tree, MyNode):
        table[tree] = path
    else:
        code_table(tree.left, path=f'{path}0')
        code_table(tree.right, path=f'{path}1')


table = dict()
string = input('Введите 3 слова: ')
code_table(hoffman(string))

for i in string:
    print(table[i], end='')

print()
