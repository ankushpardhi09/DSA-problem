#maximum number of conseucetive ones in a binary array
# arr ={1,1,0,1,1,1,0,1,1,1,} #output = 4
# max_count = 0
# current_count = 0   
# for num in arr:
#     if num == 1:
#         current_count += 1
#     else:
#         max_count = max(max_count, current_count)
#         current_count = 0

# max_count = max(max_count, current_count) #to check the last count of ones
# print(max_count)    


# # count the number of occurences of a substring in aa given string
# s = "abababab"
# substring = "aba"
# count = 0
# for i in range(len(s) - len(substring)+1):
#     if s[i:i+len(substring)] == substring:
#         count += 1
# print(count)    
