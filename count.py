#Program to count number of word 'am' in a file

file = open("am.txt", "r")

data = file.read()

data = data.split()

count = 0

for i in data:
    if i == "am":
        count += 1
