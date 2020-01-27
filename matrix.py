"""
@author: descentis
http://sccilabs.org/amit_verma.html
"""

a,b=map(int,input().split())

count=1
m = []
for i in range(1,a+1):
    l = []
    for j in range(1,b+1):
        l.append(count)
        count+=1
    m.append(l)

for i in range(a):
    for j in range(b):
        if(j==b-1):
            print(m[i][j], end="")
        else:
            print(m[i][j], end=" ")
    if(i!=a-1):
        print()