# strings are immutable in python
# "" '' and """ """" can be used to define a string

#string slicing
text = "Hello World"
# last index is not included
print(text[0:5])

# third parameter is for step i.e. how many steps to skip, here also last index is not included 
print(text[0:9:2])              # hoping of 1 step
print(f"char:{text[0:9:-1]}")   # results empty string 
print(f"df{text[8:1:-1]}")      # results "oll"

# using triple quotes
print('''They said,"What's there?"''')

# escape single quotes
print('They said,"What\'s going on?"')

# escape double quotes
print("They said,\"What's going on?\"")
 
# escape characters
print("C:\\Users\\DEVANSH SHARMA\\Python32\\Lib")       # backslash
print("This is the \n multiline quotes")                # newline
print("This is \x48\x45\x58 representation")            # hex value

# raw string (print string as it is)
print(r"C:\\Users\\DEVANSH SHARMA\\Python32")

# format string
# using curly braces
print("{} and {} are players".format("virat", "dhoni"))

# using positional argument
print("{1} and {0} are students".format("divya", "shreya"))

# using keyword argument
print("{a},{b},{c} are objects".format(a="table", b="pen", c="glass"))


# string formating
float = 20.6
string = "priya"
integer = 47
print("Hii there im float...my value is %f\nHii there im string...my value is %s\nHii there im integer...my value is %d\n"%(float, string, integer))

# more than one line string
print('''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.''')

# string methods
# original string remains unchanged (immutable)
strObj = "  Hello World!  "
print(strObj.lower())
print(strObj.upper())
print(len(strObj))            # length of the string
print(strObj.strip())         # removes extra spaces from both sides of the string
print(strObj.replace("Hello", "Byie"))  
print(strObj.find("Hel"))     # finds the start index of the string(it returns -1 if not found)
print(strObj.count("o"))      # number of times the string or char appears in the given string

hobbies = "playing, dancing, singing, reading"
print(hobbies.split())        # converts the string into list, by default splits at space
print(hobbies.split(", "))    # splits at comma and a space
languages = ["python", "java", "php", "sql"]   
print(" ".join(languages))    # converts the list into string
