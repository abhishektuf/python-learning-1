file=open("cloud.json")

str=file.readlines()
print(str)

file.close()


file2=open("data.json",'w')

file2.write("Writing using python program 1")

file2.close()
