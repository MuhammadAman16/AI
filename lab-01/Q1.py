# (i)Write a Python program to swap 4 variables values (input four values.
# Sample input:
# Before swapping
# a=2,b=56,c=78,d=9
# After Swapping
# a=,9,b=78,c=56,d=2

a= input("Enter Value: ")
b=input("Enter Value: ")
c=input("Enter Value: ")
d=input("Enter Value: ")

a,b,c,d=d,c,b,a
print("a="+ a,"b="+b, "c="+c,"d="+d)
