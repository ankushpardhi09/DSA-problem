#Exception handling in python

#Types Exception handling
# 1. Runtime Exception handling : Exmaple : ZeroDivisionError, NameError, IndexError, KeyError, ValueError, TypeError
# we can handle these type of exception by using try and except block. we can also use else and finally block with try and except block.
# Real World example of runtime exception handling is when we are taking input from user and we want to handle the exception if user enters invalid input.
# Runtime exception handling is also used when we are working with files and we want to handle the exception if file is not found or if there is an error while reading or writing to the file.
# What is use Runtime exception handling : it is used to handle the exception that occurs during the execution of the program. 
# it is used to prevent the program from crashing and to provide a user friendly message to the user.

# 2. User defined Exception handling : we can create our own exception handling by using class and raise keyword 
# we can create our own exception handling by creating a class that inherits from the built-in Exception class and then we can raise the exception by using the raise keyword.
# Real World example of user defined exception handling is when we want to create our own exception for a specific error that is not covered by the built-in exceptions. for example, we can create our own exception for invalid input or for a specific error in our program.
# What is use User defined exception handling : it is used to create our own exception for a specific error that is not covered by the built-in exceptions. it is also used to provide a more specific and user friendly message to the user when an error occurs.

#Type of exception
#1. ZeroDivisionError : it occurs when we try to divide a number by zero. for example, if we try to divide 10 by 0, it will raise a ZeroDivisionError. we can handle this exception by using try and except block. we can also use else and finally block with try and except block.
#2. NameError : it occurs when we try to access a variable that is not defined. for example, if we try to print a variable that is not defined, it will raise a NameError. we can handle this exception by using try and except block. we can also use else and finally block with try and except block.
#3. IndexError : it occurs when we try to access an index that is out of range. for example, if we try to access the 5th element of a list that has only 4 elements, it will raise an IndexError. we can handle this exception by using try and except block. we can also use else and finally block with try and except block.
#4. KeyError : it occurs when we try to access a key that is not present in a dictionary. for example, if we try to access a key that is not present in a dictionary, it will raise a KeyError. we can handle this exception by using try and except block. we can also use else and finally block with try and except block.
#5. ValueError : it occurs when we try to convert a value to a specific type and the value is not compatible with that type. for example, if we try to convert a string to an integer and the string is not a valid integer, it will raise a ValueError. we can handle this exception by using try and except block. we can also use else and finally block with try and except block.
#6. TypeError  : it occurs when we try to perform an operation on a value of a specific type and the value is not compatible with that type. for example, if we try to add a string and an integer, it will raise a TypeError. we can handle this exception by using try and except block. we can also use else and finally block with try and except block.

#Example of Runtime exception handling

# try:
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter another number: "))
#     result = num1 / num2
#     print("The result is: ", result)
# except ZeroDivisionError:
#     print("You cannot divide a number by zero.")
# except ValueError:
#     print("Invalid input. Please enter a valid number.")

# #Example of User defined exception handling
# class InvalidInputError(Exception):
#     pass

# def validate_input(value):
#     if value < 0:
#         raise InvalidInputError("Input cannot be negative.")
#     else:
#         print("Valid input: ", value)
# try:
#     user_input = int(input("Enter a positive number: "))
#     validate_input(user_input)  
# except InvalidInputError as e:
#     print(e)


#Example of logging exception handling
# import logging
# logging.basicConfig(filename='newfile.txt', level=logging.DEBUG)
# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     result = a / b
#     print("The result is: ", result)
# except (ZeroDivisionError, ValueError) as message:
#     print(massage)
#     logging.exception(massage)
# print("logging level is set to DEBUG, so the exception message will be logged in the newfile.txt file.")    


import csv
f= open('Marks.csv', 'a')
a= csv.writer(f)
a.writerow(['StuID', 'StuName', 'Physics', 'Chemistry', 'Maths', 'Total', 'Percentage', 'result'])
StuID = input("Enter Student ID: ")
StuName = input("Enter Student Name: ")
try:
    Physics = int(input("Enter marks for Physics: "))
    Chemistry = int(input("Enter marks for Chemistry: "))
    Maths = int(input("Enter marks for Maths: "))
    Total = Physics + Chemistry + Maths
    Percentage = Total / 3
    if Percentage >= 40:
        result = "Pass"
    else:
        result = "Fail" 
    a.writerow([StuID, StuName, Physics, Chemistry, Maths, Total, Percentage, result])
except ValueError:
    print("Invalid input. Please enter a valid number for marks.")


