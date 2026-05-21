#types of binary tree
#      1    
#     / \
#    2   3
#   / \   \
#  4   5   6

#1. Full Binary Tree: A full binary tree is a binary tree in which every node has either 0 or 2 children. In the above example, the nodes 1, 2, and 3 are full nodes, while nodes 4, 5, and 6 are leaf nodes.
#2. Complete Binary Tree: A complete binary tree is a binary tree in which all levels are completely filled except possibly the last level, which is filled from left to right. In the above example, the tree is a complete binary tree because all levels are filled except for the last level, which is filled from left to right.
#3. Perfect Binary Tree: A perfect binary tree is a binary tree in which all internal nodes have exactly two children and all leaf nodes are at the same level. In the above example, the tree is not a perfect binary tree because node 3 has only one child (node 6).
#4. Balanced Binary Tree: A balanced binary tree is a binary tree in which the difference in height between the left and right subtrees of any node is no more than one. In the above example, the tree is a balanced binary tree because the height difference between the left and right subtrees of each node is at most one.
#5. Binary Search Tree (BST): A binary search tree is a binary tree in which the value of each node is greater than the values of all nodes in its left subtree and less than the values of all nodes in its right subtree. In the above example, the tree is not a binary search tree because node 2 is less than node 1, but it is in the left subtree of node 1.

#Full Binary tree
#Each node has either 0 or 2 children
#no node has a single child
#           1
#         /   \
#        2     3
#      /    \
#    4      5   
#  / \     / \
# 6   7    8  9

#Complete Binary Tree
#All levels are completely filled except possibly the last level, which is filled from left to right
#           1
#         /   \
#        2     3
#      /   \
#     4     5

#Perfect Binary Tree
#All internal nodes have exactly two children and all leaf nodes are at the same level
#           1
#         /    \
#        2      3
#      /   \   /  \
#     4     5 6    7

#Balanced Binary Tree
#The difference in height between the left and right subtrees of any node is no more than one
#           1
#         /   \
#        2     3
#      /   \
#     4     5

# types of traversal in binary tree
#            1
#         /    \
#        2      3
#      /   \   /  \
#     4     5 6    7

#1. Inorder Traversal: In this traversal method, the nodes are visited in the
#following order: left subtree, root node, right subtree. For the above example, the inorder traversal would be: 4, 2, 5, 1, 3, 6.
#2. Preorder Traversal: In this traversal method, the nodes are visited in the 
#following order: root node, left subtree, right subtree. For the above example, the preorder traversal would be: 1, 2, 4, 5, 3, 6.
#3. Postorder Traversal: In this traversal method, the nodes are visited in the
#following order: left subtree, right subtree, root node. For the above example, the postorder traversal would be: 4, 5, 2, 6, 3, 1.

# tyes of tree Serach
#1. Breadth-First Search (BFS): In this search method, the algorithm explores all the nodes at the present depth level before moving on 
# to the nodes at the next depth level. It can be implemented using a queue data structure. BFS is useful for finding the shortest path 
# between two nodes in a tree or for traversing all nodes in a tree level by level.
#Example of BFS traversal for the above tree would be: 1, 2, 3, 4, 5, 6, 7.

#2. Depth-First Search (DFS): In this search method, the algorithm explores as far down a branch of the tree as possible before backtracking. 
# It can be implemented using recursion or a stack data structure. DFS is useful for searching for a specific value in a tree or for traversing all nodes in a tree.
#Example of DFS traversal for the above tree would be: 1, 2, 4, 5, 3, 6, 7.

# Insertion node to a binary Search Tree (BST)
# Algorithm:
#Check if uf the corrent node is the root node or not
# If the current node is null, create a new node with the value to be inserted and return it as the new root of the subtree.
# 1. Start at the root node.
# 2. Compare the value to be inserted with the value of the current node.
# 3. If the value to be inserted is less than the value of the current node, 
# move to the left child of the current node. If the left child is null, insert the new value as the left child. 
# Otherwise, repeat steps 2 and 3 with the left child as the current node.
# 4. If the value to be inserted is greater than the value of the current node,
# move to the right child of the current node. If the right child is null, insert the new value as the right child.
# Otherwise, repeat steps 2 and 3 with the right child as the current node.

