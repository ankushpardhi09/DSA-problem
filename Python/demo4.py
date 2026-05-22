#consider graph as a dictionary

#A------B
#|      |
#|      |
#C------D

#connections
#A <--> B
#A <--> C
#B <--> D
#C <--> D


#Adjecency matrix representation of the graph:
#   A  B  C  D
#A  0  1  1  0  
#B  1  0  0  1
#C  1  0  0  1
#D  0  1  1  0


# class Graph:
#     def __init__(self,vertices):
#         self.v = vertices

#         self.graph = [[0 for _ in range(vertices)] 
#                       for _ in range(vertices)]
#     def add_edge(self,u,v):
#         self.graph[u][v] = 1
#         self.graph[v][u] = 1

#     def remove_edge(self,u,v):
#         self.graph[u][v] = 0
#         self.graph[v][u] = 0

#     def display(self):
#         for row in self.graph:
#             print(row)

# g = Graph(4)
# g.add_edge(0,1)
# g.add_edge(0,2)
# g.add_edge(1,3)
# g.add_edge(2,3)
# g.remove_edge(0,1)
# print("Graph after adding edges and removing edge between 0 and 1:")
# g.display()


from collections import Counter

def missingNumbers(arr, brr):
    count_a = Counter(arr)
    count_b = Counter(brr)
    
    missing = []
    
    for num in count_b:
        if count_b[num] > count_a.get(num, 0):
            missing.append(num)
            
    return sorted(missing)
