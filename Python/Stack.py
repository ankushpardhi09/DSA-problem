# eg.
# class Name:
#     age = 30
#     def display(self):
#         print("Hello World")

# obj = Name()
# print(obj.age)
# obj.display()

# eg.
# class Student:
#     def __init__(self):
#         self.name="prashant"
#         self.age=30
#     def display(self):
#         print("Name=", self.name)
#         print("Age=", self.age)
# stuObj = Student()
# print(stuObj)

# eg.
# class Message:
#     def __init__(self):
#         print("I am a Constructor")

#     def shows(self):
#         print("class program")
# obj = Message()
# obj.shows()
# obj2 = Message() 

# eg.
# class StudentInfo:
#     def __init__(self, name, age, roll_no):
#         self.Name = name
#         self.Age = age
#         self.RollNo = roll_no

#     def displayStudentInfo(self):
#         print("Name =",self.Name)
#         print("Age=", self.Age)
#         print("Roll No =", self.RollNo)

# studentObj = StudentInfo("Prakash",34,101)
# studentObj.displayStudentInfo()

# stack implementation without size limit
# Stack Implementation:
# 1 List/Array
# 2 LinkedList
# Now you have to implement stack with size limit

# Stack Operations:
# 1 push
# 2 pop
# 3 peek
# 4 isEmplty
# 5 isFull
# 6 Delete
# 7 Display

# eg.
# import sys
# class Stack:
#     def __init__(self,size):
#         self.myStack =[]  #creating stack
#         self.stackSize = size  #stack size defined

#     def push(self, value):
#         if self.isFull():
#             print("stack is Full")
#         else:
#             self.myStack.append(value)
#             print("Element Pushed")

#     def display(self):
#         print(self.myStack)

#     def isEmpty(self):
#         if self.myStack == []:
#             return True
#         else:
#             return False
        
#     def pop(self):
#         if self.isEmpty():
#             print("stack is Empty")
#         else:
#             print(self.myStack.pop())

#     def peek(self):
#         if self.isEmpty():
#             print("stack is empty")
#         else:
#             print(self.myStack[-1])
        
#     def delete(self):
#         self.myStack = []

#     def isFull(self):
#         if len(self.myStack) == self.stackSize:
#             return True
#         else:
#             return False
        
# size = int(input("Enter the size of stack :"))
# obj = Stack(size)
# print("Stack has created :")
# while True:
#     print("1. Push Operation :")
#     print("2. Display stack")
#     print("3. Pop Operation")
#     print("4. peek Operation")
#     print("5. Delete Stack")
#     print("6. Stack is Full")
#     print("7. Exit")
#     choice = int(input("Enter your Choice :"))
#     if choice == 1 :
#         value = int(input("Enter Value to put into stack :"))
#         obj.push(value)
#     elif choice == 2:
#         obj.display()
#     elif choice ==3:
#         obj.pop()
#     elif choice ==4:
#         obj.peek()
#     elif choice ==5:
#         obj.delete()
#     elif choice ==6:
#         obj.isFull()
#     else:
#         sys.exit()

# eg.
# mylist = [5,7,2,3,7,8,2,3,3] #output= 3
# newDict = {}
# for i in range(len(mylist)): #i=1
#     count = 0
#     key = mylist[i] #key = 7
#     j = 1 # j = 4
#     while j<len(mylist):
#         if key == mylist[j] : #7=7
#             count+=1
#         j = j+1
#     if count>1:
#         newDict[key]= count
# max = newDict
# print(max)

