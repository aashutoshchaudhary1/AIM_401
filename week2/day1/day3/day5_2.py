import copy
from collections import deque

# ==========================================
# 1. COPYING LISTS (Shallow vs Deep Copy)
# ==========================================
print("--- 1. List Copying ---")

# Shallow Copy: .copy() or [:]
original = [1, 2, [3, 4]]
shallow_copied = original.copy()  # or original[:]

shallow_copied[0] = 99
# Modifying inner list affects BOTH because shallow copy shares references to nested objects
shallow_copied[2][0] = 888

print("Original after shallow copy modification:", original)
print("Shallow copied list:", shallow_copied)

# Deep Copy: copy.deepcopy()
original_2 = [1, 2, [3, 4]]
deep_copied = copy.deepcopy(original_2)

deep_copied[2][0] = 999  # Does NOT affect original_2
print("\nOriginal 2 after deep copy modification:", original_2)
print("Deep copied list:", deep_copied)


# ==========================================
# 2. LIST AS A STACK (LIFO: Last-In, First-Out)
# ==========================================
print("\n--- 2. Stack Operations (LIFO) ---")
stack = []

# Push elements using append()
stack.append("Page 1")
stack.append("Page 2")
stack.append("Page 3")
print("Stack after pushes:", stack)

# Peek (look at top element without removing)
top_item = stack[-1]
print("Top item (peek):", top_item)

# Pop element (removes from top)
popped = stack.pop()
print(f"Popped item: {popped}")
print("Stack after pop:", stack)


# ==========================================
# 3. QUEUE OPERATIONS (FIFO: First-In, First-Out)
# ==========================================
print("\n--- 3. Queue Operations (FIFO using deque) ---")
queue = deque(["Customer 1", "Customer 2", "Customer 3"])

# Enqueue (add to back)
queue.append("Customer 4")
print("Queue after enqueue:", list(queue))

# Dequeue (remove from front)
served = queue.popleft()
print(f"Served (dequeued): {served}")
print("Queue after popleft:", list(queue))


# ==========================================
# 4. LIST COMPREHENSION
# ==========================================
print("\n--- 4. List Comprehension ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Squares of even numbers
even_squares = [x**2 for x in numbers if x % 2 == 0]
print("Squares of even numbers:", even_squares)


# ==========================================
# 5. USEFUL FUNCTIONS (enumerate, zip, join, any, all)
# ==========================================
print("\n--- 5. Useful Advanced Functions ---")

fruits = ["apple", "banana", "cherry"]
prices = [1.2, 0.5, 2.5]

# enumerate(): gives index and value together
print("enumerate():")
for index, fruit in enumerate(fruits):
    print(f"  Index {index}: {fruit}")

# zip(): combines two or more lists element-by-element
print("\nzip():")
for fruit, price in zip(fruits, prices):
    print(f"  {fruit} costs ${price}")

# join(): joins string list elements with a separator
string_list = ["Python", "is", "awesome"]
sentence = " ".join(string_list)
print("\njoin():", sentence)

# any() and all()
bool_list = [True, False, True]
print("\nany(bool_list):", any(bool_list))  # True if AT LEAST ONE element is True
print("all(bool_list):", all(bool_list))  # True if ALL elements are True
