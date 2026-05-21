#Stack implementation using Linked List
#stack are also implemented by using array but in that case we have to define the size of the stack and if we want to increase the size of the stack then we have to create a new array and copy the elements of the old array to the new array but in linked list we don't have to define the size of the stack and we can easily increase the size of the stack by creating a new node and linking it to the previous node.


# """Clean, minimal stack implementation using a singly-linked list.

# This module provides a small, well-documented `Stack` class with
# `push`, `pop`, `peek`, `is_empty`, `__len__` and useful dunder methods
# for iteration and string representation.

# The stack grows dynamically and does not require pre-sizing.
# """

# from typing import Any, Iterator, Optional#, overload


# class Node:
#     """A node in a singly-linked list.

#     Attributes:
#         value: Stored value.
#         next: Reference to the next node, or None.
#     """

#     __slots__ = ("value", "next")# Using __slots__ to save memory by preventing the creation of __dict__ for each instance.__slots__ is a
#     # special attribute that can be defined in a class to specify a fixed set of attributes that instances of the class will have. 
#     # By defining __slots__, we can prevent the creation of __dict__ for each instance, which can save memory when creating many instances of the class.

#     def __init__(self, value: Any, next: Optional["Node"] = None) -> None:# The constructor takes a value and an optional next node reference.
#         self.value = value
#         self.next = next

#     def __repr__(self) -> str:# The __repr__ method provides a string representation of the node for debugging purposes.
#         return f"Node({self.value!r})"


# class Stack:#
#     """A simple LIFO stack implemented with a linked list.

#     The top of the stack is the head of the linked list.
#     """

#     def __init__(self) -> None:# The constructor initializes the stack with an empty head and a size of zero.
#         self._head: Optional[Node] = None
#         self._size: int = 0

#     def is_empty(self) -> bool:
#         """Return True if the stack is empty."""
#         return self._head is None

#     def push(self, value: Any) -> None:
#         """Push `value` onto the stack."""
#         self._head = Node(value, self._head)
#         self._size += 1

#     def pop(self) -> Any:
#         """Remove and return the top value. Raises IndexError if empty."""
#         if self._head is None:
#             raise IndexError("pop from empty stack")
#         node = self._head
#         self._head = node.next
#         self._size -= 1
#         return node.value

#     def peek(self) -> Any:
#         """Return the top value without removing it. Raises IndexError if empty."""
#         if self._head is None:
#             raise IndexError("peek from empty stack")
#         return self._head.value

#     def __len__(self) -> int:
#         return self._size

#     def __iter__(self) -> Iterator[Any]:
#         """Iterate from top to bottom (LIFO order)."""
#         current = self._head
#         while current is not None:
#             yield current.value
#             current = current.next

#     def __repr__(self) -> str:
#         values = list(self)
#         return f"Stack(top->bottom): {values!r}"


# if __name__ == "__main__":
#     # Quick demonstration / smoke test
#     s = Stack()
#     s.push(1)
#     s.push(2)
#     s.push(3)
#     print(s)
#     print("Top:", s.peek())
#     print("Popped:", s.pop())
#     print("Top after pop:", s.peek())
#     print(s)


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#



# class Node:
#     def __init__(self, value = None):
#         self.value = value
#         self.next = None

#     def __str__(self):
#         values = [str(x = value) for x in self.LinkedList]
#         return "\n".join(values)

# class LinkedList:# class to create a linked list
#     def __init__(self):
#         self.head = None

# class Stack:# class to create a stack using linked list
#     def __init__(self) -> None:# constructor to initialize the stack
#         self.LinkedList = LinkedList()
    
#     def isEmpty(self):# function to check if the stack is empty
#         return self.LinkedList.head is None# return true if the head of the linked list is null, otherwise return false

#     def push(self, value):# function to push an element to the stack
#         newNode = Node(value)# create a new node with the given value
#         if self.LinkedList.head is None:# if the stack is empty, set the head of the linked list to the new node
#             self.LinkedList.head = newNode# if the stack is not empty, set the next of the new node to the current head of the linked list and then set the head of the linked list to the new node
#         else:# if the stack is not empty, set the next of the new node to the current head of the linked list and then set the head of the linked list to the new node
#             newNode.next = self.LinkedList.head# set the next of the new node to the current head of the linked list
#             self.LinkedList.head = newNode# set the head of the linked list to the new node

#     def pop(self):# function to pop an element from the stack
#         if self.isEmpty():# if the stack is empty, return a message indicating that the stack is empty
#             return "Stack is empty"
#         else:# if the stack is not empty, get the value of the current head of the linked list, set the head of the linked list to the next of the current head of the linked list, and then return the value of the current head of the linked list
#             nodeValue = self.LinkedList.head.value# get the value of the current head of the linked list
#             self.LinkedList.head = self.LinkedList.head.next# set the head of the linked list to the next of the current head of the linked list
#             return nodeValue# return the value of the current head of the linked list
    
#     def peek(self):# function to peek the top element of the stack
#         if self.isEmpty():# if the stack is empty, return a message indicating that the stack is empty
#             return "Stack is empty"
#         else:# if the stack is not empty, return the value of the current head of the linked list
#             return self.LinkedList.head.value# return the value of the current head of the linked list
        

# customStack = Stack()
# customStack.push(1)
# customStack.push(2)
# customStack.push(3)
# print(customStack)
# print("display the top element of the stack: ", customStack.peek())# Output: 3
# print("pop the top element of the stack: ", customStack.pop())# Output: 3
# print("display the top element of the stack after popping: ", customStack.peek())# Output: 2
# print(customStack)

