# count = 1
# while count < 50:
#     if count == 4:
#         break
#     print(f"count is {count}")
#     count += 1
# print("Loop ended")
    

# continue statement
# i = 0
# while i <5:
#     i+=1

#     if i ==3:
#         continue
#     print(i)

# pass statement
# count = 0
# while count < 4:
#     count+=1
#     if count==2:
#         pass
#     else:
#         print(f"Processing numebr: {count}")

# Number guessing game
# number = int(input("Guess a number between 1 to 100: "))
# while number != 40:
#     if number < 40:
#         print("You guessed too low")
#         number = int(input("Guess a number between 1 to 10: "))
#     elif number > 40:
#         print("You guessed too high")
#         number = int(input("Guess a number between 1 to 10: "))
        
# print("You guessed correct")


# ATM Machine
balance = 0
while True:
    print("1.Deposit")
    print("2.Display")
    print("3.Exit")

    option=int(input("Enter your choice: "))

    if option == 1:
        amount= int(input("Enter the amount to deposit: "))
        print(f"Amount deposited: {amount}")
        balance+=amount
    elif option == 2:
        print(f"Current balance: {balance}")
    elif option == 3:
        break
    else:
        print("Invalid choice")

