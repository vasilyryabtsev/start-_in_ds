"""

Original file is located at
    https://colab.research.google.com/drive/1l4MKCyS-nI2-4tdiTYJCTogGX-uNyOpW?usp=sharing#scrollTo=hNHNWPhngrUl

    
"""




import requests
import time
import re

from random import randint

BOOK_PATH = 'https://www.gutenberg.org/files/2638/2638-0.txt'

def benchmark(func):
    """
    Декоратор, выводящий время, которое заняло выполнение декорируемой функции
    """

    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f'Время выполнения функции {func.__name__}: {end - start}\n')
        return res
    return wrapper

def logging(func):
    """
    Декоратор, который выводит параметры с которыми была вызвана функция
    """

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(f'Функция вызвана с параметрами:\n{args}, {kwargs}\n')
        return res

    return wrapper

def counter(func):
    """
    Декоратор, считающий и выводящий количество вызовов декорируемой функции
    """

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        wrapper.count += 1
        print(f'Функция была вызвана: {wrapper.count} раз\n')
        return res
    wrapper.count = 0
    return wrapper

def memo(func):
    """
    Декоратор, запоминающий результаты исполнения функции func, чьи аргументы args должны быть хешируемыми
    """
    cache = {}

    def fmemo(*args):
        if args in cache:
            return cache[args]
        else:
            res = func(*args)
            cache[args] = res
            return res

    fmemo.cache = cache
    return fmemo