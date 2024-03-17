#DATA TYPES IN PYTHON
# Numbers
a = 5
print("The type of a is:",type(a))                                  # type of variable
b = 40.5
print("The type of b is:",type(b))                                  # type of variable
print("b is a floating point number",isinstance(40.5,int))          # bcz b is a floating point number not a int number
c = 1+3j
print("The type of c is:",type(c))                                  # type of variable
print("c is a complex number",isinstance(1+3j,complex))             # c is a complex number


#string
str1 = "hello python"
str2 = "how are you"
print(str1[0:2])                    # string from 0th index to index 2 where index 2 is excluded
print(str1[-3:])                    # string from third last character till the end
print(len(str1))                    # length of the string
print(str1.upper())                 # convert all characters in uppercase
print(str1[4])                      # get the individual character at index
print(str1*2)                       # prints string two times
print(str1 +str2)                   # string concatination


#list
li1 = [1,"hi","python",2]
print(type(li1))                                                      # type of list
print(li1)                                                            # prints the list
print(li1[3:])                                                        # returns list at index 3
print(li1[0:2])                                                       # list index starts with 1
print(li1 + li1)                                                      # list concatination
print(li1*2)                                                          # list repetition


#tuple
tu1 = (20 , "apple","sky",12.4)                                       # define a tuple
print(type(tu1))                                                      # type of tuple
print(tu1)                                                            # print the tuple
print(tu1[0:3])                                                       # slicing a tuple
print(tu1[:2])                                                        # slicing a tuple
print(tu1 + tu1)                                                      # concatination of tuple
print(tu1 * 3)                                                        # repition of tuple
# tu1[3] = 30                                                         # (immutable) adding a new element in a tuple results in error


#dictionary
d = {1:'Aakash', 2:'Suman', 3:'Janvi', 4:'Ravi'}                      # define a dictionary
print(d)                                                              # print a dictionary
print("1st name is",d[1])                                             # accessing a dictionary by its key
print("2nd name is "+d[4])
print(d.keys())                                                       # accessing keys 
print(d.values())                                                     # accessing values


#boolean
print(type(True))                                                     # class boolean
print(type(False))
a = False                                                             # define a variable
print(a)
print(a is True)                                                      # false statement


#set
set1=set()                                                            # create empty set
print(set1)                                                           # print empty set
set2={20, 'python', 82.3, 'Alex'}                                     # create a set
print(set2)                                                           # print a set 
set2.add(30)                                                          # add an element in the set
print(set2)                                                           # print modified set
set2.remove(30)                                                       # remove an element from the set
print(set2)                                                           # print modified set
