#Queue is a linear data structure that follows the First In First Out (FIFO) principle.
# It is used to store a collection of elements, where the first element added is the first one to be removed.
#Queue operations include enqueue (adding an element to the rear of the queue), dequeue (removing the front element from 
#the queue), peek (viewing the front element without removing it), isEmpty (checking if the queue is empty), isFull (checking 
#if the queue is full), clear (removing all elements from the queue), and display (showing all elements in the queue).
#Queue can be implemented using a list/array or a linked list. In the case of a queue with a size limit, we need to check if 
# the queue is full before enqueuing an element and check if it is empty before dequeuing an element. The time complexity of queue 
# operations is O(1) for enqueue, dequeue, peek, isEmpty, and isFull, while the display operation has a time complexity of O(n) where n 
# is the number of elements in the queue. 

# """Simple fixed-size queue implementation with optional interactive menu.

# This file adds type hints so Pylance can infer parameter types.
# """

# from typing import Any, List


# class Queue:
#     def __init__(self, size: int) -> None:
#         self._data: List[Any] = []
#         self._size: int = int(size)

#     def is_full(self) -> bool:# method to check if the queue is full
#         return len(self._data) >= self._size# method to check if the queue is empty

#     def is_empty(self) -> bool:# method to check if the queue is empty
#         return len(self._data) == 0 # method to add an element to the rear of the queue. Returns False when full.

#     def enqueue(self, value: Any) -> bool:# method to add an element to the rear of the queue. Returns False when full.
#         """Add value to the rear of the queue. Returns False when full."""
#         if self.is_full():# check if the queue is full before enqueuing an element
#             return False # if the queue is full, return False
#         self._data.append(value)# if the queue is not full, add the value to the rear of the queue and return True
#         return True# method to remove and return the front element. Raises IndexError if empty.

#     def dequeue(self) -> Any: # method to remove and return the front element. Raises IndexError if empty.
#         """Remove and return the front element. Raises IndexError if empty."""# check if the queue is empty before dequeuing an element
#         if self.is_empty():# if the queue is empty, raise an IndexError
#             raise IndexError("dequeue from empty queue")# if the queue is not empty, remove and return the front element
#         return self._data.pop(0)# method to view the front element without removing it. Raises IndexError if empty.

#     def peek(self) -> Any:# method to view the front element without removing it. Raises IndexError if empty.
#         if self.is_empty():# check if the queue is empty before peeking at the front element
#             raise IndexError("peek from empty queue")# if the queue is empty, raise an IndexError 
#         return self._data[0]# if the queue is not empty, return the front element without removing it 

#     def clear(self) -> None:# method to remove all elements from the queue
#         self._data.clear()# method to show all elements in the queue

#     def as_list(self) -> List[Any]:# method to show all elements in the queue
#         return list(self._data) # return a copy of the queue's data as a list


# def main() -> None:# simple interactive menu to demonstrate the Queue class
#     try:# get the size of the queue from user input, ensuring it's a positive integer
#         size: int = int(input("Enter the size of the queue: "))# check if the size is positive
#         if size <= 0:# if the size is not positive, print an error message and exit
#             print("Size must be positive")# if the size is not positive, print an error message and exit
#             return 
#     except ValueError:# if the input is not a valid integer, print an error message and exit
#         print("Invalid size")# if the input is not a valid integer, print an error message and exit
#         return # create a Queue instance with the specified size

#     q: Queue = Queue(size)# interactive menu loop

#     menu = (
#         "\n1. Enqueue",
#         "2. Display",
#         "3. Dequeue",
#         "4. Peek",
#         "5. Clear queue",
#         "6. Exit",
#     )

