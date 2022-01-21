import datetime
from random import randint


def timer(func):
    def f(*args, **kwargs):
        start = datetime.datetime.now()
        func(*args, **kwargs)
        print((start - datetime.datetime.now()).microseconds)
    return f


def bubble(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                buff = array[j]
                array[j] = array[j + 1]
                array[j + 1] = buff
    return array


bubble_timer = timer(bubble)
N = 10000
n = 10
a = []
b = []
for i in range(N):
    a.append(randint(1, 999999))

for i in range(n):
    b.append(randint(1, 9999))


print(b)
print(a)
print(bubble(b))
print(bubble(a))
bubble_timer(b)
bubble_timer(a)
