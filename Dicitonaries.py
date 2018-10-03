phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

# Alternatively, a dictionary can be initialized with the same values in the following notation:
# phonebook = {
#     "John" : 938477566,
#     "Jack" : 938377264,
#     "Jill" : 947662781
# }
# print(phonebook)


# Iterating over dictionaries

phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))


# Removing 
#del phonebook["John"]
# OR 
phonebook.pop("John")
phonebook["Jake"] = 938273443
print(phonebook)

for key in phonebook.iterkeys():
    print(key)

if phonebook.has_key("Jake"):
    print("TRUE")
