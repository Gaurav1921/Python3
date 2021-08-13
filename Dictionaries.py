""" dictionary is more of a mess unlike lists it is bag of values which don't stay in order and along with that in
dictionaries we also have to label when we add any value """
purse = dict()
purse["money"] = 12     # here money is the label and 12 is the value of that label
purse["candy"] = 3
purse["tissue"] = 75
print(purse)            # in dictionaries values are stored inside the curly brackets (in lists we used square brackets)
print(purse["candy"])   # in dictionaries the index is the label while in lists it was the position as 0,1,...
purse["candy"] = purse["candy"] + 2
print(purse)
purse["candy"] = 8      # dictionaries are mutable like lists
print(purse)

""" here we see how many times that name has been shown on the screen/list """
counts = dict()
names = ["csev", "cwen", "csev", "zqian", "cwen"]
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1        # 'count[name]' = value of that variable
print(counts)

""" used to check whether the key is present or not """
names = ["csev", "cwen", "csev", "zqian", "cwen"]
if 'zqian' in counts:
    x = counts['zqian']
else:
    x = 0
z = counts.get('zqian', 0)     # go in the counts dictionary lookup for the key name with the default value set to 0
print(z)

""" to get to do the above problem in a easier way we do use get function """
counts = dict()
names = ["csev", "cwen", "csev", "zqian", "cwen"]    # in a file we can use split to create a list automatically
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

""" counting pattern """
counts = dict()
line = input("Enter some line:")
words = line.split()
print("Words: ", words)
for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)

""" for loop in dictionaries """
counts = {"chuck": 1, "fred": 42, "jan": 100}
for key in counts:
    print(key, counts[key])

""" Retrieving lists of keys and values with in-built functions """
jjj = {"chuck": 1, "fred": 42, "jan": 100}
print(list(jjj))
print(jjj.keys())
print(jjj.values())
print(jjj.items())      # gives us both keys and values in from of tuples '()'

""" to print the keys and values without the inbuilt function we use two iteration variables """
jjj = {"chuck": 1, "fred": 42, "jan": 100}
for aa, bb in jjj.items():
    print(aa, bb)


