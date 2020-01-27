#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 20:05:08 2018

@author: Abhishek Kumar
"""

def fizzBuzz(r):
    for i in range(1,r):
        if(i%3==0 and i%5==0):
            print(str(i)+" = FizzBuzz")
        else:
            if(i%5==0):
                print(str(i)+" = Buzz")
            else:
                if(i%3==0):
                    print(str(i)+" = Fizz")
                else:
                    print(str(i))

fizzBuzz(51)