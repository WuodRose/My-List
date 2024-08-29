# Step 1: Creating My list
my_list = []

# Step 2: Append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Check the list after appending
print("List after appending elements:", my_list)

# Step 3: Insert value at the second position
my_list.insert(1, 15)

# Check the list after inserting
print("List after inserting 15 at the second position:", my_list)

# Step 4: Extend with another list
my_list.extend([50, 60, 70])

# Check the list after extending
print("List after extending with [50, 60, 70]:", my_list)

# Step 5: Remove the last element
my_list.pop()

# Check the list after removing the last element
print("List after removing the last element:", my_list)

# Step 6: Sort the list
my_list.sort()

# Check the list after sorting
print("List after sorting:", my_list)

# Step 7: Find and print the index of value 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)
