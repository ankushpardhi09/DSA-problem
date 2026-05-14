#what is While loop?
# A while loop is a control flow statement that allows code to be executed repeatedly based on a given boolean condition. 
# The loop continues to execute as long as the condition is true. Once the condition becomes false, the loop terminates and 
# the program continues with the next statement after the loop.
# i = 1 
# while i <= 5:
#     print(i)
#     i += 1

#________________________________________________#

# what is Function?
# A function is a block of code that performs a specific task and can be reused multiple times.
# function provides a modularity to the code and helps in breaking down complex problems into smaller, manageable pieces.

# def hello():
#     print("Hello, World!")
# hello()  # Calling the function to execute its code

#what is difference between function and method?
#function: is a block of code that perform a specific task and can be reused multiple times, while a method is a function 
# that is associated with an object and can access and modify the object's data.
#methods: In Simple terms, a method is a function that is defined within a class and is associated with an object of that class.

# def arithmatic():
#     a =int(input("Enter the first number: "))
#     b =int(input("Enter the second number: "))
#     sum = a + b
#     sub = a - b
#     mul = a * b
#     div = a / a
#     return sum, sub, mul, div

# result = arithmatic()
# print("arithmatic = ",result) #to get the sum of the two numbers


#how many type of aruguments we pass in function?
#1. Positional arguments: are the most common type of arguments, where the values are passed in the same order as the parameters defined in the function.
#2. Keyword arguments: are the arguments that are passed by specifying the parameter name along with the value. This allows you to pass the arguments in any order.
#3. Default arguments: are the arguments that have a default value assigned to them. If the caller does not provide a value for that argument, the default value will be used.
#4. Variable-length arguments: are the arguments that can accept a variable number of values.   
#5. veriable-number of arguments: are the arguments that can accept a variable number of values. There are two types of variable-length arguments: *args and **kwargs. *args is used to pass a variable number of non-keyword arguments, while **kwargs is used to pass a variable number of keyword arguments.

# # positional arguments
# def arithmatic(a,b):
#     sum = a + b
#     sub = a - b
#     mul = a * b
#     div = a / a
#     return sum, sub, mul, div
# #positional arguments
# result = arithmatic(5,5)
# print("arithmatic = ",result) #to get the sum of the two numbers

#keyword arguments
# def credentials(username, password):
#     if username == "admin" == password == "admin":
#         print("Login successful")
#     else:
#         print("Login failed")
# credentials(username="admin", password="admin")#calling the function with keyword arguments

#default arguments
# def cityName(city="pune"):
#     print(city)

# cityName("Mumbai") #calling the function with default arguments
# cityName("Nagpur") #calling the function with default arguments
# cityName()#calling the function without arguments, it will give an error because the function is defined with a parameter and 
#it is not optional. To fix this error, we can provide a default value for the parameter in the function definition. 


#variable-length arguments
# def cityName(*name):
#     print(name)

# cityName("Mumbai","nagpur","Delhi") #calling the function with default arguments


#modularity approach in function
def add():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    print(a + b)

def sub():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    print(a - b)

def div():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    print(a / b)

def mul():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    print(a * b)

while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Divide")
    print("4. Multiply")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add()
    elif choice == 2:
        sub()
    elif choice == 3:
        div()
    elif choice == 4:
        mul()
    elif choice == 5:
        break
    else:
        print("Invalid choice")
    