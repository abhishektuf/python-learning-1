def factorial(n):
    '''
    product=1
    
    Iterative version>
    
    for i in range(1,n+1):
        product=product*i
    return product
    '''
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

n=int(input('Enter the number : '))
if(n<0):
    print('Factorial is not defined for negative numbers')
else:
    f=factorial(n)
    print('Factorial of',n,'is',f)
