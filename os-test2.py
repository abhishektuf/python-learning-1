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
abp = os.path.abspath('oslib1.py')
bname = os.path.basename(abp)
spath = os.path.split(os.getcwd())
epath = os.path.exists('c:\windows')

result = shutil.copyfile(abp, r'C:\Users\xtqj1432\Desktop\test.py')

print(result)

f = open('hello.txt', 'a+')
f.write("Hello this is line added by Python program on this file.")
f.close()

print(os.stat('oslib1.py'))
print(os.environ.get('HOME'))
print(os.path.dirname('c:\windows\win.ini'))
file_path = os.path.join(pwd, 'movies.py')
print(os.path.exists('c:\windows\win.ini'))
print(os.path.splitext('c:\windows\win.ini'))
print(file_path)


print(abp)
print(bname)
print(spath)
print(epath)
