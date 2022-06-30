#Program to count total number of vowels in a text file

vowels = "aeiou"
count = 0

with open("text1.txt", "r") as file:
    for i in file.read():
        if i.lower() in vowels:
            count += 1


print("Number of vowels in the file:", count)
