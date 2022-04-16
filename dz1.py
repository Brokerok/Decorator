import datetime


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
