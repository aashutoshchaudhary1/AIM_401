# # for i in range (1,10):
# #     print(i)


# for eachpass in range(4):
#     print("it is good")



# number = 2
# expotent = 3
# product = 1
# for eachpass in range (expotent):
#     product = product*number
#     print(product)
# no = int(input("Enter a number:"))
# for no in range (no,11):
#     for mul in range (1,11):
#         print(no,"x",mul,"=",no*mul)
#     print("\n")
    

# one_number = int(input("enter a number:"))
# second_number = int(input("Enter the second number:"))
# jump = int (input("Enter a jump number:"))
# for third in range (one_number, second_number,jump):
#     print(third, end="\t\t")


# lower = int(input("Enter te lower bound:"))
# upper = int(input("Enter the upper bound:"))
# thesum = 0
# for number in range(lower, upper+1):
#     thesum = thesum + number
    
# print("The sum of numbers is:",thesum)

# Audmented Assignment

# for count in range(0,2):
#     print (count)


# field and precision
# salary =100000
# print("Your salary id Rs %10.3f" % salary)

# condition statment
marks = int(input("Enter your marks:"))
if marks >= 90:
    print("Your grade is A")
elif marks >= 80:
    print("Your grade is B")
elif marks >= 70:
    print("Your grade is C")
elif marks >= 60:
    print("Your grade is D")
else:
    print("Your grade is F")