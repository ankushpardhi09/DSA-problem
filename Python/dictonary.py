# mydict ={
# 101: "prajwal",
# 102: "suresh",
# 103: "kumar",
# "104": "kumar",
# "105": "ankit",
#  101 : "ayush",
#  104 : "kunal"
# }

# print(mydict)

# a= mydict[101]#to access the value of the key 101
# print(a)

# mydict[102] = "satyarth"#to add a new key-value pair to the dictionary
# print(mydict)

# for x in mydict:
#     print(x)

# for x in mydict.values():
#     print(x)

# for x,y in mydict.items():
#     print(x,y)

# mydict["mobile_no"] = 8805600780
# print(mydict)

# mydict.pop(101)#to remove the key 101 and its value from the dictionary
# print(mydict)   

# a ={(1,2):1,(3,4):2,(5,6):3}#dictionary with tuple keys and integer values
# print(a[5,6])#to access the value of the key (5,6) which is 3 because the key is a tuple and not a string


# a={'a':1,'b':2,'c':3}#dictionary with string keys and integer values
# print(a['a','b']) #to access the value of the key 'a' and 'b' which is not possible because the key is a tuple and not a string

# arr = {}
# arr[1] = 1
# arr['1'] = 2
# arr[1] += 1
# print(arr)
# total = 0
# for x in arr:
#     total += arr[x]
# print(total)


# my_dict = {}
# my_dict[1] = 1
# my_dict['1'] = 2
# my_dict[1.0] = 4
# print(my_dict)
# sum = 0
# for x in my_dict:
#     sum += my_dict[x]
# print(sum)


# my_dict = {}
# my_dict[1,2,4] = 8
# my_dict[4,2,1] = 10
# my_dict[1,2] =12
# sum = 0
# for x in my_dict:
#     sum += my_dict[x]
# print(sum)
# print(my_dict)

# box = {}
# jars = {}
# creates = {}
# box["biscuits"] = 1
# box["cake"] = 3
# jars["jam"] = 4
# creates['box'] = box
# creates['jars'] = jars
# print(creates)
# print(box)
# print(jars)
# print(len(creates['box']))


# disct = {'c':97,'b':98,'a':99 }
# for _ in sorted(disct):
#     print(disct[_])    


# rec ={'Name':"pythomn", 'Age': 20}
# r= rec.copy()#to create a copy of the dictionary
# print(id(r))
# print(id(rec))


# rec = {'Name':"python", 'Age': 20, 'add':"NJ",'country':"India"}
# id1 = id(rec)
# print(id1)
# del rec
# rec = {'Name':"python", 'Age': 20, 'add':"NJ",'country':"India"}
# id2 = id(rec)
# print(id2)
# print(id1 == id2)


# # Find the key with the maximum value in a dictionary use for loop
# my_dict = {'a': 50, 'b': 30, 'c': 70}
# max_key = None
# max_value = float('-inf')  # Initialize to negative infinity
# for key, value in my_dict.items():
#     if value > max_value:
#         max_value = value
#         max_key = key
# print(max_key)

# # Find the key with the minimum value in a dictionary use for loop
# my_dict = {'a': 50, 'b': 30, 'c': 70}
# min_key = None
# min_value = float('inf')  # Initialize to positive infinity
# for key, value in my_dict.items():
#     if value < min_value:
#         min_value = value
#         min_key = key
# print(min_key, min_value)  


# #count frequency of elements in a list using dictionary
# my_list = ['1', '2', '3', '4', '5', '2', '3']
# frequency = {}
# for item in my_list:
#     if item in frequency:
#         frequency[item] += 1
#     else:
#         frequency[item] = 1
# print(frequency)    
 
# # reverse a number using dictionary
# num = 123 
# a = num % 10 #to get the last digit of the number
# num = num // 10 #to remove the last digit of the number
# b = num % 10 #to get the second last digit of the number    
# c = num // 10 #to remove the second last digit of the number
# rev = a*100 + b*10 + c #to reverse the number
# print(rev)

# # reverse a number using dictionary
# num = 123456
# a = num % 10 #to get the last digit of the number a = 6
# num = num // 10 #to remove the last digit of the number num = 12345
# b = num % 10 #to get the second last digit of the number b = 5
# num = num // 10 #to remove the second last digit of the number num = 1234
# c = num % 10 #to get the third last digit of the number c = 4
# num = num // 10 #to remove the third last digit of the number num = 123
# d = num % 10 #to get the fourth last digit of the number d = 3
# num = num // 10 #to remove the fourth last digit of the number num = 12
# e = num % 10 #to get the fifth last digit of the number e = 2
# num = num // 10 #to remove the fifth last digit of the number num = 1
# f = num % 10 #to get the sixth last digit of the number f = 1
# rev = a*100000 + b*10000 + c*1000 + d*100 + e*10 + f #to reverse the number
# print(rev)


# Amount = int(input("Enter the amount for withdraw: "))
# print("100 notes= ", Amount//100)#to calculate the number of 100 notes in the amount 
# print("50 notes= ", (Amount % 100)//50)
# print("20 notes= ", ((Amount % 100) % 50)//20)
# print("10 notes= ", (((Amount % 100) % 50) % 20)//10)
# print("5 notes= ", ((((Amount % 100) % 50) % 20) % 10)//5)
# print("2 notes= ", (((((Amount % 100) % 50) % 20) % 10) % 5)//2)
# print("1 notes= ", (((((Amount % 100) % 50) % 20) % 10) % 5) % 2)