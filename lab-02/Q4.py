# 1. Create a loop that counts from 0 to 100
count =1
while count <=100:
    print (count)
    count+=1

# 2. Make a multiplication table using a loop
num=2
i=1
while num<20:
    num=2*i
    print(num)
    i+=1

# 3. Output the numbers 1 to 10 backwards using a loop
count =10
while count >= 1:
    print (count)
    count-=1

# 4. Create a loop that counts all even numbers to 10
count=0
for i in range(11):
    if (i%2==0):
        print(i)
        count+=1
print("total number of even numbers",count)

# 5.  Create a loop that sums the numbers from 100 to 200
sum = 0
for i in range(100, 201):
    sum += i
print(sum)

# 6. Make a program that lists the countries in the set below using a while loop.
clist = ["Canada","USA","Mexico"]
i=0
while (i<len(clist)):
    print(clist[i])
    i += 1



