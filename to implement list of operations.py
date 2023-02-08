# Initialize a list
my_list = [1, 2, 3, [4, 5, 6], 'hello']

# Nested lists
print("Nested lists:", my_list[3])

# Length
print("Length of the list:", len(my_list))

# Concatenation
concatenated_list = my_list + [7, 8, 9]
print("Concatenated list:", concatenated_list)

# Membership
print("Is 'hello' in the list?:", 'hello' in my_list)

# Iteration
for item in my_list:
    print(item)

# Indexing
print("Third item in the list:", my_list[2])

# Slicing
print("First three items in the list:", my_list[:3])
