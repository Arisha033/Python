# tuples in python
# A tuple is a collection which is ordered, unchangeable and allow duplicate values.
nested_tuple = ("python",{4:7,8:9},(3,2,1),[78,"alex"])
print(type(nested_tuple))
print(nested_tuple)

# creating a tuple with single element is not possible
single_tuple = ("tuple")
print(type(single_tuple))           # it returns str type

# creating a tuple with single element is done as follows:
single_tuple = ("tuple",)
print(type(single_tuple))
print(nested_tuple [0][3])
print(nested_tuple [-3])
print(nested_tuple [-4][-1])

# slicing
print(nested_tuple[0:])
print(nested_tuple[-2:-1])

# update a tuple
'''We can't update a tuple, 
but we can convert it into a list, 
update that list and then convert it back to a tuple'''

thistuple = tuple(("apple", "banana", "cherry"))

tuple_into_list = list(thistuple)          # convert tuple to list
tuple_into_list[1] = "orange"

tuple_into_list.append("grapes")          # add item at the end of tuple
updated_tuple = tuple(tuple_into_list)

print(f"Updated tuple: {updated_tuple}")

# we can change whole tuple
thistuple = ("peas", "carrot", "tomato")
print(f"New tuple: {thistuple}")

# remove items from a tuple
try:
  del nested_tuple [1]
  print(nested_tuple)    #tuple dosn't support item deletion
except:
  print("items of the tuples can't be deleted")

try:
  item_to_remove = thistuple.remove("banana")          # can't remove items
  print(item_to_remove)
except:
   print("tuples don't have .remove() method")

# unpacking of a tuple(extracting values into varibles)
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

# methods of tuple
# count() method
count = fruits.count("apple")
print(count)

# index() method
Tuple_data = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res1 = Tuple_data.index(3)        # returns the index of 1st occurrence of 3
res2 = Tuple_data.index(3,4)      # returns the index of 1st occurrence of 3 afer 4th index
print(res1)
print(res2)

# concatination of tuple
print(Tuple_data + (6,7,8))

# repitation in  tuple
print(Tuple_data * 2)
print(Tuple_data.__sizeof__())

# membership test in tuple
print("python" in nested_tuple)
print("alex" not in nested_tuple)
print(3 in Tuple_data)

# iteration in tuple
for item in Tuple_data:
    print(item)