# ii) Write a Python program to convert temperatures to and from celsius, Fahrenheit.

temp= int(input ("Enter temprature: "))
q= input ("Enter unit of temprature Celsis (c) or Fahrenheit(f) : ")

if q.upper()=="C":
    in_fahrenheit= int ((temp*9/5)+32)
    print(str(in_fahrenheit) + " F")
if q.upper()=="F":
    in_celsius= ((temp-32)*5/9)
    print(str(in_celsius) + " C")
else:
    print ("Invalid unit ")
