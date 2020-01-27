'''
@author: Abhishek Kumar

'''
from turtle import *
turtle.bgcolor("black")
seurat=turtle.Turtle()
from random import randint

width=5
height=7
dot_distance=25

seurat.penup()
list_color=["white","yellow","brown","red","blue","green","orange","pink","violet","grey","cyan"]
seurat.setpos(-250,250)


def spiralPrint(m,n):
    k=0
    l=0
    f=0
    col=randint(0,10)
    seurat.color(list_color[col])

    while(k<m and l<n):

        if(f==1):
            seurat.right(90)

        for i in range(l,n):
            seurat.dot()
            seurat.forward(dot_distance)
            #print(a[k][i],end=" ")
        k+=1
        f=1

        seurat.right(90)
        col=randint(0,10)
        seurat.color(list_color[col])


        for i in range(k,m):
            seurat.dot()
            seurat.forward(dot_distance)
            #print(a[i][n-1],end=" ")
        n-=1
        seurat.right(90)
        col=randint(0,10)
        seurat.color(list_color[col])

        if(k<m):
            for i in range(n-1,l-1,-1):
                seurat.dot()
                seurat.forward(dot_distance)
                #print(a[m-1][i],end=" ")
            m-=1
        seurat.right(90)
        col=randint(0,10)
        seurat.color(list_color[col])

        if(l<n):
            for i in range(m-1,k-1,-1):
                seurat.dot()
                seurat.forward(dot_distance)

                #print(a[i][l],end=" ")
            l+=1
            

spiralPrint(20,20)
turtle.done()

'''
a=[]
count=1
for i in range(5):
    l=[]
    for j in range(5):
        l.append(count)
        count+=1
    a.append(l)

spiral(5,5,a)
'''

