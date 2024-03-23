# dictionary in python
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# ways to define a dictionary
dict1 = dict({1: 'Microsoft', 2: 'Google', 3:'Facebook'})
print(dict1)
dict2 = dict([(4,"Praneeth"),(2,"Verma")])
print(dict2)
dict3 = {"name":"John", "age":30}
print(dict3)
dict4 = {  
    "child1" : 
    {
    "name" : "Emil",
    "year" : 2004
    },
   "child2" : 
    {
    "name" : "Tobias",
    "year" : 2007
    },
    "child3" : 
    {
    "name" : "Linus",
    "year" : 2011
    }
  }
print(dict4["child1"]["name"])           # accessing items in nested dictionary

# accessing the values of dictionary
print(dict1[1])

# adding set of values with single key
dict1[5] = "alex","Smith"
print(dict1)

# updating existing key
dict1[2] = "Meta"
print(dict1)


# built-in functions of dict
'''The any() function returns True if at least one element in the iterable is True.
If the iterable is empty, any() returns False.

The all() function returns True if all elements in the iterable are True (or if the iterable is empty).
'''
dict5 = {1: "Ayan", 2: "Bunny", 3: "Ram", 4: "Bheem"}  
print(f"Length of dict5 is: {len(dict5)}")                # length of a dictionary

print(any({":"}))               # checks if any value is present or not, returns True/False
print(any({5}))                 # returns true

print(all({":",":",":"}))       # checks if all values are present or not, returns True/False

print(f"Sorted dictionary is: {sorted(dict5)}")             # sorts the dictionary based on keys

# built in methods of dictionary
mydict = {1: "Microsoft", 2: "Google", 3: "Facebook", 4: "Amazon", 5: "Flipkart"} 

# accessing items of dictionary
y = mydict.get(2)           # returns the specified value
print(y)  

x = mydict.keys()           # returns keys of the dict
print(x)

z = mydict.values()         # returns the value of dict
print(z)

mydict.items()              # returns all key-value pair of the dict
print(mydict)

# change items of dictionary
mydict.update({3:"Meta"})   # update the value of 3rd key
print(mydict)

# remove items from dictionary
x = mydict.pop(4)            # remove the 4th key of the dict
print(mydict)

mydict.popitem()             # remove the last key-value of the dict
print(mydict)

del mydict[1]                # deletes the 1st key and its associated value
print(mydict)
del dict3                   # deletes the dict completely
print(mydict)

mydict.clear()               # empties the dictionary
print(mydict)

# copies a dictionary 
'''You cannot copy a dictionary simply by typing dict2 = dict1, 
because: dict2 will only be a reference to dict1, 
and changes made in dict1 will automatically also be made in dict2.'''
# first way to make a ccopy of a dictionary
copy = dict1.copy()
print(copy)
# second way to make a copy of a dictionary
another_copy = dict(dict1)
print(another_copy)

# dictionary comprehension
squared_numbers = {x:x**2 for x in range(6)}
print(f"Sqaured numbers: {squared_numbers}")

# creating dictionary from keys and values in list
keys = ["a","b","c"]
values = [1,2,3]
new_dict = dict.fromkeys(keys,values)
print(f"List inside dictionary: {new_dict}")