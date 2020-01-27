#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 12:03:05 2018

@author: Abhishek Kumar
"""

numbers=[]
inp=input()
inp=int(inp)
count=0
for i in range(1,51):
    numbers.append(i)
numbers.sort()
for i in range(1,len(numbers)+1):
    if(i%inp==0 and i!=inp):
        count=count+1
print(count)
