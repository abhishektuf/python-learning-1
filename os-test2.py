import os
import shutil
import subprocess
from pprint import pprint

pwd = os.getcwd()
'''
ls = os.listdir()
print(pwd)
print(ls)

for item in ls:
    print(item)
'''
abp = os.path.abspath('os.py')
bname = os.path.basename(abp)
spath = os.path.split(os.getcwd())
epath = os.path.exists('c:\windows')


result = shutil.copyfile(abp, r'C:\Users\xtqj1432\Desktop\test.py')

print(result)

f = open('hello.txt','a+')
f.write("Hellow this is line added by Python program on this file.")
f.close()



'''
print(abp)
print(bname) 
print(spath)
print(epath)
'''