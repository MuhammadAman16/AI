# II. a Python program to find if a given string starts with a given character using Lambda.
input_string=input("Enter String: ")

checkLetter=(lambda x: x==input_string[0])

first_char=input("Enter First character to check: ")

if checkLetter(first_char):
    print("given string starts with the given character")
else:
    print("String starts with another character")
