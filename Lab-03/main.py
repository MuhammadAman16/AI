
# You have collected information about cities in your province. You decide to store each city’s
# name, population, and mayor in a file. Write a python program to accept the data for a number
# of cities from the keyboard and store the data in a file in the order in which they’re entered
# Open a file for writing

# The with statement is used to create a context in which the file is opened. This ensures that the file
# is properly closed when the block of code inside the with statement is finished, even if an error occurs.
# Inside the with block, the file object is assigned to a variable named f. This file object can be used
# to write data to the file.
# with open('mycities.txt', 'w') as f:
#     # Keep accepting city data until the user enters an empty city name
#     while True:
#         # Prompt the user for the city name
#         city = input("Enter the city name (or press Enter to quit): ")
#         if not city:
#             break
#         # Prompt the user for the city's population
#         population = input("Enter the city population: ")
#         # Prompt the user for the mayor's name
#         mayor = input("Enter the mayor's name: ")
#         # Write the city data to the file
#         f.write(f"{city},{population},{mayor}\n")
# print("City data saved to file.")

#  Write a python program to create a data file student.txt and append the message “Now we are
# AI students”s

# f = open("student.txt","a")
# f.write("Now we are AI students's")
# print("Data saved to file.")



# ==========================EXAMPLES=======================================



