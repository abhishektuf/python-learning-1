'''
def numbers(n): 
    for i in range(0, n):
        l = 1
        for j in range(0, i+1): 
            print(l, end=" ")
            l+=1
        print("")
n = int(input())
numbers(n)
'''

r=int(input())
for i in range(0,r):
    l=1
    for j in range(0,i+1):
        print(l,end="")
        l+=1
    if l==r:
        break
    else:
        print("")