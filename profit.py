# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 08:47:55 2018

@author: conta
"""

costprice=input()
costprice=int(costprice)
sellprice=input()
sellprice=int(sellprice)
if(costprice<sellprice):
    print("Profit")
if(costprice==sellprice):
    print("Neither")
if(costprice>sellprice):
    print("Loss")