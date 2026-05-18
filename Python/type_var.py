#types of instance variable(instance var)
# instance variable is depandent on object
# instance variable is not shared by all the objects of the class
# It is create a Sepaarte memory for each object
# class New1:
#     def __init__(self):
#         self.age = 10 #instance variable
# obj1 = New1()
# obj2 = New1()
# obj3 = New1()
# obj1.age = 20
# print(obj1.age) #30
# print(obj2.age) #20
# print(obj3.age) #20

#types of instance variable(static var)
# static variable is not depandent on object it is depandent on class
# static variable is shared by all the objects of the class
# It is create a single memory for all the objects of the class
# class New2:
#     a = 10 #static variable

#     def __init__(self):
#         self.name = "Ankush" #instance variable
# obj1 = New2()
# obj2 = New2()
# obj3 = New2()
# New2.a = 50
# print(obj1.a) #50
# print(obj2.a) #50   
# print(obj3.a) #50


#for evrey object a separete copy of instance variable is created but for static variable
# only one copy is created will be created it is accessible for every object of the class

class College:
    college_name = "ABC College" #static variable

    def __init__(self):
        self.student_name = "Ankush" #instance variable
    
principal = College()#object created for class College
teacher = College()#object created for class College
accountant = College()#object created for class College
print(principal.college_name) #ABC College
print(teacher.college_name) #ABC College
print(accountant.college_name) #ABC College
print(principal.student_name) #Ankush
print(teacher.student_name) #Ankush
print(accountant.student_name) #Ankush
    


