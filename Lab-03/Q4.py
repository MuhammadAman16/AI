# You have collected information about cities in your province. You decide to store each city’s
# name, population, and mayor in a file. Write a python program to accept the data for a number
# of cities from the keyboard and store the data in a file in the order in which they’re entered

f = open('mycities.txt', 'w')
count=int(input("Enter the number of cities for which you want to enter the data: "))
for i in range(count):
    city = input("Enter the city name: ")
    population = input("Enter the city population: ")
    mayor = input("Enter the mayor's name: ")
    f.write(f"{city},{population},{mayor}\n")
f.close()
print("City data saved to file.")




