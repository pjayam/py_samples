print('Hello, world!')

num1 = 1.5
num2 = 7.8766676768768768678

# Add two numbers
sum = float(num1) + float(num2)

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

# Note: change this value for a different result
num = 9 

# uncomment to take the input from 161the user
# num = float(input('Enter a number: '))
num_sqrt = num ** 0.5
print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))

print("----------------EXERCISE--------------------")
# change this code
mystring = "hello"
myfloat = 10.0
floatNum = float(100)
myint = 20

print(floatNum)

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)