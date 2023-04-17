# (ii)Write a Python script to concatenate following dictionaries to create a new one.
dict1 = {"apple": 1, "banana": 2}
dict2 = {"orange": 3, "pear": 4}
dict3 = {"grape": 5, "pineapple": 6}

new_dict = {}

for i in [dict1,dict2,dict3]:
    new_dict.update(i)

print("Concatenated dictionary:", new_dict)
