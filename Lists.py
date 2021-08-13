"""Algo - a set of rules or steps used to solve a problem.
DS - a particular way of organizing data in a computer - lists, dictionaries, tuples. """

""" list is a collection of many values in a single variable """
friends = [1, 24, "strings", [5, 6], 76]   # surrounded by square brackets, can have an empty list too, list inside list
print(friends)

""" using 'for' loop for lists """
for i in [5, 4, 3, 2, 1]:
    print(i)
print("Blastoff!")

""" extracting a particular element of lists inside it """
friends = ["joseph", "glenn", "sally"]       # the first value starts from 0
print(friends[1])

""" lists are mutable i.e. it can be changed whereas strings are not """
lotto = [2, 14, 26, 41, 63]
print(lotto)      # if we would have done the same with strings it would give an error as strings are not mutable
lotto[2] = 28
print(lotto)      # it gives an update value of lotto with 2nd value of the variable as 28

""" to check the length of a list we use len function """
x = [1, 2, "joe", 99]
print(len(x))

""" using the range function on lists """
friends = ["joseph", "glenn", "sally"]
print(range(len(friends)))

""" a tale of two loops """
friends = ["joseph", "glenn", "sally"]
for friend in friends:
    print("Happy New Year:", friend)
# or this way also:
for i in range(len(friends)):
    friend = friends[i]
    print("Happy New Year:", friend)

""" concatenating lists using '+' """
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

""" lists can be sliced using ':' """
t = [9, 41, 12, 3, 74]       # just like string the second no is up to but not including
print(t[1:3])
print(t[:])

""" to get the number of operations which can be done on the list do the below """
x = list()
print(dir(x))

""" using append function to add the elements inside the list while keeping the initial list as empty """
stuff = list()
stuff.append("book")
stuff.append(99)
print(stuff)

""" to check if something is in the list using 'bool' function"""
some = [1, 9, 21, 10, 16]
print(bool(1 in some))
print(bool(20 not in some))

""" lists comes out in the exact order as it has been written but it can be sorted as per our needs """
friends = ["joseph", "glenn", "sally"]
friends.sort()          # sorts them in alphabetical order
print(friends)

""" python does have some in-built functions """
num = [3, 41, 12, 9, 74]
print(len(num))
print(max(num))
print(sum(num))

""" # using data structures to calculate average
num_list = list()               # created an empty list
while True:
    inp = input("Enter a number: ")
    if inp == "done":           # breaks the loop when the user inputs 'done'
        break
    value = float(inp)           # converting the inp into float here as done can't be converted into float
    num_list.append(value)       # for user to inout values: inp-->value
average = sum(num_list) / len(num_list)
print("Average: ", average) """

""" splitting the strings into parts """
abc = "With three words"
stuff = abc.split()    # it splits the strings and gives us individual words
print(stuff)
print(len(stuff))      # if there is no space between two words in a string, the list would recognize it as one word
print(stuff[1])
for w in stuff:        # but if we specify what delimiter char we want to split by using 'split(";")' then it recognizes
    print(w)

""" to exactly extract the word from a string using double split pattern """
line = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"       # we want to extract 'uct.ac.za' from string
words = line.split()
email = words[1]
pieces = email.split("@")
required = pieces[1]
print(required)





