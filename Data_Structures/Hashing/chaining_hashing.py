hash_table = [[] for _ in range(10)]
print(hash_table)
# Output:
# [[], [], [], [], [], [], [], [], [], []]

# hash key function


def hashing_func(hash_table, key):
    return key % len(hash_table)


# insert
'''
-While inserting a new element into the hash table, we first search if the key already exists in the hash table.
-If the key is already present in the hash table, then we update its value with the new one.
-Otherwise, we insert a new key-value pair into the hash table.
'''


def insert(hash_table, key, value):

    hash_key = hashing_func(hash_table, key)
    key_exists = False
    bucket = hash_table[hash_key]

    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            key_exists = True
            break

    if key_exists:
        bucket[i] = ((key, value))
    else:
        bucket.append((key, value))


insert(hash_table, 10, 'Nepal')
insert(hash_table, 25, 'USA')
print(hash_table)

insert(hash_table, 20, 'India')
print(hash_table)


# serching
def search(hash_table, key):
    hash_key = hashing_func(hash_table, key)
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return v


print(search(hash_table, 10))  # Output: Nepal
print(search(hash_table, 20))  # Output: India
print(search(hash_table, 30))  # Output: None
