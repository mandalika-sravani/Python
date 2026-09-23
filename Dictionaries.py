# Dictionary --- A collection of {key:value} pairs ordered and changeable. no duplicates

capitals = {"USA" : "Washington D.C",
            "India" : "New Delhi",
            "China" : "Beijing",
            "Russia" : "Moscow"}

# print(dir(capitals))

capitals.update({"Germany" : "Berlin"})

print(capitals)

#keys = capitals.keys()
#print(keys)

for key in capitals.keys():
    print(key)

#values = capitals.values()
#print(values)

for value in capitals.values():
    print(value)
