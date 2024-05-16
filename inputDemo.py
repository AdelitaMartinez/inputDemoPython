# InputDemo.py
# Programmer: Adelita Martinez (amartinez1013@cnm.edu)
# Date: 15 May 2024
# Purpose: Practice getting input from the user

# Get person's name 
name = input('Please enter your name: ')

# Get first number from user
# num_str1 = input('Please enter a number: ') 

# Convert to number
# Float converts values into floating point numbers
# Can also use int to specifically find the integer
# num1 = float(num_str1)

# Both these steps can be put together in one line like below:
num1 = float(input('Please enter a number: '))

# Get second number from user
# num_str2 = input('Please enter another number: ')
# num2 = float(num_str2)

num2 = float(input('Please enter another number: '))

# Add numbers together 
sum = num1 + num2

# Display result
print("Okay, ",name, "The sum of your number is:",sum) 