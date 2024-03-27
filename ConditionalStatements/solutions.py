''' 1. Age Group Categorization '''
# user_age = int(input("Enter your age: "))

# if user_age < 13:
#     print("You are a child.")
# elif user_age < 20:
#     print("You are teenager.")
# elif user_age < 60:
#     print("You are adult.") 
# else:
#     print("You are Senior.")


''' 2. Movie Ticket Pricing '''
# age = 20
# day = "Wednesday"

# price = 12 if age >= 18 else 8

# if day == "Wednesday":
#     price = price - 2
#     print(f"Ticket price for you is: {price}.")


''' 3. Grade Calculator '''
# score = int(input("Enter your score: "))

# if score >= 101:
#     print("Please enter the valid score.")
#     exit()

# if  score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# elif score >= 60:
#     grade = "D"
# else:
#     grade = "F"
# print(f"You got: {grade}.")


''' 4. Fruit Ripeness Checker '''
# fruit = "banana"
# fruit_color = "green"

# if fruit == "banana":
#     if fruit_color == "green":
#         print(f"{fruit} is Unripe.")
#     elif fruit_color == "yellow":
#         print(f"{fruit} is ripe.")
#     else:
#         print(f"{fruit} is overripe.")
# else:
#     print("No information for fruits other than banana.")


''' 5. Weather Activity Suggestion '''
# weather = "Sunny"

# if weather == "Sunny":
#     activity = "Go for a walk."
# elif weather == "Rainy":
#     activity = "Read a book."
# elif weather == "Snowy":
#     activity = "Build a snowman."
# else:
#     activity = "Do whatever you want to!"
# print(activity)


''' 6. Transportation Mode Selection '''
# distance = 15

# if distance < 3:
#     mode = "walk"
# elif distance < 15:
#     mode = "bike"
# elif distance >= 15:
#     mode = "car"
# print(f"Your mode of transportation is: {mode}")


''' 7. Coffee Customization '''
# order_size = "small"
# extra_shot = True

# if extra_shot:
#     coffee = order_size + " with extra shot of espresso."
# else:
#     coffee = order_size + " with no extra espresso."

# print(f"Your order is : {coffee}")


'''8. Password Strength Checker '''
# password = 'sghua%$3'
# if len(password) < 6:
#     strength = "Weak"
# elif len(password) < 10:
#     strength = "Medium"
# else:
#     strength = "Strong"
# print(f"Your password strength is : {strength}")


''' 9. Leap Year Checker '''
# year = 2024

# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) :
#     print(f"{year} is a leap year.")

# else:
#     print(f"{year} is not a leap year.")


''' 10. Pet Food Recommendation '''
# petSpecies = "Cat"
# petAge = 5

# if petSpecies == "Dog":
#     if  petAge < 5:
#          print(f"Food for you {petSpecies} is Puppy food")
#     else:
#         print(f"Food for you {petSpecies} is Senior Dog food")
# elif petSpecies == "Cat":
#     if petAge < 5:
#         print(f"Food for your {petSpecies} is Junior Cat Food.")
#     else:
#         print(f"Food for your {petSpecies} is Senior Cat Food.")
# else:
#     print("We don't have suggestions for this type of pet.")