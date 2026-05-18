# name ="Ankushpardhi"
# print(name[0])#indexing starts from 0
# print(name[1])#print(name[2])
# print(name[-1])#negative indexing starts from -1
# print(name[11])#last character using positive index
# print(name[0:5])#slicing: start index : end index : step
# print(name[1:0])#print(name[5:0])#start index is greater than end index
# print(name[0:5])#start index is included and end index is excluded
# print(name[:])#start to end
# print(name[0:5:2])#print(name[::2])#start to end with step 2
# print(name[::-1])#reverse the string


# s = "Python are High level programming Language"
# print(s.lower())#convert to lowercase
# print(s.upper())#convert to uppercase
# print(s.title())#convert to title case
# print(s.capitalize())#convert first character to uppercase and rest to lowercase
# print(s.swapcase())#convert uppercase to lowercase and vice versa

# name = " ankush"
# sal = 5000
# age = 25
# print("{}sal is {} age is {}".format(name,sal,age))#string formatting using format method
# print("{0} sal is {1} age is {2}".format(name, sal, age))#string formatting using f-string
# print("{x} sal is {y} age is {z}".format(x=name, y=sal, z=age))#string formatting using f-string with variable names
# A=1
# print(f"{A} is a Good boy")#string formatting using f-string with variable names


# name = "Ankush"
# for i in name: #=> for i in range(len(name)):
#     print(i)


# # how to remove Duplicate characters and print the length of the string and reverse of the string
# name="Prashant"#string with duplicate characters
# new_name=""#empty string to store the new name without duplicate characters
# M = len(name)
# for i in range(M-1,-1,-1):#for i in range(len(name)):
#     if name[i] not in new_name:#check if the character is not already in the new_name string
#         new_name+=name[i]#if the character is not in the new_name string then add it to the new_name string
# print(new_name) 

# #how to remove duplicate characters and print the length of the string and reverse of the string with 
# # out using indexing or slicing or built-in functions or others shortcuts methods
# name= "Ankushpardhi"
# new_name=""
# for i in name:
#     if i not in new_name:
#         new_name+=i
# # print reverse of the string
# print(name[::-1])


# #Write a program to if String is palindrome or not
# name ="nayan"
# print(name)
# print(name[::-1])#reverse the string
# if name == name[::-1]:#check if the string is equal to its reverse
#     print("String is palindrome")
# else:   
#     print("String is not palindrome")

# # check for Anagram
# # Write a program to check if two strings are anagrams of each other 
# s1 = "listen"
# s2 = "silent"
# if sorted(s1) == sorted(s2):#sort the characters of both strings and compare them
#     print("Strings are anagrams")
# else:
#     print("Strings are not anagrams")

# # count the number of vowels and consonants in a string
# s1 = "listen"
# vowels = ['a', 'e', 'i', 'o', 'u']
# vowel_count = 0
# consonant_count = 0
# for i in s1:
#     if i in vowels:
#         vowel_count += 1
#     else:
#         consonant_count += 1

# print(f"Number of vowels: {vowel_count}")
# print(f"Number of consonants: {consonant_count}")


# # count the number of words in a string
# # Write a program to count the number of words in a string
# s1 = "The quick brown fox jumps over the lazy dog"
# word_count = 0
# for i in s1:
#     if i == " ":
#         word_count = word_count + 1
# print(f"Number of words: {word_count + 1}")#add 1 to the word count to account for the last word


# Bodmas Rule



# # check how many Special characters are there in the string
# S= "hb9#n8@kdilhdDDn%7(@nebvuwdesi*@)"
# #check how many Special characters are there in the string
# count = 0
# z =ord(S[0])#ord() function returns the ASCII value of the character
# print(z)

# if (z >= 32 and z <= 47) or (z >= 58 and z <= 64) or (z >= 91 and z <= 96) or (z >= 123 and z <= 126):
#     count = count + 1


# titel case Sentance
# S= "the quick brown fox jumps over the lazy dog"
# new_S = ""
# for i in S: 
#     if i == " ":
#         new_S = new_S + " "
#     else:
#         new_S = new_S + i.title()
# print(new_S)

# # check a string is Alphanumeric or not(true or false)
# print("Ankjkush1njovnio95i-94no23ew".isalnum())#check if the string contains only alphanumeric characters (letters and numbers)
# print("ankushpardhi".isalpha())#check if the string contains only alphabetic characters (letters)
# print("1234567890f".isdigit())#check if the string contains only digits
# print(" ".isspace())#check if the string contains only whitespace characters (spaces, tabs, etc.)
# print("Ankush".isupper())#check if the string contains only uppercase characters (letters)
# print("Ankush".islower())#check if the string contains only lowercase characters (letters)
# print(" ".istitle())#check if the string is in title case (first letter of each word is uppercase and the rest are lowercase)
# print(" ".isspace())#check if the string contains only whitespace characters (spaces, tabs, etc.)
# print("Ankush".isprintable())#check if the string contains only printable characters (letters, numbers, punctuation, etc.)

