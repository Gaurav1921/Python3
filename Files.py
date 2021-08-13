""" to open/read a file, the output will be handle = open(filename,mode) """
hand = open("mbox.txt", "r")    # filename will always be a string, mode is for opening the file to read/write
print(hand)

""" a special character for newline is \n represented in strings """
stuff = "Hello\nWorld!"
print(stuff)
print(len(stuff))      # one character length is reserved for a new line (it might seem two as \ & n)

""" file handle is treated as a sequence of lines, we can use 'for' statement to iterate through that sequence 
(ordered set) """
xfile = open('mbox.txt')
for cheese in xfile:
    print(cheese)

""" now to count the number of lines in a file """
fhand = open("Union")
count = 0
for i in fhand:
    count = count + 1
print("line count: ", count)

""" to reading it from a *whole* file """
fhand = open("mbox-short.txt")
inp = fhand.read()
print(len(inp))
print(inp[:20])

""" searching a line/word through a file """
fhand = open("mbox-short.txt")
for line in fhand:          # will be going through every line in the opened file
    line = line.rstrip()    # added this extra code because while printing adds one line + the file already has one line
    if line.startswith("From:"):
        print(line)

""" for doing the exact same thing as above we can do the below thing """
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From:"):   # will be skipping those lines and printing the lines starting with "From:"
        continue
    print(line)

""" for users trying to open the file names, they might be entering bad file names so to not have any error we will be
using try/except thing"""
fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:      # if the file can't be opened it will run the except code
    print("File can't be opened:", fname)
    quit()
count = 0    # if the file name can be opened it will continue from here
for line in fhand:
    if line.startswith("Subject:"):
        count = count + 1
    print("There were", count, "subject lines in", fname)
