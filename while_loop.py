count=0
while count<=5:
    print(count,"This is inside the while loop")
    count+=1
else:
    print(count,"This is outside the while loop")


word="python"
position=0
while position < len(word):
    print (word[position])
    position+=1


line=1
while line<=5:
    position=1
    while position<line:
        print (position)
        position+=1
    else:
        print (position)
    line+=1