class Node:
    def __init__(self, data):#constructor to initialize the node with data and next pointer
        self.data = data
        self.next = None
class LinkedList:#class to represent the linked list
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):#method to add a node at the end of the linked list
        new_node = Node(data)
        if not self.head:#if the linked list is empty, set the new node as head and tail
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def print_list(self):#method to print the linked list
        current_node = self.head
        while current_node:#traverse the linked list and print each node's data
            print(current_node.data)
            current_node = current_node.next

    def between(self, data, position):#method to add a node at a specific position in the linked list
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current_node = self.head
        for _ in range(position - 1):#traverse the linked list to find the node at the specified position
            if current_node is None:#if the position is out of bounds, raise an error
                raise IndexError("Position out of bounds")
            current_node = current_node.next

        new_node.next = current_node.next#set the next pointer of the new node to the next node of the current node
        current_node.next = new_node #set the next pointer of the current node to the new node

    def beginning(self, data):#method to add a node at the beginning of the linked list
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def addEnd(self, data):#method to add a node at the end of the linked list
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node
    
    def delete(self, data):#method to delete a node with the specified data from the linked list
        current_node = self.head
        previous_node = None

        while current_node:
            if current_node.data == data:#if the node to be deleted is found
                if previous_node:
                    previous_node.next = current_node.next #set the next pointer of the previous node to the next node of the current node
                else:
                    self.head = current_node.next #if the node to be deleted is the head, set the head to the next node

                if current_node == self.tail:#if the node to be deleted is the tail, update the tail pointer
                    self.tail = previous_node
                return

            previous_node = current_node
            current_node = current_node.next


if __name__ == "__main__":
    linked_list = LinkedList()
    while True:
        print("1. Add node Linked List :")
        print("2. Add node in beginning of Linked List :")
        print("3. Add node in end of Linked List :")
        print("4. Add node in between of Linked List :")
        print("5. Delete node from Linked List :")
        print("6. Print Linked List :")
        print("7. Exit :")
        choice = int(input("Enter your choice : "))
        if choice == 1:
            data = int(input("Enter data to add : "))
            linked_list.append(data)
        elif choice == 2:
            data = int(input("Enter data to add : "))
            linked_list.beginning(data)
        elif choice == 3:
            data = int(input("Enter data to add : "))
            linked_list.addEnd(data)
        elif choice == 4:   
            data = int(input("Enter data to add : "))
            position = int(input("Enter position to add : "))   
            linked_list.between(data, position)
        elif choice == 5:
            data = int(input("Enter data to delete : "))
            # linked_list.delete(data)
        elif choice == 6:
            linked_list.print_list()
        elif choice == 7:
            break
        else:
            print("Invalid choice !")
        
        
        