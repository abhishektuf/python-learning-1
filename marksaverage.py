#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 11:31:46 2018

@author: Abhishek Kumar
"""
from statistics import mean
marks = []
for i in range(5):
    s=input()
    s=int(s)
    marks.append(s)

s2=mean(marks)
print(float(s2))
