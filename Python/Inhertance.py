#what is inheritance in python?
# Inheritance is a fundamental object-oriented programming (OOP) concept that allows a new class
# (called a child class or subclass) to inherit attributes and behaviors (methods) from an existing class (called a parent class or superclass). 
# This promotes code reusability and establishes a natural hierarchical relationship between classes. 

#how many types of inheritance are there in python?
#1. Single level inheritance
#2. Multi level inheritance
#3. Multiple inheritance

#Single level inheritance
# class class1:# parent class
#     def method1(self):# method1 of class1
#         print("This is method 1")
# class class2(class1):# child class inheriting from class1
#     def method2(self):# method2 of class2
#         print("This is method 2")

# obj = class2()# creating an object of class2
# obj.method1()# calling method1 of class1 using the object of class2
# obj.method2()# calling method2 of class2 using the object of class2



#Multi level inheritance
# class College:# parent class
#     def college_name(self):# method1 of College
#         print("Modern College of Engineering and Technology")
# #===============================================================
# class Student(College):# child class inheriting from College
#     def student_info(self):# method2 of Student
#         print("Ankush Pardhi")
#         print("Computer Science and Engineering")
# #===============================================================
# class Exam(Student):# child class inheriting from Student
#     def subjects(self):# method3 of Exam
#         print("Data Structures and Algorithms")
#         print("Operating Systems")
#         print("Database Management Systems")

# obj = Exam()# creating an object of Exam
# obj.college_name()# calling method1 of College using the object of Exam
# obj.student_info()# calling method2 of Student using the object of Exam
# obj.subjects()# calling method3 of Exam using the object of Exam


#Multiple inheritance
# class SubjectMark:
#     DSA = int(input("Enter your DSA marks: "))
#     OS = int(input("Enter your OS marks: "))
#     DBMS = int(input("Enter your DBMS marks: "))
# #===============================================================
# class PracticalMark:
#    DBMSpractical = int(input("Enter your DBMS practical marks: "))
# #===============================================================
# class Result(SubjectMark, PracticalMark):# child class inheriting from SubjectMark and PracticalMark
#     def total_marks(self):# method1 of Result
#         if self.DSA >= 40 and self.OS >= 40 and self.DBMS >= 40 and self.DBMSpractical >= 40:
#             total = self.DSA + self.OS + self.DBMS + self.DBMSpractical
#             print("Total marks:", total, "You have passed the exam.")
#         else:
#             print("You have failed in the exam.")
# obj = Result()# creating an object of Result
# obj.total_marks()# calling method1 of Result using the object of Result


# how to check Ambiguity in Multiple Inheritance issue in python?
# Ambiguity in multiple inheritance occurs when a child class inherits from multiple parent classes that have methods with the same name. 
# This can lead to confusion about which method should be called when the child class tries to access that method.
# To check for ambiguity in multiple inheritance, you can use the Method Resolution Order (MRO) in Python.
# The MRO is a list that defines the order in which Python looks for methods in a hierarchy of classes.
# You can check the MRO of a class using the __mro__ attribute or the mro() method. 
# If there are methods with the same name in multiple parent classes, the MRO will determine which method is called when the child class accesses that method.

class Parent1:
    def method(self):
        print("This is method from Parent1")
class Parent2:
    def method(self):
        print("This is method from Parent2")
class Child(Parent1, Parent2):
    pass
print(Child.__mro__)# checking the MRO of Child class
# Output: (<class '__main__.Child'>, <class '__main__.Parent1'>, <class '__main__.Parent2'>, <class 'object'>)
# In this example, the MRO of the Child class shows that it will first look for the method in Parent1, then in Parent2, and finally in the base object class.
child_obj = Child()
child_obj.method()# calling the method of Child class, which will call the method of Parent1 due to the MRO


