#Data structures are different ways of organizing data on your computer that can be used efficiently.
#Some common data structures include lists, tuples, sets, and dictionaries.

#Algorithme : A step-by-step procedure for solving a problem or performing a task. It is a set of instructions that can be followed to achieve a specific goal.
#Algorithms are used in computer science to design efficient and effective solutions to problems. They can be implemented in various programming languages and 
#can be used for a wide range of applications, such as sorting, searching, and data manipulation.

# two steps to check : 1: correctness of the algorithm, 2: efficiency of the algorithm

# Data processing: is the process of collecting as input, proccesing, and outputting data.
# It involves transforming raw data into a more useful format, such as a report or a visualization.
# Data processing can be done manually or using automated tools and software. It is an essential step in the 
# data analysis process, as it allows us to extract insights and make informed decisions based on the data.

# Time complexity: is a measure of the amount of time an algorithm takes to run as a function of the size of the input.
 
# It is usually expressed using Big O notation, which describes the upper bound of the growth rate of the algorithm's running time.

#worst case time complexity: is the maximum amount of time an algorithm takes to run for any input of a given size. 
# It represents the upper bound of the running time and is denoted as O(f(n)), where f(n) is a function that describes the growth 
# rate of the running time as the input size increases.

# best case time complexity: is the minimum amount of time an algorithm takes to run for any input of a given size.
# It represents the lower bound of the running time and is denoted as Ω(f(n)),
# where f(n) is a function that describes the growth rate of the running time as the input size increases.

#Time complexity types
# O(1) = constant = Accessing an element in an array by index
#O(1) Constant time Ex: arrary = {1,2,3,4,5}  ,  arrary[0] // It takes constant time to access the first element of the array, regardless of the size of the array.

# O(n) = linear = Traversing a list to find a specific element(loop though array element)
# Example: arrary = {1,2,3,4,5}  ,  for i in arrary: if i == 3: print("found") // It takes linear time to find the element 3 in the array, as we may have to check each element until we find it.

# O(n^2) = Quadratic = Nested loops, such as a loop inside another loop, where the number of iterations is proportional to the square of the input size.
# Example: arrary = {1,2,3,4,5}  ,  for i in arrary: for j in arrary: print(i,j) // It takes quadratic time to print all pairs of elements in the array, as we have to check each element against every other element.

# O(log n) = logrithmic = Examaple is Binary search algorithm, where the search space is halved with each iteration.(find an element in a sorted array)
#Example: arrary = {1,2,3,4,5}  ,  binary_search(arrary, 3) // It takes logarithmic time to find the element 3 in the sorted array using binary search, as we can eliminate half of the remaining elements with each comparison.

# O(n 2^n) = Exponential = Recursive algorithms that generate all possible combinations of a set, such as the power set of a set with n elements.
#Example: arrary = {1,2,3}  ,  power_set(arrary) // It takes exponential time to generate the power set of the array, as we have to consider all possible combinations of the elements.
#(Worst case time complexity of the power set algorithm is O(n 2^n) because we have to generate all possible subsets of the input set, which can be up to 2^n subsets, and each subset can take up to O(n) time to generate.)

# why recrtion is used in programming?
# Recursion is a programming technique where a function calls itself in order to solve a problem. It is often used to solve problems that can be broken down into smaller, similar subproblems.
# Recursion can simplify code and make it easier to read and understand. It can also be used to solve problems that are difficult to solve using iterative approaches, such as problems that involve tree or graph traversal, or 
# problems that require backtracking.


#what is Space complexity?
# Space complexity is a measure of the amount of memory an algorithm uses as a function of the size of the input. It is usually expressed using Big O notation, which describes the upper bound of the growth rate of the algorithm's memory usage. 
# Exmaple : O(1) = constant space complexity, O(n) = linear space complexity, O(n^2) = quadratic space complexity, O(log n) = logarithmic space complexity, O(n 2^n) = exponential space complexity.


#roe wise max valus
#[[100, 195, 234, 324],
# [122, 212, 111 , 432],    
# [211, 145, 234 , 321],]

#input = prashant*is*a*good*programmer
#output = ****prashantisgoodprogrammer

name = "prashant*is*a*good*programmer"
newname = ""
val = ""#count the number of * in the string
for i in name:
    if i == "*":
        newname += "*"
    else:
        newname += i    
print(newname)
print(str(val+newname))


#________________________________________________________

# 1.
# basicSalary = 20000

# HRA = basicSalary * 0.2
# TA = basicSalary * 0.3
# DA = basicSalary * 0.45

# print(basicSalary + HRA + TA + DA)

# 2.
# def binarySearch(array, target):
#     low = 0
#     high = len(array)-1
#     while low <= high:
#         mid = (low+high)//2
#         if array[mid] == target:
#             return mid
#         elif array[mid] < target:
#             low = mid+1
#         else:
#             high = mid-1
#     return -1

# array=[2,4,5,9,11,13,14,15,19,20,22,23,27,30,32,39,42,44,45,49,51,53,54,55,59,60,62,63,67,70,72,79]
# target = 72
# result = binarySearch(array, target)
# if result == -1:
#     print("Element not found")
# else:
#     print("Element found at ", result)

# 3.
# def bubbleSort(array):
#     for i in range(len(array)-1):
#         for j in range(len(array)-i-1):
#             if array[j] > array[j+1]:
#                 temp = array[j]
#                 array[j] =array[j+1]
#                 array[j+1] = temp
#             print(array)
#         print()
        
# array = [64, 34, 25, 12, 22, 11, 90]
# bubbleSort(array)

# 4.
# input = [5,7,8,3,7,8,9,2,3]
# dic={}
# for ele in input:
#     if ele not in dic:
#         dic[ele] = 0
#     dic[ele] += 1 
# # print (dic)
# max = 0
# for ele in dic:
#     if dic[ele] > max:
#         max = dic[ele]
# # print (max)
# ans = 0
# # elements =[]
# for ele in dic:
#     if dic[ele] == max:
#         ans += 1

# print(ans)

# mylist = [5,7,8,3,7,8,9,2,3]
# newlist =[] #7

# for i in range(len(mylist)): #i=1
#     count = 0
#     key = mylist[i] #key = 7
#     j = i+1 # j = 4
#     while j<len(mylist):
#         if key == mylist[j] : #7=7
#             newlist.append(key)
#         j = j+1
# print(len(newlist))
