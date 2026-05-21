# Polymorphism in Python
# Polymorphism is a fundamental concept in object-oriented programming that allows objects of different classes to be treated as objects of a common superclass.
# In Python, polymorphism is achieved through method overriding and duck typing. Method overriding allows a subclass to provide a specific implementation of a method that is already defined in its superclass. Duck typing allows an object to be treated as an instance of a class based on its behavior rather than its actual type.
# Method Overriding Example

#type of polymorphism:
#1. Compile-time Polymorphism (Method Overloading)
# Method Overloading: In Python, method overloading is not directly supported as it is in some other programming languages. However, you can achieve a similar effect by using default arguments or variable-length arguments in your methods. This allows you to define a single method that can handle different numbers of arguments or different types of arguments.
# type of Compile-time Polymorphism: only one type of compile-time polymorphism is there in python and that is operator overloading.
#operator Overloading: In Python, you can overload operators to define custom behavior for built-in operators when applied to instances of your classes. For example, you can overload the + operator to concatenate two objects of a custom class.

#2. Run-time Polymorphism (Method Overriding)
# Method Overriding: In Python, method overriding occurs when a subclass provides a specific implementation of a method that is already defined in its superclass. The overridden method in the subclass will be called instead of the method in the superclass when an instance of the subclass is used.

# method overriding example
class RBI:
    def home_loan(self):
        print("RBI home loan interest rate is 8%")

    def Equcation_loan(self):
        print("RBI Equcation loan interest rate is 9%")

class SBI(RBI):
    def Equcation_loan(self):
        print("SBI Equcation loan interest rate is 10%")
        super().Equcation_loan()# calling the method of parent class using super() function

obj = SBI()
obj.Equcation_loan()# calling method2 of SBI using the object of SBI


#method overloading in operator overloading example
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"
point1 = Point(2, 3)
point2 = Point(4, 5)
result = point1 + point2
print(result)  # Output: (6, 8)

    