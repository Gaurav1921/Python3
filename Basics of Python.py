""" to install any module first go in command prompt and write 'pip install flask' and then come here and write
modules are built in codes which makes our work more easier and pip is package manager which pulls modules """
import flask

""" to print something the syntax for it is """
print("Hello World")

""" using python as calculator """
print(36 + 8)      # returns the addition
print(36 - 8)      # returns the subtraction
print(36 * 8)      # returns the multiplication
print(36 / 8)      # returns the division
print(36 // 8)     # returns the quotient
print(30 % 8)      # returns the remainder

""" comments for multi line """
# comments for single line

""" if we don't want to add another line while printing statement use end (by default its a new line character) """
print("Gaurav is the best", end=" ")         # python thinks that the space is the end of the line & starts printing new line from there
print("Do like and subscribe the channel")

""" escape sequence character """    # for more go to Quackit.com escape char
print("Gaurav\nSingh")         # new line character
print("Gaurav\"Singh\"")       # when extra "" used
print("Gaurav\tSingh")         # extra space character

""" assigning values to a variable """
var1 = "Hello World"
var2 = 4                # we can add two integers or two strings but not strings and int
var3 = 3.4

""" to know the type of variable"""
print(type(var2))
print(type(var1))
print(type(var3))

""" doing typecast """
a = int("54")            # originally 54 and 73.3 were strings but now typecasted to integers and float
b = float("73.3")
print(a+b)

""" we can  multiply string with int """
print("Gaurav"*5)