class BSTNode:# class for Binary Search Tree Node
    def __init__(self, data):# constructor to initialize the node with data and set left and right child to None
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insertNode(rootNode , nodeValue):# function to insert a new node with the given value into the binary search tree
    if rootNode.data is None:# if the current node is null, create a new node with the value to be inserted and return it as the new root of the subtree.
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:# compare the value to be inserted with the value of the current node. If the value to be inserted is less than or equal to the value of the current node, move to the left child of the current node.
        if rootNode.leftChild is None:# If the left child is null, insert the new value as the left child. Otherwise, repeat steps 2 and 3 with the left child as the current node.
            rootNode.leftChild = BSTNode(nodeValue)
        else:# If the left child is not null, repeat steps 2 and 3 with the left child as the current node.
            insertNode(rootNode.leftChild, nodeValue)
    else:# If the value to be inserted is greater than the value of the current node, move to the right child of the current node. If the right child is null, insert the new value as the right child. Otherwise, repeat steps 2 and 3 with the right child as the current node.
        if rootNode.rightChild is None:# If the right child is null, insert the new value as the right child. Otherwise, repeat steps 2 and 3 with the right child as the current node.
            rootNode.rightChild = BSTNode(nodeValue)
        else:# If the right child is not null, repeat steps 2 and 3 with the right child as the current node.
            insertNode(rootNode.rightChild, nodeValue)
    
def PreOrderTraversal(rootNode):# function to perform a preorder traversal of the binary search tree
    if rootNode is not None:# If the current node is not null, visit the root node, then recursively traverse the left subtree, and finally recursively traverse the right subtree.
        print(rootNode.data)# visit the root node
        PreOrderTraversal(rootNode.leftChild)# recursively traverse the left subtree
        PreOrderTraversal(rootNode.rightChild)# recursively traverse the right subtree

def inorderTraversal(rootNode):# function to perform an inorder traversal of the binary search tree
    if rootNode is not None:# If the current node is not null, recursively traverse the left subtree, visit the root node, and finally recursively traverse the right subtree.
        inorderTraversal(rootNode.leftChild)# recursively traverse the left subtree
        print(rootNode.data)# visit the root node
        inorderTraversal(rootNode.rightChild)# recursively traverse the right subtree

def postorderTraversal(rootNode):# function to perform a postorder traversal of the binary search tree
    if rootNode is not None:# If the current node is not null, recursively traverse the left subtree, then recursively traverse the right subtree, and finally visit the root node.
        postorderTraversal(rootNode.leftChild)# recursively traverse the left subtree
        postorderTraversal(rootNode.rightChild)# recursively traverse the right subtree
        print(rootNode.data)# visit the root node

def searchNode(rootNode, nodeValue):# function to search for a node with the given value in the binary search tree
    if rootNode is None:# Stop when the subtree is empty.
        print("Value Not found in the Tree",nodeValue)
    elif rootNode.data == nodeValue:# If the current node's value matches the value being searched for, return True.
        print("Value found in the tree",nodeValue)
    elif nodeValue < rootNode.data:# If the value being searched for is less than the current node's value, recursively search the left subtree.
        searchNode(rootNode.leftChild, nodeValue)
    else:# If the value being searched for is greater than the current node's value, recursively search the right subtree.
        searchNode(rootNode.rightChild, nodeValue)

#Height of a Binary Tree
def heightOfBinaryTree(rootNode):# function to calculate the height of a binary tree
    if rootNode is None:# If the current node is null, return -1 (the height of an empty tree is defined as -1).
        return -1
    else:# Otherwise, recursively calculate the height of the left and right subtrees and return the maximum of the two heights plus one (to account for the current node).
        leftHeight = heightOfBinaryTree(rootNode.leftChild)# recursively calculate the height of the left subtree
        rightHeight = heightOfBinaryTree(rootNode.rightChild)# recursively calculate the height of the right subtree
        return max(leftHeight, rightHeight) + 1# return the maximum of the two heights plus one (to account for the current node)
    


new_BST = BSTNode(None)# Object
insertNode(new_BST, 70)
insertNode(new_BST, 50)
insertNode(new_BST, 90)
insertNode(new_BST, 30)
insertNode(new_BST, 60)
insertNode(new_BST, 80)
insertNode(new_BST, 100)
insertNode(new_BST, 20)
insertNode(new_BST, 40)
insertNode(new_BST, 10)
print("Binary Search Tree created successfully")
print()
print("Preorder Traversal of the Binary Search Tree:")
PreOrderTraversal(new_BST)# Output: 70, 50, 30, 20, 10, 40, 60, 90, 80, 100
print("Inorder Traversal of the Binary Search Tree:")
inorderTraversal(new_BST)# Output: 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
print("Postorder Traversal of the Binary Search Tree:")
postorderTraversal(new_BST)# Output: 10, 20, 40, 30, 60, 50, 80, 100, 90, 70  
print("Search for a value in the Binary Search Tree:")
searchNode(new_BST, 70)# Output: Value found in the tree
searchNode(new_BST, 25)# Output: Value Not found in the Tree
print("Height of the Binary Search Tree:")
print(heightOfBinaryTree(new_BST))# Output: 3