# print("Ankushpardhi".find("k"))#find the index of the first occurrence of the specified substring
# print("Ankush".index("k"))#find the index of the first occurrence of the specified substring and raise an error if the substring is not found
# print("Ankush".count("k"))#count the number of occurrences of the specified substring


#  pattern printing question
i = 1 
j = 1

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i, end=" ")#print the value of i and end with a space instead of a new line
#     print()

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(j, end=" ")#print the value of j and end with a space instead of a new line
#     print()

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i+j, end=" ")#print the sum of i and j and end with a space instead of a new line
#     print()

# write a program to print the following pattern
# A A A
# B B B
# C C C
# n = int(input("Enter the number of rows: "))
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print(chr(64+i), end=" ")#print the value of j and end with a space instead of a new line
#     print()

# n = int(input("Enter the number of rows: "))
# for i in range(1, n+1):
#     for j in range(1, 1+i):
#         print("*", end=" ")
#     print()

# n = int(input("Enter the number of rows: "))
# for i in range(1, n+1):
#     for j in range(1, n+2-i):
#         print(chr(64+j), end=" ")#print the value of j and end with a space instead of a new line
#     print()

# import time
# n = int(input("Enter the number of rows: "))
# for i in range(1, n+1):
#     print(" "*(n-i), end=" ")
#     for j in range(1, i+1):
#         time.sleep(1)#add a delay of 0.5 seconds between each print statement
#         print("*", end=" ")
#     print()

# n = [1, 2, 3, 4, 5]

# prod = 1

# for i in a:

#removing spaces from a string
#1.rstrip() method removes the leading spaces from a string
#2.lstrip() method removes the trailing spaces from a string
#3.strip() method removes both leading and trailing spaces from a string

# city = input ("Enter the name of the city: ")
# scity = city.strip()#split the city name into a list of words
# if scity == 'hyderabad':
#     print("Hyderabad is the capital of Telangana")
# elif scity == 'mumbai':
#     print("Mumbai is the capital of Maharashtra")
# elif scity == 'delhi':
#     print("Delhi is the capital of India")
# else:
#     print("City not found")

# # compare the triplets
# a= [5, 6, 7]
# b= [3, 6, 10]   

# def compareTriplets(a, b):
#     alice_score=0
#     bob_score=0
#     for alice_val, bob_val in zip(a, b):#zip() function is used to iterate over two or more 
#         #iterables (lists, tuples, etc.) in parallel, returning a tuple of the corresponding elements from each 
#         # iterable at each iteration.
#         if alice_val > bob_val:
#             alice_score += 1
#         elif alice_val < bob_val:
#             bob_score += 1
            
#     return [alice_score, bob_score]
# result = compareTriplets(a, b)
# print(result)

   
#Write a program to Accept Student name and marks  form the keyword and Create a dictionary .
# also display student marks by taking Student name .

# n = int(input("Enter the number of students: "))# get the number of students from user input
# students = {}# create an empty dictionary to store student names and marks
# for _ in range(n):# loop to get student names and marks from user input
#     name = input("Enter student name: ")# get the student's name from user input
#     marks = float(input("Enter student marks: "))# get the student's marks from user input and convert it to a float
#     students[name] = marks# add the student's name and marks to the dictionary

# while True:# loop to allow the user to query student marks by name
#     query = input("Enter student name to get marks (or 'exit' to quit): ")# get the student's name to query from user input
#     if query.lower() == 'exit':# check if the user wants to exit the program
#         print("Exiting program.")# if the user wants to exit, print a message and break out of the loop
#         break
#     elif query in students:# check if the queried student name exists in the dictionary
#         print(f"{query}'s marks: {students[query]}")# if the student name exists, print the student's marks
#     else:# if the student name does not exist in the dictionary, print a message indicating that the student was not found
#         print("Student not found.")

# n=int(input("Enter the number of students: "))
# d={}
# for i in range(n):
#     name=input("Enter student name: ")
#     marks=float(input("Enter student marks: "))
#     d[name]=marks
# while True:
#     name=input("Enter student name to get marks (or 'exit' to quit): ")
#     marks=d.get(name,-1)
#     if marks==-1:
#         print("Student not found.")
#     else:
#         print("the marks of ",name,"is",marks)
#     options=input("Do you want to continue? (yes/no): ")
#     if options == "no":
#         break
# print("thank you for using the program.")


