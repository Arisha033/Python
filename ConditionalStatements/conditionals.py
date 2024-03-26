# Conditional statements are used to control the flow of program based on certain condition
# if, elif, else, nested if

# if statement - used to execute a block of code if a condition is true
i = 5
if i <= 10:
    print(f"{i} is less than or equals to 10.")

# if...else statement - used to execute one block of code if the condition is true, and another block of code if the condition is false.
x = 10
if x % 2 == 0:
    print(f"{x} is even.")
else:
    print(f"{x} is odd.")

# if...elif...else statement - used to check multiple conditions, it executes the block of code that meets the condition.
y = -2
if y >= 0:
    print(f"{y} is positive.")
elif y <= 0:
    print(f"{y} is negative.")
else:
    print(f"{y} is zero.")

# nested if statement - if statement inside if, elif or else statement
num = -40
if num % 2 == 0:
    if num >= 0:
        print(f"{num} is even and positive.")
    else:
        print(f"{num} is even but not positive.")
else:
    print(f"{num} is odd.")

# shorthand for if...else - ternary operators or conditional expressions
a = 10
b = 20
print(f"{a} is greater than {b}.") if a > b else print(f"{b} is greater than {a}")


# combine conditional statements
# and operator - checks for both the conditions are true
z = 21
if z % 2 == 0 and z >= 0:
    print(f"{z} is an even postive number.")
else:
    print(f"{z} is not an even positive number.")

# or operator - checks for one of the condition is true
age = 20
if age <= 30 or age >= 18:
    print("You are an adult.")

# not operator - reverse the result
bool = True
print(not bool)

# pass - if you want to leave if statement empty for some reason, then it shows Error, to overcome that use pass statement
num1 = 20
num2 = 40
if num1 > num2:
    pass