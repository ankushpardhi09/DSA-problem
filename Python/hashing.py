#What is hashing?
##Hashing is a technique used to uniquely identify a piece of data. 
# It is commonly used in data structures like hash tables, where it allows for efficient data retrieval. 
# A hash function takes an input (or 'key') and returns a fixed-size string of bytes, which is typically a hash code. 
# The hash code is used to index the original data in the hash table.

# what a problem solve by hasing
##Hashing can solve several problems, including:
#1. Fast data retrieval: Hashing allows for constant average time complexity for data retrieval, making it much faster than other data structures like lists or arrays.
#2. Data integrity: Hashing can be used to verify the integrity of data by generating a hash code for the original data and comparing it to a hash code generated from the retrieved data.
#3. Password storage: Hashing is commonly used to securely store passwords. Instead of storing
# the actual password, a hash of the password is stored. When a user attempts to log in, the hash of the entered password is compared to the stored hash.
#4. Caching: Hashing can be used to implement caching mechanisms, where the hash of a piece of data is used as a key to store and retrieve the data from the cache.

#linear search = O(n)
#binary search = O(log n)
#hashing = O(1) on average  


#WHta is hash function?
##A hash function is a function that takes an input (or 'key') and returns a fixed-size string of bytes, which is typically a hash code.
# The hash code is used to index the original data in a hash table.
# A good hash function should have the following properties:
#1. Deterministic: The same input should always produce the same output.
#2. Fast: The hash function should be able to compute the hash code quickly.
#3. Uniform: The hash function should distribute the hash codes uniformly across the hash table to minimize collisions (when two different inputs produce the same hash code).

#formula : index = hash(key) % table_size

#pyjhon fash function

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    self.table[index][i] = (key, value)  # Update existing key
                    return
            self.table[index].append((key, value))  # Handle collision by chaining

    def search(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None  # Key not found

# Example usage
hash_table = HashTable(10)
hash_table.insert("name", "Alice")
hash_table.insert("age", 30)
print(hash_table.search("name"))  # Output: Alice
print(hash_table.search("age"))   # Output: 30


#find the leaders in the array


