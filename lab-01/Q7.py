# function to convert temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# function to convert temperature from Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("Enter temperature for the last week")

# a list of temperatures in Celsius
temperatures_celsius = []

for i in range(1, 5):
    celsius_input = int(input("Temperature for day " + str(i) + " in Celsius: "))
    temperatures_celsius.append(celsius_input)

# tuple to store the minimum and maximum temperatures in Celsius
min_temp_c = min(temperatures_celsius)
max_temp_c = max(temperatures_celsius)
print("The max temperature in the past week is: " + str(max_temp_c) + " degrees Celsius")
print("The min temperature in the past week is: " + str(min_temp_c) + " degrees Celsius")
if min_temp_c <= 11:
    print("The weather is cold")
elif max_temp_c<=25 and min_temp_c>=10:
    print("The weather is pleasent")
else:
    print("The weather is warm")
# convert the minimum and maximum temperatures to Fahrenheit

to_fahrenheit=input(print("Do you want to convert the temprature in Faherenheit (y/n)? "))

if (to_fahrenheit.upper()=="Y"):
    max_temp_f=celsius_to_fahrenheit(max_temp_c)
    print("The max temperature is "+str(max_temp_f) + " degrees Fahrenheit")
    min_temp_f = celsius_to_fahrenheit(min_temp_c)
    print("The min temperature is "+ str(min_temp_f) + " degrees Fahrenheit")
else:
    print("Thank you")




