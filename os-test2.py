import oslib1
import shutil
import subprocess
from pprint import pprint

pwd = oslib1.getcwd()
'''
ls = os.listdir()
print(pwd)
print(ls)

for item in ls:
    print(item)
'''
abp = oslib1.path.abspath('oslib1.py')
bname = oslib1.path.basename(abp)
spath = oslib1.path.split(oslib1.getcwd())
epath = oslib1.path.exists('c:\windows')


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