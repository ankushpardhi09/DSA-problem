# Queue implementation using linked list

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
    
class LinkedList:# class to create a linked list
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
         currNode = self.head
         while currNode:
                yield currNode
                currNode = currNode.next

class Queue:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return "\n".join(values)
    
    def isEmpty(self):
        return self.LinkedList.head is None
    
    def enqueue(self, value):
        newNode = Node(value)
        if self.LinkedList.head is None:
            self.LinkedList.head = newNode
            self.LinkedList.tail = newNode
        else:
            self.LinkedList.tail.next = newNode
            self.LinkedList.tail = newNode

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue
        
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.LinkedList.head.value

    def dequeue (self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            if self.LinkedList.head is None:  # If the queue becomes empty after dequeue
                self.LinkedList.tail = None  # Set tail to None as well
            return nodeValue
        
    
        

customQueue = Queue()
customQueue.enqueue(1)  
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)
print("Dequeued:", customQueue.dequeue())
print(customQueue)
print("Peek:", customQueue.peek())
print("Dequeued:", customQueue.dequeue())
print(customQueue)  

