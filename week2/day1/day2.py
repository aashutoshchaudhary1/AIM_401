# # Strings in Python
# name = "Aashutosh"
# strlen = len(name)
# # print(strlen)

# # # print the string in reverse order
# # print(name[::-1])

# # # strings are immutable
# # for letter in name:
# #     print(letter)

# for index in range(strlen):
#     print(index, name[index])


# data = "My name is Aashutosh Chaudhary"
# print(data[:len(data)])
# print(data[-3:])
# print(data[-7:-3])

# a= ["myfile.txt", "myprogram.exe", "Yourfile.txt"]
# for filename in a:
#     if ".txt" in filename:
#         print(filename)


# Caesar Cipher (Encrypt text by distance)
text = input("Enter a message: ")
distance = int(input("Enter distance value: "))

cipher_text = ""
for char in text:
    cipher_text += chr(ord(char) + distance)

print("Cipher text:", cipher_text)