#     while True:# display the menu and get user choice
#         for line in menu:# print the menu options
#             print(line)# get the user's choice and handle invalid input
#         try:# get the user's choice and handle invalid input
#             choice: int = int(input("Enter your choice: "))# get the user's choice and handle invalid input
#         except ValueError:# if the input is not a valid integer, print an error message and continue to the next iteration of the loop
#             print("Please enter a number between 1 and 6")# if the input is not a valid integer, print an error message and continue to the next iteration of the loop
#             continue# handle the user's choice and perform the corresponding queue operations

#         if choice == 1:# enqueue a value entered by the user, trying to convert it to an integer if possible
#             raw = input("Value to enqueue: ")# get the value to enqueue from user input
#             # try to convert to int, otherwise keep string
#             try:# try to convert the input value to an integer, if it fails, keep it as a string
#                 value: Any = int(raw)# try to convert the input value to an integer, if it fails, keep it as a string
#             except ValueError:# if the input value cannot be converted to an integer, keep it as a string
#                 value = raw# enqueue the value and print the result, checking if the queue is full before enqueuing
#             if q.enqueue(value):# enqueue the value and print the result, checking if the queue is full before enqueuing
#                 print("Enqueued:", value)# enqueue the value and print the result, checking if the queue is full before enqueuing
#             else:# if the queue is full, print a message indicating that the queue is full
#                 print("Queue is full")# if the queue is full, print a message indicating that the queue is full

#         elif choice == 2:# display the contents of the queue
#             print("Queue contents:", q.as_list())# display the contents of the queue by calling the as_list method to get a list representation of the queue's data and printing it

#         elif choice == 3:# dequeue an element from the queue and print it, handling the case where the queue is empty
#             try:
#                 print("Dequeued:", q.dequeue())# dequeue an element from the queue and print it, handling the case where the queue is empty by catching the IndexError and printing the error message
#             except IndexError as exc:
#                 print(exc)

#         elif choice == 4:# peek at the front element of the queue and print it, handling the case where the queue is empty
#             try:
#                 print("Front element:", q.peek())# peek at the front element of the queue and print it, handling the case where the queue is empty by catching the IndexError and printing the error message
#             except IndexError as exc:
#                 print(exc)

#         elif choice == 5:# clear the queue and print a message indicating that the queue has been cleared
#             q.clear()
#             print("Queue cleared")# clear the queue and print a message indicating that the queue has been cleared

#         elif choice == 6:# exit the program by breaking out of the loop and printing an exit message
#             print("Exiting")
#             break

#         else:
#             print("Invalid option, try again")# if the user's choice does not match any of the valid options, print an error message and continue to the next iteration of the loop


# if __name__ == "__main__":# if this script is run directly, call the main function to start the interactive menu
#     main()# if this script is run directly, call the main function to start the interactive menu


#what is Diffference between Stack and Queue?
# Stack is a linear data structure that follows the Last In First Out (LIFO) principle
# Queue is a linear data structure that follows the First In First Out (FIFO) principle

#whjat is Diffference between list And Linked list?
# List is a collection of elements that are stored in contiguous memory locations, while a linked list is a collection of elements 
# where each element (node) contains a reference (pointer) to the next element in the list.
# List allows for fast access to elements by index, while a linked list requires traversal from the head to access a specific element.

# Stack using list
# Easy to implement using a list, but can be inefficient for large stacks due to resizing.
# speed problem when is Growning the stack, as it may require copying all elements to a new list.
# 
# Stack using linked list
# fast preformance for push and pop operations, as it does not require resizing.    
# Implemented is not easy as using a list, as it requires defining a Node class and managing pointers.


# fruit = {}# create an empty dictionary to store the count of each fruit
# def addone(index):
#   if index in fruit:
#     fruit[index] += 1
#   else:
#     fruit[index] = 1

# addone("apple")
# addone("banana")
# addone("apple")
# print(len(fruit)) # shows {'apple': 2, 'banana': 1}
# Output: 2, because there are two unique fruits in the dictionary: "apple" and "banana". The count of "apple" is 2, and the count of "banana" is 1, but the length of the dictionary only counts unique keys, not their values. 
