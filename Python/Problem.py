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

s = "07:05:45PM"

def timeConversion(s):
    # Get AM/PM
    period = s[-2:]
    # Get hours
    hour = int(s[:2])
    
    if period == "PM" and hour != 12:
        hour += 12
    elif period == "AM" and hour == 12:
        hour = 0
        
    # Format hour to 2 digits and append the rest of the string (minutes:seconds)
    return "{:02d}".format(hour) + s[2:-2]