#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 08:57:21 2018

@author: Abhishek Kumar
"""

with open("file.txt","r+") as abhifile:
    print(abhifile.read())
    abhifile.write("Abhishek Kumar")
abhifile.close()