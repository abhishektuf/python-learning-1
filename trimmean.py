#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 08:31:28 2018

@author: Abhishek Kumar
"""

from statistics import mean
from scipy import stats

Survey=[10,20,30,25,35,20,40,90,100,110,112,31,45,72,85,91,103,156]
Survey.sort()
print("Mean", mean(Survey))
m = stats.trim_mean(Survey,0.1)
print("Trimmed Mean", m)