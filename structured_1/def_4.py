# -*- coding: utf-8 -*-

def fib(n):    # вывести числа Фибоначчи меньшие (вплоть до) n
    """Выводит ряд Фибоначчи, ограниченный n."""
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a+b

    # Теперь вызовем определенную нами функцию:
fib(2000)

