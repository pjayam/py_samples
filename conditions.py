x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True

print("--------and - or operators------")

name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")


print("--------in operator------")

name = "John"
names = ["Johdn", "Ricdk"]
if name in names:
    print("Your name is either John or Rick.")
else:
    print("Your name is none of John or Rick.")

print("--------is operator------")
#Unlike the double equals operator "==", the "is" operator does not match the values of the variables, but the instances themselves.
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False

print("--------not operator------")

print(not False) # Prints out True
print((not False) == (False)) # Prints out False


print("----------EXERCISE----------")
# change this code
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")