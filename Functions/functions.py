''' A function is a block of code which perform certain task.
    - you can pass data, known as parameters, into a function.
    - return data as a result
    - allows code reusability
'''
# Difference between function and method
'''
A function is a block of code that is organized and named, designed to perform a specific task
- They are independent and can be called from anywhere in the code.
- In Python, functions  are defined using the def keyword followed by the name of the function (which must be an identifier).

A method is a function associated with an object or a class.
- Methods are defined within a class and are called using an instance of that class or the class itself.
- It operates on data within the object or class.
'''
# Recursion in Python
''' When a function call itself then it is called Recursion'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print("Factorial is : ",factorial(5))