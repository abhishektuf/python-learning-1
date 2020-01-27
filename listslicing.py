#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 11:44:02 2018

@author: Abhishek Kumar
"""

numbers=[]

for i in range(1,51):
    numbers.append(i)

a, b = input().split()
a=int(a)
b=int(b)

numbers=numbers[a:b]

for i in range(len(numbers)):
    print(numbers[i])

