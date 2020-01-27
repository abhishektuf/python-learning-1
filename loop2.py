a=["Abhay","Shiv","Amit","Vaibhav","Shivan","Paramjeet","Rahul","Abhishek"]
winner='Paramjeet'
'''
i=0
while i<len(a):
    if a[i]==winner:
        print(winner,"is the winner")
        break
    i+=1
else:
    print("No winner")

if winner in a:
    print(winner,"found in the team")
else:
    print(winner,"not found in our team")
'''
'''
try:
    print(a.index(winner))
except ValueError:
    print(winner, "not found in team.")
'''
print(a)
while True:
    if not a:
        break
    print(a.pop(-1))
print(a)