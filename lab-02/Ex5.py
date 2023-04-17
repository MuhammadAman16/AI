# Fixed a Letter from a to e and then ask the user to guess that letter until correct letter entered.
value="c"
uservalue = input("Enter a letter from a to e: ")

while value!=uservalue:
    print("Incorrect")
    uservalue = input("Enter a letter from a to e: ")

print("Welcome user")
