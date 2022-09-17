#Program to remove lines begining with a from one file and copy them to another

file = open("file.txt", "r")

data = file.readlines()

file = open("file.txt", "w")

dest = open("dest.txt", "w")

for i in data:
    if i[0] == "A" or i[0] == "a":
        dest.write(i)
    else:
        file.write(i)

print("Program executed")