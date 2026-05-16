#Stack is a data structure that follows the Last In First Out (LIFO) principle. It is used to store a collection of elements, where the last element added is the first one to be removed.
#Stack operations include push (adding an element to the top of the stack), pop (removing the top element from the stack), peek (viewing the top element without removing it), isEmpty (checking if the stack is empty), isFull (checking if the stack is full), delete (removing all elements from the stack), and display (showing all elements in the stack).
#Stack can be implemented using a list/array or a linked list. In the case of a stack with a size limit, we need to check if the stack is full before pushing an element and check if it is empty before popping an element. The time complexity of stack operations is O(1) for push, pop, peek, isEmpty, and isFull, while the display operation has a time complexity of O(n) where n is the number of elements in the stack.    

#input = 8
# 79 77 54 81 48 34 25 16 
# output  = 3
#Explaination : the areas that in squere form are 81 , 25 and 16 so the output is 3

# write a program to find the number of perfect square in the given list of numbers


# def func(valus, values):
#     var = 1
#     values[0] = 44
# t =3
# v = [1,2,3,4,5]
# func(t,v)
# print(t, v[0])

#Explaintatioln : in the above code we have a function func which takes two parameters valus and values.
#when we call the function func(t,v) it will change the value of t to 1 and the first element of the list v to 44.
#so the output will be 3 44


#Question : what will be the output of the following code and explain it.
# def func(i ,values = []): # type: ignore
#     values.append(i) # type: ignore
#     print(values) # type: ignore
# func(1)
# func(2)
# func(3)
#Explaintation : in the above code we have a function func which takes two parameters i and values.
#when we call the function func(1) it will append the value 1 to the list values and print the list.
#when we call the function func(2) it will append the value 2 to the list values and print the list.
#when we call the function func(3) it will append the value 3 to the list values and print the list.
#so the output will be [1] [1, 2] [1, 2, 3] 



#How to Stack can be implemented using a list or linked list in python?
#Stack can be implemented using a list in python by using the built-in list data structure. 
#Here is an example of a stack implementation using a list:
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return "Stack is empty"

    def isEmpty(self):
        return len(self.stack) == 0

    def display(self):
        print(self.stack)
