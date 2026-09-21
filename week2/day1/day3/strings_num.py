# binary_str = input("Enter a binary number: ")
# binary_digits = ['0', '1']

# # Check if all characters are valid binary digits ('0' or '1')
# for char in binary_str:
#     if char not in binary_digits:
#         print("Invalid binary number")
#         break
# else:
#     # Convert binary to decimal
#     decimal_val = 0
#     exponent = len(binary_str) - 1
#     for digit in binary_str:
#         decimal_val += int(digit) * (2 ** exponent)
#         exponent -= 1
        
#     print(f"Decimal equivalent: {decimal_val}")


# Convert Decimal to Binary using Floor Division

# Get decimal number from user
decimal_num = int(input("Enter a decimal number: "))

if decimal_num == 0:
    binary_str = "0"
else:
    binary_str = ""
    temp = decimal_num
    
    while temp > 0:
        remainder = temp % 2           # Get the binary digit (0 or 1)
        binary_str = str(remainder) + binary_str  # Prepend remainder to result string
        temp = temp // 2               # Floor division to reduce number

print(f"Binary equivalent of {decimal_num} is: {binary_str}")
