#sort dictionary by key a value

#write a program to sort a dictionary by key and value in ascending and descending order
#using sorted() function

#sort by key in ascending order
my_dict = {'c': 3, 'a': 1, 'd': 4 , 'e': 5 , 'b': 2}
sorted_dict = dict(sorted(my_dict.items()))
print("Sorted by key in ascending order:", sorted_dict)
#sort by key in descending order
sorted_dict_desc = dict(sorted(my_dict.items(), reverse=True))
print("Sorted by key in descending order:", sorted_dict_desc)
