# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Shaker'
age = 28

# Concatenate 
print('Hello, my name is ' + name + ' and I am ' + str(age))

# String Formatting

# Arguments by position
print('My name is {name} and I am {age}'.format(name=name, age=age))

#F-Strings 
print(f'Hello, my name is {name} and I am {age} years old.')

# String Methods
s = 'hello world'

# Capitalize string
print(s.capitalize())