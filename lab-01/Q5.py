# i)Write a list comprehension which, from a list, generates a lowercased version of each string that has
# length greater than five.

comprehension = ["My", "name", "is" ,"Muhammad", "I", "study", "in" ,"UBIT"]
lowercase=[]

for s in comprehension:
    if len(s)>5:
        lowercase.append(s.lower())

print(lowercase)