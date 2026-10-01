# # def sum(a,b):
# #     return a+b

# # print(sum(1, 2))


# # No arguemnt no return value

# # def greet():
# #     print("Hello")

# # greet()

# #argument but no return value

# # def add(a,b):
# #     sum = a+b
# #     print(sum)


# # add(1,3)


# #with no argument but return value
# # def add():
# #     a=int(input("ENter the value of a:"))
# #     b=int(input("Enter the value of b:"))
# #     return a+b

# # print(add())


# def area(length,breadth):
#     a=length*breadth
#     return a

# print(area(20,10))


# #Opertaors using UDf

# def operators():
#     a = int(input("Enter the value of a:"))
#     b = int(input("Enter the value of b:"))
#     print("The sum of a and b is:",a+b)
#     print("The difference of a and b is:",a-b)
#     print("The product of a and b is:",a*b)
#     print("The division of a and b is:",a/b)
#     print("The modulo of a and b is:",a%b)


# operators()

# # User-Defined Function (UDF) to process 5 user inputs
# def process_inputs():
#     user_list = []
    
#     for i in range(1, 6):
#         user_input = input(f"Enter input {i} of 5: ").strip()
        
#         try:
#             # Check if integer (no decimal point) or float
#             if '.' not in user_input:
#                 val = int(user_input)
#                 user_list.append(val)
#                 print(f"-> Added integer '{val}' to list.")
#             else:
#                 val = float(user_input)
#                 if user_list:
#                     removed = user_list.pop()
#                     print(f"-> Float '{val}' entered. Removed last element '{removed}' from list.")
#                 else:
#                     print(f"-> Float '{val}' entered. List is empty, nothing to remove.")
#         except ValueError:
#             print("-> Invalid input! Please enter a valid integer or float.")
            
#         print("Updated list:", user_list)
#         print("-" * 40)

# # Execute the function
# process_inputs()


# Student Result Management UDF
def student_management():
    student_data = {}
    
    # Input name and marks of 5 students
    for i in range(1, 6):
        print(f"\n--- Student {i} ---")
        name = input("Enter student name: ").strip()
        marks = float(input(f"Enter marks for {name}: "))
        
        # Grading Condition
        if marks >= 80:
            grade = "A"
        elif marks >= 60:
            grade = "B"
        elif marks >= 40:
            grade = "C"
        else:
            grade = "F"
            
        # Store data in dictionary
        student_data[name] = {
            "marks": marks,
            "grade": grade
        }

    # Display each student's name, marks, and grade
    print("\n================ STUDENT RESULTS ================")
    print(f"{'Name':<15} {'Marks':<10} {'Grade':<10}")
    print("-" * 35)
    for name, info in student_data.items():
        print(f"{name:<15} {info['marks']:<10.2f} {info['grade']:<10}")

    # Calculate and display highest, lowest, and average marks
    all_marks = [info["marks"] for info in student_data.values()]
    highest_marks = max(all_marks)
    lowest_marks = min(all_marks)
    average_marks = sum(all_marks) / len(all_marks)

    print("\n================ SUMMARY STATISTICS ================")
    print(f"Highest Marks : {highest_marks:.2f}")
    print(f"Lowest Marks  : {lowest_marks:.2f}")
    print(f"Average Marks : {average_marks:.2f}")

# Execute the function
student_management()