#Write a program to access each character of the string in forward and Backward direction  by while loop.
#Input = "lerning python is very easy"

# s = "learning python is very easy"# define the input string
# # Access characters in forward direction using a while loop
# n = len(s)# get the length of the string to determine the number of iterations for the while loop
# i = 0# initialize an index variable to 0
# print("Characters in forward direction:")# print a message indicating that the characters will be displayed in forward direction
# while i < n:# loop while the index is less than the length of the string
#     print(s[i],end='')# print the character at the current index, end='' is used to print characters on the same line without adding a newline after each character
#     i += 1# increment the index to move to the next character
# # Access characters in backward direction using a while loop
# print("\nCharacters in backward direction:")# print a message indicating that the characters will be displayed in backward direction
# j = len(s) - 1# initialize an index variable to the last index of the string
# while j < n and j >= 0 :# loop while the index is within the valid range of indices for the string
#     print(s[j],end='')# print the character at the current index, end='' is used to print characters on the same line without adding a newline after each character
#     j -= 1# decrement the index to move to the previous character




#question : A company provides network encryption for secure data transfer. The data string is encrypted prior to transmission 
# and gets decrypted at the receiving end. But due to some technical error, the encrypted data is lost and the received 
# string is different from the original string by 1 character. Amnold, a network administrator, is tasked with finding the 
# character that got lost in the network so that the bug does not harm other data that is being transferred through the network.
# Write an algorthm to help Arnold find the character that was missing at the receiving end but present at the sending end.
# Input
# The input consists of two space-separated strings – stringSentand stringRec, representing the string that was sent through the 
# network, and the string that was received at the receiving '3nd of the network, respectively.
#Constraints
# NA
# Example
# Input
# abcdfjgerj abcdfijger

# s = "abcdfjgerj abcdfijger"# define the input string containing the sent and received strings separated by a space
# stringSent, stringRec = s.split()# split the input string into the sent and received strings using the split method
# # Create a frequency dictionary to count the occurrences of each character in the sent string
# freq = {}# initialize an empty dictionary to store the frequency of each character in the sent string
# for char in stringSent:# loop through each character in the sent string
#     if char in freq:# if the character is already in the frequency dictionary, increment its count
#         freq[char] += 1# if the character is already in the frequency dictionary, increment its count
#     else:# if the character is not in the frequency dictionary, add it with a count of 1
#         freq[char] = 1# if the character is not in the frequency dictionary, add it with a count of 1
# # Decrease the frequency count for each character in the received string
# for char in stringRec:# loop through each character in the received string
#     if char in freq:# if the character is in the frequency dictionary, decrement its count
#         freq[char] -= 1# if the character is in the frequency dictionary, decrement its count
# # Find the character with a frequency count of 1, which is the missing character
# missing_char = None# initialize a variable to store the missing character
# for char, count in freq.items():# loop through the items in the frequency dictionary
#     if count == 1:# if the count of a character is 1, it means that this character is missing in the received string
#         missing_char = char# set the missing character to the current character
#         break# break out of the loop since we have found the missing character
# if missing_char:# if a missing character was found, print it
#     print("Missing character:", missing_char)# if a missing character was found, print it
    

# v = ['a','e','i','o','u']# define a list of vowels
# W = input ("Enter a string: ")# get a string input from the user
# found = []# initialize an empty list to store the found vowels
# for i in W:# loop through each character in the input string
#     if i in v:# check if the character is a vowel by checking if it is in the list of vowels
#        if i not in found:# if the vowel is not already in the found list, add it to the found list
#            found.append(i)# if the vowel is not already in the found list, add it to the found list
# print("Vowels found in the string:", found)# print the list of found vowels
# print("unique vowels found:", len(found), "form the given word=",W)# print the number of unique vowels found and the original input string

#input: "Ankush"
#process of Executionline by line with the help of code:
# v = ['a','e','i','o','u']# define a list of vowels
# W = input ("Enter a string: ")# get a string input from the user, for example, "Ankush"
# found = []# initialize an empty list to store the found vowels    
# for i in W:# loop through each character in the input string "Ankush"
#     if i in v:# check if the character is a vowel by checking if it is in the list of vowels, for "Ankush", the characters 'A' and 'u' are vowels
#        if i not in found:# if the vowel is not already in the found list, add it to the found list, for "Ankush", 'A' and 'u' will be added to the found list
#            found.append(i)# if the vowel is not already in the found list, add it to the found list, for "Ankush", 'A' and 'u' will be added to the found list
# print("Vowels found in the string:", found)# print the list of found vowels, for "Ankush", it will print "Vowels found in the string: ['A', 'u']"         
# print("unique vowels found:", len(found), "form the given word=",W)# print the number of unique vowels found and the original input string, for "Ankush", it will print "unique vowels found: 2 form the given word= Ankush"


