# for chaining
hash_table = [[] for _ in range(10)]

# output [[], [], [], [], [], [], [], [], [], []]


def hashing_func(key):
    return key % len(hash_table)


def insert(hash_table, key, value):
    hash_key = hashing_func(key)
    hash_table[hash_key].append(value)
    print(hash_table)


insert(hash_table, 10, 'Nepal')
# outputs [['Nepal'], [], [], [], [], [], [], [], [], []]

insert(hash_table, 25, 'USA')
# outputs [['Nepal'], [], [], [], [], ['USA'], [], [], [], []]

insert(hash_table, 20, 'India')
# outputs [['Nepal', 'India'], [], [], [], [], ['USA'], [], [], [], []]


'''
Standard Implementation

A more standard implementation of Hash Table with Python is presented below.
We create three different functions to insert, search, and delete items from the hash table.

Python’s built-in “hash” function is used to create a hash value of any key.
This function is useful as it creates an integer hash value for both string\
and integer key. The hash value for integer will be same as it is, 
.e. hash(10) will be 10, hash(20) will be 20, and so on.

In the below code, note the difference in output while using 10 and ’10’.\
10 (without quote) is treated as an integer and ’10’ (with quote) is treated as a string.
'''
hash_key = hash('xyz')
print(hash_key)  # Output: -5999452984703080694


# string and number has diff hash value
hash_key = hash('10')
print(hash_key)  # Output: 6272037681056609
hash_key = hash(10)
print(hash_key)  # Output: 10


hash_key = hash('20')
print(hash_key)  # Output: 6400038450057764
hash_key = hash(20)
print(hash_key)  # Output: 20

hash_key = hash('25')
print(hash_key)  # Output: 6400038450057761
hash_key = hash(25)
print(hash_key)  # Output: 25


# we can use hash value % hash table length, for the same

hash_key = hash('10') % len(hash_table)
print(hash_key)  # Output: 9
hash_key = hash('20') % len(hash_table)
print(hash_key)  # Output: 4
hash_key = hash('25') % len(hash_table)
print(hash_key)  # Output: 1
hash_key = hash(10) % len(hash_table)
print(hash_key)  # Output: 0
hash_key = hash(20) % len(hash_table)
print(hash_key)  # Output: 0
hash_key = hash(25) % len(hash_table)
print(hash_key)  # Output: 5
