""" tuples are like lists with () as parenthesis whose values inside a variable can't be changed unlike lists, dict """
x = ("glenn", "sally", "joseph")
print(x[2])
print(x)
print(max(x))     # alphabetically s comes at the last
# x[2] = "gaurav"          # strings and tuples are not immutable

""" we can't sort, append, reverse a tuple """
t = tuple()
print(dir(t))

""" this way it's easier to work with tuples as it's not modifiable, and used when we want to make temporary variables """
(x, y) = (4, "fred")        # we can use two variables in tuples
print(y)

""" tuples as logical operators, it starts with comparing the 1st pair """
x = (0, 1, 2) < (5, 1, 2)
print(bool(x))

""" using sorted """
d = {"a": 10, "b": 1, "c": 22}
i = d.items()
t = sorted(d.items())
print(t)
for k, v in t:
    print(k, v)

""" to sort by values instead of key in tuples just replace k, v with v, k and then append in the list and then sort """
c = {"a": 10, "b": 1, "c": 22}
tmp = list()
for k, v in c.items():
    tmp.append((v, k))
print(tmp)
tmp = sorted(tmp, reverse=True)    # the 2nd iterator means we will be going reverse from upper to lower i.e decreasing
print(tmp)

""" # now the same problem of top 10 most common words using tuples 
romeo.txt = open("romeo.txt")
counts = dict()
for line in romeo.txt:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1       # till here common got thw histogram of words unsorted

lst = list()
for k, v in counts.items():
    lst.append(v, k)
    
lst = sorted(lst, reverse=True)
print(lst)

for v, k in lst[:10]:
    print(k, v) """








