# Python List Operations - Complete Guide

# 1. Creating a List
numbers = [10, 20, 30, 40, 50]
print("Initial List:", numbers)

# 2. Accessing Elements (Indexing & Slicing)
print("\n--- Accessing Elements ---")
print("First element (index 0):", numbers[0])
print("Last element (index -1):", numbers[-1])
print("Slicing (index 1 to 3):", numbers[1:4])

# 3. Adding Elements
print("\n--- Adding Elements ---")
# append(): adds item to the end
numbers.append(60)
print("After append(60):", numbers)

# insert(): adds item at a specific index
numbers.insert(2, 25)  # insert 25 at index 2
print("After insert(2, 25):", numbers)

# extend(): adds multiple items from another list
numbers.extend([70, 80])
print("After extend([70, 80]):", numbers)

# 4. Modifying Elements
print("\n--- Modifying Elements ---")
numbers[0] = 5
print("After changing index 0 to 5:", numbers)

# 5. Removing Elements
print("\n--- Removing Elements ---")
# remove(): removes the first occurrence of a value
numbers.remove(25)
print("After remove(25):", numbers)

# pop(): removes and returns item at given index (default is last item)
popped_item = numbers.pop()
print(f"After pop() (removed {popped_item}):", numbers)

popped_index_1 = numbers.pop(1)
print(f"After pop(1) (removed {popped_index_1}):", numbers)

# 6. Searching & Checking Elements
print("\n--- Searching Elements ---")
print("Is 30 in numbers?", 30 in numbers)
print("Index of value 40:", numbers.index(40))
print("Count of value 50:", numbers.count(50))

# 7. Sorting & Reversing
print("\n--- Sorting & Reversing ---")
numbers.reverse()
print("After reverse():", numbers)

numbers.sort()
print("After sort() (ascending):", numbers)

numbers.sort(reverse=True)
print("After sort(reverse=True) (descending):", numbers)

# 8. Useful Built-in Functions
print("\n--- List Utility Functions ---")
print("Length of list (len):", len(numbers))
print("Minimum value (min):", min(numbers))
print("Maximum value (max):", max(numbers))
print("Sum of elements (sum):", sum(numbers))