#Question : A company wishes to provide cab service for their N employees, The employees have distance ranging from O to N-1.The company has 
# calculated the total distance from an employee's residence to the company, considering the path to be followed by the cab is a straight path.
# The distance of the company from itself is O. The distance for the employees who live to the left side of the company is represented with a 
# negative sign. The distance for the employees who live to the right side of the company is represented with a positive sign. The cab wil be 
# allotted a range of distance. The company wishes to find the distance for the employees who live within the particular distance range. Write 
# an algorithm to find the distance for the employees who live within the distance range.
# Input
# The first line of the input consists of three space-separated integers-num, start and end
# representing the size of the list (N); the starting value of the range: and the ending value of the
# range, respectively. The second line of the input consists of N space-separated integers
# representing the distances of the employees from the company
# output:
#print space-separated integers representing the distances of the employees who live within the distance range.
#If no employee lives within the distance range, print "No employees found in the given range".

# x,y,z = map(int, input().split())# get the size of the list and the range values from user input
# mylist =[]
# for i in range(x):# loop to get the distances of the employees from user input
#     distance = int(input("Enter the distance of employee {} from the company: ".format(i+1)))# get the distance of each employee from user input
#     mylist.append(distance)# add the distance to the list of distances
# for j in mylist:# loop through the list of distances to find and print the distances that fall within the specified range
#     if j >= y and j <= z:# check if the distance falls within the range defined by y and z
#         print(j, end=' ')# if the distance falls within the range, print it followed by a space



# #Write a program to print the current date and time in the format "YYYY-MM-DD HH:MM:SS".
# import datetime
# date = datetime.datetime.now()# get the current date and time
# print("It's now:{: %Y-%m-%d %H:%M:%S}".format(date))# print the current date and time in a specific format


#Write a program to compare two lists and print whether they are equal or not. Two lists are considered equal if they have the same 
# elements in the same order.
# x=['A','B','C']
# y=['A','B','C']
# z=[1,2,3,4,5]
# print(x==y) # True, because x and y contain the same elements in the same order
# print(x==z) # False, because x and z contain different elements and have different lengths  
# print(x != z) # True, because x and z contain different elements and have different lengths


# Write a program list comprehension.
# val=[2**i for i in range(1,6)]# create a list of values that are powers of 2 from 2^1 to 2^5 using a list comprehension
# print(val) # print the list of values, which will output [2, 4, 8, 16, 32]

# #Write a program dictionary comprehension.
# squared = {i: i**2 for i in range(1, 6)}# create a dictionary where the keys are integers from 1 to 5 and the values are the squares of those integers using a dictionary comprehension
# print(squared) # print the dictionary, which will output {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#Write a program set comprehension.
# doubles = {x:2*x for x in range(1, 6)}# create a set of values that are double the integers from 1 to 5 using a set comprehension
# print(doubles) # print the set of values, which will output {2, 4, 6, 8, 10}


#Write a program to get two integers from user input and print their product.
# a,b=[int(x) for x in input("Enter two numbers: ").split()]# get two integers from user input and unpack them into variables a and b
# print("Product is :", a*b) # print the product of the two integers, which will output "Product is : <product of a and b>"

#Write a program to get three floating-point numbers from user input and print their sum.
# a,b,c = [float(x) for x in input("Enter three numbers: ").split()]# get three floating-point numbers from user input and unpack them into variables a, b, and c
# print("The sum is :", a+b+c)# print the sum of the three floating-point numbers, which will output "The sum is : <sum of a, b, and c>"


# check for loop with continue and else statement it is possible in python to use an else statement with a for loop. 
# The else block will be executed after the for loop completes its iteration, unless the loop is terminated by a break statement.
# If the loop is terminated by a break statement, the else block will not be executed.
# mycart=[10,20,800,40,50]
# for i in mycart:
#     if i>400 :
#         print("This item is too expensive")
#         continue
#     print("This item is affordable")
# else:
#     print("All items have been checked")



# while True:# allow the user to attempt to log in up to 3 times
#     username = input("Enter your username: ")# get the username from user input
#     password = input("Enter your password: ")# get the password from user input
#     if username == "admin" and password == "admin":# check if the username and password match the expected values
#         print("Login successful!")# if the username and password are correct, print a success message
#         break# break out of the loop since the login was successful
#     else:# if the username and password do not match the expected values, print an error message
#         print("Invalid username or password. Please try again.")# if the username and password are incorrect, print an error message
#         username = input("Enter your username: ")# get the username from user input for the next attempt
#         password = input("Enter your password: ")# get the password from user input for the next attempt


