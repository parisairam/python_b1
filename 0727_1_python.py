# Hello World Program

message = 'Hello, World!'

print(message)

#Introduction to String

message = 'This is a string in Python'
print(message)
message = "This is also a string"
print(message)
message = "It's a string"
print(message)
message = "This is also a string"
print(message)
message = '"Beautiful is better than ugly.". Said Tim Peters'
print(message)
message = 'It\'s also a valid string'
print(message)
message = r'C:\python\bin'
print(message)

#Created Multiline String
help_message = '''
Usage: mysql command
    -h hostname     
    -d database name
    -u username
    -p password 
'''

print(help_message)

# Variables in String
name = 'John'
message = f'Hi {name}'
print(message)

#Concatenate Python Strings
greeting = 'Good ' 'Morning!'
print(greeting)

greeting = 'Good '
time = 'Afternoon'

greeting = greeting + time + '!'
print(greeting)

#Access String Elements

str = "Python String"
print(str[0]) # P
print(str[1]) # y

str = "Python String"
print(str[-1])  # g
print(str[-2])  # n

#Getting length of String
str = "Python String"
str_len = len(str)
print(str_len)

#Slicing Strings
str = "Python String"
print(str[0:2])