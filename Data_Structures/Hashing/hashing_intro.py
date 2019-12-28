#__author__ : girish
# source https://www.bogotobogo.com/python/python_hash_tables_hashing_dictionary_associated_arrays.php


hash_table = [None] * 10
print(hash_table)


# function to generate hash value


def hashing_func(key):
    return key % len(hash_table)

# Inserting Data into Hash Table


def insert(hash_table, key, value):
    hash_key = hashing_func(key)
    hash_table[hash_key] = value
    print("Updated Table -->", hash_table)


# insert element
insert(hash_table, 10, 'Nepal')
# ouputs ['Nepal', None, None, None, None, None, None, None, None, None]

insert(hash_table, 25, 'USA')
#ouputs ['Nepal', None, None, None, None, 'USA', None, None, None, None]

# access value
print(hash_table[hashing_func(10)])  # outputs Nepal


# Concept of Collision
'''
Collision

A collision occurs when two items/values get the same slot/index, 
i.e. the hashing function generates same slot number for multiple items. 
If proper collision resolution steps are not taken then the previous item\
    in the slot will be replaced by the new item whenever the collision occurs.
'''

# eg of Hashing
insert(hash_table, 20, 'India')
#outputs ['India', None, None, None, None, 'USA', None, None, None, None]
# here hash key will be same for Nepal, India so it will get replaced with India

'''
Collision Resolution

There are generally two ways to resolve a collision:

1. Linear Probing
2. Chaining

1. Linear Probing

One way to resolve collision is to find another open slot whenever there is a\
collision and store the item in that open slot. The search for open slot starts\
from the slot where the collision happened. It moves sequentially through the\
slots until an empty slot is encountered. The movement is in a circular fashion.
It can move to the first slot while searching for an empty slot. Hence,\
covering the entire hash table. This kind of sequential search is called\
Linear Probing.

2. Chaining

The other way to resolve collision is Chaining. This allows multiple items\
exist in the same slot/index. This can create a chain/collection of items in a\
single slot. When the collision happens, the item is stored in the same slot\
using chaining mechanism.

'''
