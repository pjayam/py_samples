astring = "Hello world!"
print("single quotes are ' '")

print("length : %d" %len(astring))
print("Index of 'O' is %d " % astring.index("o"))
print("Count of letter 'l' : %d" %astring.count("l"))#here it is case-sensitive
print(astring[3:7]) #Substring Includes 3 and excludes 7

#This prints the characters of string from 3 to 7 skipping one character. This is extended slice syntax. The general form is [start:stop:step].
print(astring[3:7:2]) 
print(astring[3:7:1])

# They are an easy way of starting at the end of the string instead of the beginning. This way, -3 means "3rd character from the end".
print(astring[-3:12]) # '-' represents from last

print(astring.upper())
print(astring.lower())
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))
print(astring.split(" "))

##------------------------------------
print("----------------EXERCISE--------------------")
s = "Strings are awesome!"
# Length should be 20
print("Length of string s is = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))