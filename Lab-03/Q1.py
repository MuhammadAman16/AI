# I. a Python program to square and cube every number in a given list of integers using Lambda.
numbers = [1,2,3,4]

square_number=list(map(lambda x:x**2,numbers))
cube_number= list(map(lambda x:x**3,numbers))

print (square_number)
print (cube_number)