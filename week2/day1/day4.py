# f= open ("a.txt", "w")
# f.write("Hello World")

# f = open("a.txt", "r")
# # f.write("\nMy name is Aashutosh")
# print(f.read())
# f.close()

# import random
# f= open("integer.txt", "w")
# for count in range(50):
#     number = random.randint(1,500)
#     f.write(str(number) + "\n")
# f.close()


# f = open("integer.txt", "r")
# total_sum = 0

# for line in f:
#     # Convert each line string to integer and add to total_sum
#     total_sum += int(line.strip())

# print("Sum of all numbers:", total_sum)

# Example: Data with numbers in both rows and columns (e.g. "10 20 30")



# 1. Using line.strip() for single number per line (like in integer.txt)
f = open("integer.txt", "r")
total_sum = 0

for line in f:
    # line.strip().split() splits "28  34  45" into ['28', '34', '45']
    for num_str in line.strip().split():
        total_sum += int(num_str)

f.close()

print("Sum of all numbers:", total_sum)




# hw to read and write format in json uisng python

2