# functions that takes a input, of string and returns the numbers of vowels (a,e,i,o,u) present in it
def count_vowels():
    input_string = input("Enter a string: ")
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

print("Vowels Count:",count_vowels())




# ebnumerate and zip