# Write conditional statements to print value of 0 to 1 and 1 to 0 and numbers in between
a = int(input())

if(a == 0):
    a=1
elif(a == 1):
    a=0
elif(a>2 or a<0):
    print ("You have entered a number in between")
print(a)

