# Take collection of number input from user. Print the total positive and negative number
pcount=0
ncount=0

count=int(input("Enter quantity of total numbers to enter: "))
i=0
while i<count:
    num=int(input("Enter number: "))
    if (num<0):
        ncount +=1
    else:
        pcount+=1
    i+=1
print("positive: ",pcount)
print("negative: ",ncount)