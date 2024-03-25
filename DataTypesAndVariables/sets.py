# Set items are unordered, unchangeable(can't change the items but you can remove or add items), and do not allow duplicate values.
Days = {"Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"}
print(Days)

# empty set can be created using set()
set1 = set()

# empty curly braces will create a dictionary
set2 = {}
print(type(set1))        #  set
print(type(set2))        # dictionary

# access items of the set
# print(Days[0])     # can't access it like this, use for loop instead

for i in Days:
    print(i)

print(type(Days))

# add items to the set
Days.add("Sunday")       
print(f"New set of days: {Days}")

Days.update({"January","February"})
print(f"Updated set of months: {Days}")

# remove items from the set
'''If the item to remove does not exist, remove() will raise an error.
If the item to remove does not exist, discard() will NOT raise an error.'''

Days.remove("Tuesday")          # removes tuesday from the set
print(f"Remove Tuesday from the set: {Days}")

Days.discard("Monday")         # removes monday from the set
print(f"Remove Monday from the set: {Days}")

Days.pop()                     # removes random item from the set
print(f"Set after removing random item: {Days}")

Days.clear()                   # empties the set
print(f"Set after using clear(): {Days}")

del Days
print(f"Set is deleted")     # deletes the set completely

# Operations on set
a = {"Devansh", "bob", "castle"}    
b = {"castle", "dude", "emyway", "bob"}    
c = {"fuson", "gaurav", "castle"}    

print(f"Union of a and b: {a.union(b)}")
print(f"Intersection of a and b: {a.intersection(b)}") 
print(f"Difference of a and b: {a.difference(b)}")
print(f"Symmetric difference of a and b: {a.symmetric_difference(b)}")    # symmetric_difference() method keeps all items EXCEPT the duplicates.
print(f"a is subset of b: {a.issubset(b)}")  
print(f"a is superset of b: {a.issuperset(b)}")  
print(f"Elements common in both sets are: {a.isdisjoint(b)}")          # returns false if no element is common

'''difference_update() removes all elements from the set that are also present in another set(common items),
    it modifies the set in place and returns None while difference() method return a new set.
'''
set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
set1.difference_update(set2)
print(f"Set after difference_update: {set1}")

'''intersection_update() updates the set with the intersection of both the sets,
   it modifies the set in place and returns None.
 '''
set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
set1.intersection_update(set2)
print(f"Set after intersection_upate: {set1}")

'''symmetric_difference_update updates the set with the symmetric difference of both the sets,
    it modifies the set and returns None.
    '''
set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
set1.symmetric_difference_update(set2)
print(f"Set after symmetric_difference_update: {set1}")


# Frozen Set
'''
They are immutable version of set
- methods like add(), remove(), and pop() are not available for frozenset objects.
- can perform operations like intersection, union, difference, and symmetric difference, return new frozenset objects rather than modifying the original object
- useful in situations where you want to use a set as an element of another set, or as a key in a dictionary.
'''
frozen_set = frozenset([1,2,3,4,5])
print(type(frozen_set))

# iterate  over a frozenset object using loop
for i in frozen_set:
    print(i)

#frozen_set.add(7)                 # error as we can't change the items of frozenset

listOfSets = [{1,2,3}, {2,3,4}, {3,4,5}]
convertedList = [frozenset(s) for s in listOfSets]
print("Converted List: ", convertedList)
print(type(convertedList))             # list
print(type(convertedList[0]))          # frozen set

# convert dictionary to frozen set
dictionary = {"Name":"John", "Country":"USA", "ID":101}
print(type(dictionary))

frozenset = frozenset(dictionary)
print(type(frozenset))