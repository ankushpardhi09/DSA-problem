# What is Graph Short and Easy: Gra
# Graph is a non-linear data structure that consists of a set of nodes (also called vertices) and a set of edges that connect pairs of nodes. 
# It is used to represent relationships between different entities. Graphs can be directed (where edges have a direction) or undirected
#  (where edges do not have a direction). They are commonly used in various applications such as social networks, transportation networks, 
# and computer networks.

# Example of a Graph is use in Real Life:
# 1. Social Networks: In social media platforms like Facebook or Twitter, users are represented as nodes, and the connections between them (friendships, followers) are represented as edges. This allows for the analysis of social interactions and the spread of information.
# 2. Transportation Networks: In transportation systems, cities or locations can be represented as nodes, and the roads or routes connecting them can be represented as edges. This helps in route planning and traffic management.
# 3. Computer Networks: In computer networks, devices such as computers, routers, and servers are represented as nodes, and the connections between them (wired or wireless) are represented as edges. This allows for the analysis of data flow and network performance.   

# tyoe of Graph:
# 1. Directed Graph (Digraph): In a directed graph, edges have a direction
# i.weighted directed graph: In a weighted directed graph, edges have both a direction and a weight (or cost) associated with them. The weight can represent various attributes such as distance, time, or capacity. This type of graph is commonly used in applications like transportation networks, where the weight can represent the distance between two locations or the time it takes to travel from one node to another.
# ii. Unweighted directed graph: In an unweighted directed graph, edges have a direction but do not have any associated weight. This type of graph is often used to represent relationships or connections between entities without considering any specific attributes. For example, in a social network, the edges can represent friendships or followers without assigning any weight to those connections.

# 2. Undirected Graph: In an undirected graph, edges do not have a direction
# i. Weighted undirected graph: In a weighted undirected graph, edges do not have a direction but have an associated weight (or cost). The weight can represent attributes such as distance, time, or capacity. This type of graph is commonly used in applications like transportation networks, where the weight can represent the distance between two locations or the time it takes to travel from one node to another.
# ii. Unweighted undirected graph: In an unweighted undirected graph, edges do not have a direction and do not have any associated weight. This type of graph is often used to represent relationships or connections between entities without considering any specific attributes. For example, in a social network, the edges can represent friendships or followers without assigning any weight to those connections.

# unweighted directed graph
# unweighted undirected graph
# positive weighted directed graph
# positive weighted undirected graph
# negative weighted directed graph
# negative weighted undirected graph

# Undirected Graph , unweighted
#A-------B
#|\       \
#| \       E
#|  \      /
#|   \    /    
#C----D--/

# Adjaceny Matrix: An adjacency matrix is a square matrix or you can say 2D array .
# And the elements of the matrix indicate whether pairs of vertices are adjacent or not in the graph.

# Adjacency Matrix for the above graph:
#     A  B  C  D  E
# A [ 0, 1, 1, 1, 0 ]
# B [ 1, 0, 0, 0, 1 ]
# C [ 1, 0, 0, 1, 0 ]
# D [ 1, 0, 1, 0, 1 ]
# E [ 0, 1, 0, 1, 0 ]

# Adjacency List: An adjacency list is a collection of lists or arrays where each list corresponds to a vertex in the graph and contains the adjacent vertices (neighbors) of that vertex.
# Adjacency List for the above graph:

# A: [B, C, D]  
# B: [A, E]
# C: [A, D]
# D: [A, C, E]
# E: [B, D]

#How we choose Adjacency Matrix or Adjacency List in simaple words:
#if a Graph is Complete or Almost complete then we choose Adjacency Matrix.
#On the other hand, if the egdes are few then we choose should Adjacency List.

# we have use in dictionary to represent the graph in python because it allows us to easily store and access the vertices and their corresponding edges.
# In a graph, we can represent the vertices as keys in the dictionary and the edges as values associated with those keys. This allows us to efficiently store and retrieve the connections between vertices in the graph.



class Graph:
    def __init__(self):
        self.adjacency_list: dict[str, list[str]] = {}

    def add_vertex(self, vertex: str) -> bool:
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            return True
        return False
    
    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])

    def egde(self, vertex1: str, vertex2: str) -> bool:
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:# check if both vertices exist in the graph
            self.adjacency_list[vertex1].append(vertex2)# add vertex2 to the adjacency list of vertex1
            self.adjacency_list[vertex2].append(vertex1)# add vertex1 to the adjacency list of vertex2 (since it's an undirected graph)
            return True# if the edge was successfully added
        return False# if either vertex1 or vertex2 does not exist in the graph, return False
    
    def add_edges(self, vertex1: str, vertex2: str) -> bool:
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:# check if both vertices exist in the graph
            self.adjacency_list[vertex1].append(vertex2)# add vertex2 to the adjacency list of vertex1
            return True# if the edge was successfully added
        return False# if either vertex1 or vertex2 does not exist in the graph, return False
    
    def remove_edge(self, vertex1: str, vertex2: str) -> bool:
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:# check if both vertices exist in the graph
            if vertex2 in self.adjacency_list[vertex1]:# check if vertex2 is in the adjacency list of vertex1
                self.adjacency_list[vertex1].remove(vertex2)# remove vertex2 from the adjacency list of vertex1
            if vertex1 in self.adjacency_list[vertex2]:# check if vertex1 is in the adjacency list of vertex2
                self.adjacency_list[vertex2].remove(vertex1)# remove vertex1 from the adjacency list of vertex2 (since it's an undirected graph)
            return True# if the edge was successfully removed
        return False# if either vertex1 or vertex2 does not exist in the graph, return False
    
        
my_graph = Graph()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")
my_graph.add_vertex("E")  
print("Graph after adding vertices:")
my_graph.egde("A", "B")
my_graph.egde("A", "C")
my_graph.egde("A", "D")
my_graph.egde("B", "E")
my_graph.egde("C", "D")
my_graph.egde("D", "E")
my_graph.print_graph()
print("Graph after adding edges:", my_graph.add_edges("A", "E"))
my_graph.print_graph()
my_graph.remove_edge("A", "B")
print("Graph after removing edge between A and B:")
my_graph.print_graph()



