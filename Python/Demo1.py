class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
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
            linked_list.append(data)    
        elif choice == 3:
            data = int(input("Enter data to add : "))
            linked_list.append(data)
        elif choice == 4:   
            data = int(input("Enter data to add : "))
            linked_list.append(data)
        elif choice == 5:
            data = int(input("Enter data to delete : "))
            # linked_list.delete(data)
        elif choice == 6:
            linked_list.print_list()
        elif choice == 7:
            break
        else:
            print("Invalid choice !")
        
        
        