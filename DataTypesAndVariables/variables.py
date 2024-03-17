print("Hello world....")

# variables and object identity
# variables are immuatable i.e we can't change their memory reference.
a = 50 
b = a
print(id(a))
print(id(b))
a = 500
print(id(a))

name = "arisha"
age = 20
marks = 100.88
print(name)
print(age)
print(marks)
print(type(name))
print(type(age))
print(type(marks))


# local variables
def add():             # defining a function
    a = 20             # variables inside a function
    b = 30
    c = a + b
    print("The sum is :",c)        
add()                   # calling a function 


# global variables
x = 100                              # declare a variable and initialize it  
def mainFunction():                   # global variable in function
    global x                          # print global variable
    print(x)
    x = "Welcome to Python file"       # modify global variable
    print(x)

mainFunction()
print(x,"--local variable")

# delete a variable
x = 100 
print(x)
del x
print(x)

# print single variable
a = 100
print(a)
print((a))

# print multiple variables
x = 20
y = 30
print(x)
print(y)
print(x,y)