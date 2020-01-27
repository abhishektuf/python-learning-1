

def linear_search(n,x):
    element=[1]
    for i in range(1,1001):
        element.append(i)
    count=0
    flag=0

    for i in element:
        count+=1
        if(i==x):
            print("Yes I found my number at position "+str(i))
            flag=1
            print(count)
    if(flag==0):
        print("Number not found")

#linear_search(1001,65)

def binary_search(a,x):
    first_pos=0
    last_pos=len(a)-1
    flag=0

    count=0

    while(first_pos<=last_pos and flag==0):
        count+=1
        mid_position=(first_pos+last_pos)//2
        if(x==a[mid_position]):
            flag=1
            print("The is present at position: "+str(mid_position+1))
            print("iterations: "+str(count))
            return
        else:
            if(x<a[mid_position]):
                last_pos=mid_position-1
            else:
                first_pos=mid_position+1
    print("The number is not present")

a=[]
for i in range(1,1000000):
    a.append(i)

binary_search(a,999999)
