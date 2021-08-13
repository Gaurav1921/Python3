fruit = "banana"

""" the counting for the string character starts from 0 by default. """
letter = fruit[1]
print(letter)

""" to print out the letter 3-1=2 (index value) of the word banana """
x = 3
print(fruit[x - 1])

"""prints the length of the word banana """
print(len(fruit))

""" using while loop to list out all the letters of the word banana """
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

""" using for loop for the same process which makes it easier to print """
for letter in fruit:
    print(letter)

""" to count how many a's are present in the word banana """
count = 0
for letter in fruit:  # here iteration variable : letter
    if letter == "a":
        count = count + 1
print(count)

""" slicing strings : print the exact no of letters we want from the word banana """
print(fruit[1:3])  # won't include the letter at the 3rd place (as per the numbering which starts from 0)
print(fruit[1:20])
print(fruit[:])  # when nothing specified it will assume the minimum and maximum value it can go

""" we can add two strings and we can convert int to str but not the other way round"""
a = "gaurav"
print(a + " " + "hello")
if "z" in fruit:
    print("Found")
else:
    print("Not Found")

"""" changing cases of strings into lowercase, uppercase, capitalize, left strip, right strip """
print(fruit.title())

""" to find the position of the letters in the word banana """
print(fruit.find("na"))
print(fruit.find("zz"))  # when the letter we are finding is not there it returns the value of -1

""" search and replace a particular word or a letter"""
print(fruit.replace("banana", "apple"))

""" to remove unnecessary whitespaces """
x = "    gaurav    "
print(x)
print(x.lstrip())
print(x.strip())

""" u can use startswith function and find function to state at which position it is at """
data = "stephen.marquard@gmail.com"
print(data.find("@"))
print(data.find("a", 10))  # will find the letter a after the 16th character of string data

















