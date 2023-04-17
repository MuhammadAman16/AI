# (i)Use dir and help to learn about the functions you can call on dictionaries and implement it.
my_dict = {"apple": 1, "banana": 2, "orange": 3}

print(dir(dict))
help(dict.keys)

del my_dict["banana"]
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
my_dict.update({"pear": 4})
print(my_dict)