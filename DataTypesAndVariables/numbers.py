'''There are three numeric types in Python:
int
float
complex'''

import random                     # import random number in python
from decimal import Decimal       # when we want to work with precise decimal numbers
from fractions import Fraction    # works with fraction values

print(Decimal("0.1") + Decimal("0.1") + Decimal("0.1") - Decimal("0.3" ))  # this will give exact result of addition

myFrac = Fraction(2,7)
print("My fraction is :", myFrac)    # prints My fraction is : 2

print(random.randrange(1, 10))
l1 = ["Raj", "Alex", "John", "Stephen"]
print(random.choice(l1))        # choose a random element from the list
print(random.shuffle(l1))       # shuffles the elements of the list

x = 1                          # int
y = 2.6                        # float
z = 3 + 4j                     # complex

print(type(z))
# numbers with "e" indicate float type
w = 5.0e-7                    # float

# type conversions
print(float(x))
print(complex(y))
# print(int(z))             # complex numbers can't be converted into int or float

# to specify the type of variable explicitly in python is done by casting
a = float('5')              # convert string '5' to integer
print(a)
print(type(a))

# to convert any number into binary,octal,or any other type using its base value
print(int("64", 16))
print(int("64", 8))          # tells the octal value of the number 
print(int("1000", 2))        # it tells the binary of the given number                     