# # Tower of Hanoi — clear, recursive implementation
# import time
# import sys

# class TowerOfHanoi:
#     """Recursive Tower of Hanoi solver with printable moves and optional delay."""
#     def __init__(self, n):
#         if n < 0:
#             raise ValueError("Number of disks must be non-negative")
#         self.n = n
#         # Towers stored as lists: larger integers = larger disks
#         self.towers = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}

#     def _move(self, source, target):
#         disk = self.towers[source].pop()
#         self.towers[target].append(disk)

#     def solve(self, delay=0.0, show_steps=True):
#         moves = []

#         def _recurse(m, src, dst, aux):
#             if m == 0:
#                 return
#             _recurse(m - 1, src, aux, dst)
#             self._move(src, dst)
#             moves.append((src, dst))
#             if show_steps:
#                 print(f"Move disk from {src} to {dst}; towers: {self.towers}")
#             if delay > 0:
#                 time.sleep(delay)
#             _recurse(m - 1, aux, dst, src)

#         if show_steps:
#             print(f"Starting: towers: {self.towers}")
#         _recurse(self.n, 'A', 'C', 'B')
#         if show_steps:
#             print(f"Solved: towers: {self.towers}")
#         return moves


# if __name__ == "__main__":
#     # Allow non-interactive usage:
#     #   python Problem.py 7        -> use 7 disks
#     #   python Problem.py pass 7   -> use 7 disks (matches user's "pass 7" request)
#     n = 3
#     args = sys.argv[1:]
#     if args:
#         if args[0].lower() == 'pass' and len(args) >= 2:
#             try:
#                 n = int(args[1])
#             except ValueError:
#                 print("Invalid number after 'pass'; using 3 disks.")
#         else:
#             try:
#                 n = int(args[0])
#             except ValueError:
#                 print("Invalid argument; using 3 disks.")
#     else:
#         try:
#             val = input("Enter number of disks (default 3): ") or "3"
#             # support entering 'pass 7' at prompt as well
#             parts = val.strip().split()
#             if parts and parts[0].lower() == 'pass' and len(parts) >= 2:
#                 n = int(parts[1])
#             else:
#                 n = int(parts[0])
#         except Exception:
#             print("Invalid input; using 3 disks.")
#             n = 3

#     game = TowerOfHanoi(n)
#     game.solve(delay=0.0, show_steps=True)


# #Revere Each word in a String
# s = "Hello World"
# for i in s.split():# split the string into words and loop through each word
#     print(i[::-1], end=' ')# reverse each word and print it followed by a space, ::-1 is used to reverse the string, end=' ' is used
# # to print the reversed words on the same line with a space in between

#check for valid parentheses using stack data structure
# s = input("Enter a string of parentheses: ")# get a string input from the user containing parentheses to check for validity
# stack = []# initialize an empty list to use as a stack for keeping track of opening parentheses
# parentheses_map = {')': '(', '}': '{', ']': '['}# define a mapping of closing parentheses to their corresponding opening parentheses
# is_valid = True# initialize a variable to keep track of whether the parentheses are valid or not
# for char in s:# loop through each character in the input string
#     if char in parentheses_map.values():# if the character is an opening parenthesis, push it onto the stack
#         stack.append(char)# if the character is an opening parenthesis, push it onto the stack
#     elif char in parentheses_map.keys():# if the character is a closing parenthesis, check if it matches the top of the stack
#         if not stack or stack[-1] != parentheses_map[char]:# if the stack is empty or the top of the stack does not match the corresponding opening parenthesis, the parentheses are not valid
#             is_valid = False# set is_valid to False since the parentheses are not valid
#             break# break out of the loop since we have determined that the parentheses are not valid
#         else:# if the closing parenthesis matches the top of the stack, pop the top of the stack
#             stack.pop()# if the closing parenthesis matches the top of the stack, pop the top of the stack
# if stack:# after processing all characters, if the stack is not empty, it means there are unmatched opening parentheses, so the parentheses are not valid
#     is_valid = False# set is_valid to False since there are unmatched opening parentheses
# if is_valid:# if the parentheses are valid, print a message indicating that they are valid
#     print("The parentheses are valid.")# if the parentheses are valid, print a message indicating that they are valid
# else:# if the parentheses are not valid, print a message indicating that they are not valid
#     print("The parentheses are not valid.")# if the parentheses are not valid, print a message indicating that they are not valid
