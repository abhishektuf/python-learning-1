#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 06:06:00 2018

@author: Abhishek Kumar
"""

items=["Eggs","Bread","Coffee","Sugar"]
for i in items:
    print(i)
length=len(items)
print(length)
items.reverse()
print(items)
items.append("Curd")
items.insert(0,"Meat")
print(items)
length=len(items)
print(length)

for i in range(len(items)):
    print(items[i])
items.sort()
print(items)
items.reverse()
print(items)
print(items[:2])