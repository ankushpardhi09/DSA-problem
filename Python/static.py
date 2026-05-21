# Static Methods in Python
# Static methods are methods that belong to a class rather than an instance of the class. They can be called on the class itself, without needing to create an instance of the class. Static methods are defined using the @staticmethod decorator.
class Student:
    # By uusing Class name we can Access Static variable
    @staticmethod
    def get_personal_details(first_name, last_name):
        print("Your presonal details are as follows:",first_name, last_name)

    @staticmethod
    def contact_details(mobile_number, roll_number):
        print("Your contact details are as follows:",mobile_number, roll_number)

Student.get_personal_details("John", "Doe")
Student.contact_details(1234567890, 101)


#Garbge Collection in Python
#Garbage collection is the process of automatically freeing up memory that is no longer in use by the program.
# In Python, garbage collection is handled by the built-in garbage collector, which uses reference counting and cyclic garbage collection to manage memory.

# how to grabge collection works in python:
# 1. Reference Counting: Python uses reference counting to keep track of the number of references to an object. When an object's reference count drops to zero, it is automatically deallocated and its memory is freed.
# 2. Cyclic Garbage Collection: In some cases, objects can reference each other in a cycle, which can lead to memory leaks. To address this issue, Python's garbage collector includes a cyclic garbage collection mechanism that detects and collects objects that are part of reference cycles.
# 3. Generational Garbage Collection: Python's garbage collector also uses a generational approach to optimize the collection process. Objects are categorized into three generations based on their age, and the garbage collector focuses on collecting younger objects more frequently, as they are more likely to be short-lived.   

# how to garabge collection works flowchart:
# 1. Object Creation: When an object is created, it is allocated memory and its reference count is set to 1.
# 2. Reference Counting: Each time a reference to the object is created, the reference count is incremented. Each time a reference is deleted or goes out of scope, the reference count is decremented.
# 3. Garbage Collection: When the reference count of an object drops to zero, it    is considered garbage and is automatically deallocated. The memory occupied by the object is freed and can be reused for new objects.
# 4. Cyclic Garbage Collection: If there are objects that reference each other in a cycle, the garbage collector detects this and collects the objects involved in the cycle, freeing their memory.         
