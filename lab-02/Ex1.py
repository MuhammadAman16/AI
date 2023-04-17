# Print square root of negative or positive number using if and operators.

a = int(input("Enter a number and get its square root: "))
if (a > 0):
    print("The number is greater than 0, so i can calculate it!")
    root = a ** (1 / 2)
    print("The square root of %d is %f" % (a, root))
if (a <= 0):
    print("I can't calculate the square root of negative number!")
    print("Thanks!")

