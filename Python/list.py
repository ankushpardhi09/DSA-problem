#find the All Duplicates in a list 

def find_duplicates(lst):
    duplicates = []
    seen = set()
    
    for item in lst:
        if item in seen:
            if item not in duplicates:
                duplicates.append(item)
        else:
            seen.add(item)
    
    return duplicates
# Example usage
my_list = [1, 2, 3, 4, 2, 5, 1, 6]
duplicates = find_duplicates(my_list)   
print(duplicates)  # Output: [1, 2]

