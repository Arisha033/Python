# lists in python
# list in python are defined using square brackets[] and are mutable (memory reference can be changed)

# here the memory address of both the lists are same hence changes in list 1 reflects in list 2 also
l1 = [1,2,3]
l2 = l1
l1[0] = 88
print(f"This is l1: {l1} and this is l2: {l2}")

# here the memory address of both lists are same but then we modified list 2 now list 2 is pointing to a new location and changes in list 1 doesn't effect list 2
p1 = [4,5,6]
p2 = p1
p2 = [7,8,9]
p1[0] = 22
print(f"This is p1: {p1} and this is p2: {p2}")

# here we made a copy of list s1, if we change the list s1 list s2 remains the same
s1 = [11,43,56]
s2 = s1[:]
s1[0] = 99
print(f"This is s1: {s1} and this is s2: {s2}")

# replace items in list using slicing

tea_varities = ["Lemon", "Black", "Green", "Herbal"]
# tea_varities[1:2] = "Masala"         # it treats "Masala" as a list hence returns every character of "Masala" individually
# print(tea_varities)        
tea_varities[1:2] = ["Masala"]         # by using this syntax it considered it as one item not a list of items
print(tea_varities)
print(tea_varities[1:1])                # results empty list bcz last index is excluded

# tea_varities[1:1] = ["test", "test"]        # insert multiple values at first index
# print(tea_varities)
tea_varities[1:1] =  []                  # insert nothing means just remove the elements from that range
print(tea_varities)

list1 = [1,5,"isha","example",46.7]
list2 = [1,5,"example","isha",46.7]
print(list1 == list2)       # false bcz both has different memory reference
list = [0,1,2,3,4,5]
print(list[-1])
print(list[-3:])
print(list[-3:-1])

# list methods 
mylist = [2,4,6,8,10]
mylist.append(12)              # insert value at the end
mylist.insert(2,9)             # insert value at specific position
mylist.extend([14,16])         # insert another iterable(tuples,sets,dictionary,list) to the given list
mylist.remove(9)               # remove the element with the specified value
mylist.pop(1)                  # removes and return the element
mylist.pop()                   # remove last item
del mylist[0]                  # removes the element but does not return the element
del mylist                     # deletes the whole list completely
# mylist.clear()                # clears all the elements from the list
# print(mylist)

# list comprehension
squared_nums = [x**2 for x in range(11)]
print(f"squared list: {squared_nums}")


# updating list values
li1 = [11,12,13,14,15]
print(li1)
li1 [2] = 77
print(li1)
li1[1:3] = [45,78]
print(li1)

# operations

# repitition of list
repetition = list*2
print(repetition)

# concatination of list
concatination = list1 + list2
print(concatination)

# length of list
print(len(list))

# iteration
for i in list:
    print(i)

# membership of list
print(2 in list)
print(48 in list)
print(78 in li1)

# adding elements in the list
emptyList = []
n = int(input("enter the no of elements:"))
for i in range(0,n):
    emptyList.append(input("enter the item:"))
print("printing the items of the list")
for i in emptyList:
     print(i,end = " ")

print('\n')

#printing directory of list
print(f'Directory of list1 is: {dir(list1)}')