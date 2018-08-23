#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
def fib(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


# 输出了第10个斐波那契数列
print(fib(10))

a = [1, 2, 3]
b = a[:]
print(b)
time.sleep(1)

myD = {'item1':1,'item2':2}
for key,value in dict.items(myD):
    print(key,value)
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))


