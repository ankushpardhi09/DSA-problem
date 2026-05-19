#What is Tree?
#A tree is a data structure that consists of nodes connected by edges. It is a hierarchical structure that represents relationships between 
#different elements. Each node in a tree can have zero or more child nodes, and there is one node called the root that serves as the starting 
#point of the tree.

#tree use recursion to traverse the tree and perform operations on its nodes. 

#Are Represent By Double linked list and array
#Types of Tree
#1. Binary Tree: A tree where each node has at most two children, referred to as the left child and the right child.
#2. Binary Search Tree (BST): A binary tree where the value of each node is greater than the values of its left subtree and less than the values of its right subtree.
#3. AVL Tree: A self-balancing binary search tree where the difference in heights between the left and right subtrees cannot be more than one for any node.
#4. Red-Black Tree: A self-balancing binary search tree where each node has an additional color attribute (red or black) to ensure balance.
#5. B-Tree: A self-balancing tree data structure that maintains sorted data and allows for efficient insertion, deletion, and search operations. It is commonly used in databases and file systems.
#6. Trie: A tree-like data structure used to store a dynamic set of strings,where each node represents a common prefix of the strings. It is often used for efficient retrieval of strings based on their prefixes.     

#python list can be used to implement a tree data structure.
#Are store data in a first right side of node and then left side of node
#Example of a binary tree using a list:
# A binary tree represented as a list
# The index of the left child of a node at index i is 2*i + 1
# The index of the right child of a node at index i is 2*i + 2
# Example binary tree represented as a list
#         1 
#        / \
#       2   3
#      / \
#     4   5
# The binary tree can be represented as a list as follows:
# tree = [1, 2, 3, 4, 5]

#python Array can be used to implement a tree data structure.
# are store data in a first right side of node and then left side of node
# Example of a binary tree using an array:
# A binary tree represented as an array
# The index of the left child of a node at index i is 2*i + 1
# The index of the right child of a node at index i is 2*i + 2
# Example binary tree represented as an array
#         1
#        / \
#       2   3
#      / \
#     4   5
# The binary tree can be represented as an array as follows:
# tree = [1, 2, 3, 4, 5]


#Tree Cerate with the use of class and object
# class Tree:
#     def __init__(self, data):
#         self.data = data
#         self.child = []

#     def __str__(self, left = 0):
#             result = " " * left + str(self.data) + "\n"
#             for child in self.child:
#                 result += child.__str__(left + 4)
#             return result


#     def add_child(self, object):
#         self.child.append(object)
#         print("Child added successfully")

# rootNOde = Tree("Drinks")
# Hot = Tree("Hot")
# Cold = Tree("Cold")
# Tea = Tree("Tea")
# Coffee = Tree("Coffee")
# NonAlocholic = Tree("NonAlochol")
# Alcoholic = Tree("Alcoholic")

# rootNOde.add_child(Hot)#Adding the "Hot" node as a child of the "Drinks" root node.
# rootNOde.add_child(Cold)#Adding the "Cold" node as a child of the "Drinks" root node.
# Hot.add_child(Tea)#Adding the "Tea" node as a child of the "Hot" node.
# Hot.add_child(Coffee)#Adding the "Coffee" node as a child of the "Hot" node.
# Cold.add_child(NonAlocholic)#Adding the "NonAlcoholic" node as a child of the "Cold" node.
# Cold.add_child(Alcoholic)#Adding the "Alcoholic" node as a child of the "Cold" node.

# print(rootNOde)


# class Tree:
#     def __init__(self, data):
#         self.data = data
#         self.child = []

#     def __str__(self, left = 0):
#             result = " " * left + str(self.data) + "\n"
#             for child in self.child:
#                 result += child.__str__(left + 4)
#             return result


#     def add_child(self, object):
#         self.child.append(object)
#         print("Child added successfully")

# rootNOde = Tree("N1")
# N2 = Tree("N2")
# N3 = Tree("N3")
# N4 = Tree("N4")
# N5 = Tree("N5")
# N6 = Tree("N6")
# N7 = Tree("N7")
# N8 = Tree("N8")

# rootNOde.add_child(N2)
# rootNOde.add_child(N3)
# N2.add_child(N4)
# N2.add_child(N5)
# N3.add_child(N6)
# N4.add_child(N7)
# N4.add_child(N8)


# print(rootNOde)

# Creation                TC: O(1) , SC: O(1)
# Insertion               TC: O(n) , SC: O(1)
# Deletion of a node      TC: O(n) , SC: O(1)
# Serching                TC: O(n) , SC: O(1)
# traversal               TC: O(n) , SC: O(1)
# Deletion of Linked List TC: O(1) , SC: O(1)


