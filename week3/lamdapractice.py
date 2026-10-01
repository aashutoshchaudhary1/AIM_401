# """
# Demonstration of Regular Functions and Lambda Functions in Python.
# """

# # ==========================================
# # 1. Regular Function (def) vs Lambda Function
# # ==========================================

# # Regular function to add two numbers
# def add_regular(a, b):
#     return a + b

# # Equivalent Lambda function to add two numbers
# add_lambda = lambda a, b: a + b

# print("--- 1. Simple Addition ---")
# print("Using regular function:", add_regular(5, 3))
# print("Using lambda function: ", add_lambda(5, 3))
# print()


# # ==========================================
# # 2. Using Lambda with Higher-Order Functions (map & filter)
# # ==========================================

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Using map() with lambda to square each number
# squared_numbers = list(map(lambda x: x ** 2, numbers))

# # Using filter() with lambda to extract even numbers
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# print("--- 2. Map and Filter Examples ---")
# print("Original numbers:       ", numbers)
# print("Squared numbers (map):  ", squared_numbers)
# print("Even numbers (filter):  ", even_numbers)
# print()


# # ==========================================
# # 3. Custom Function Accepting a Lambda Function
# # ==========================================

# def apply_operation(numbers_list, operation):
#     """
#     Takes a list of numbers and a function/lambda operation,
#     applying the operation to each element.
#     """
#     return [operation(x) for x in numbers_list]

# print("--- 3. Custom Higher-Order Function ---")
# doubled = apply_operation(numbers, lambda x: x * 2)
# cubed = apply_operation([1, 2, 3, 4], lambda x: x ** 3)

# print("Doubled numbers: ", doubled)
# print("Cubed numbers:   ", cubed)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Using lambda function with filter() to extract even numbers
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# # print("Even numbers:", even_numbers)
# square=list(map(lambda x: x ** 2, numbers))
# print("Square Numbers: ",square)

# from functools import reduce

# # Sum of all numbers in the list using reduce() and lambda
# total_sum = reduce(lambda x, y: x + y, numbers)
# print("Sum of all numbers:", total_sum)



data = ["Welcome", "to", "MIT"]
up =[word.upper() for word in data if "e" in word]
print("Uppercase words:", up)