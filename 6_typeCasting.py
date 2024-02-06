# type casting is needed because print function can handle only one type of datatype in python
name = "Fardin"
version = 1
# print(name+version) will return error as they are two different datatype
# So we need to type cast one of the variables to its appropriate type

version = str(version) # 1 is now a string in this line

print(name + version)

# we can use (,) . It will consider both of them as strings
print(name,version)

# type casting is needed while doing arithmatic operations with strings(digits only)

a = "100"
b= "50"

print(a+b) # it with return the string concatenated of a & b
# since we want to add the values of a & b we need to typecast them.
# either while printing or reassigning into them as numeric values
print(int(a)+int(b))

a = int(a)
b = int(b)
print(a+b)

# So we can do typecasting for each type of datatypes while necessary
