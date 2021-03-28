#ZeroDivisionError()

#Simple

try:
    10/0
except:
    print('Cannot divide by zero', '\n')

#Indicating type or error

try:
    10/0
except Exception as identifier:
    print('Error: ', identifier, '\n')

#Unsopported operand type//By dinamically asking to enter characters, will raise an exception of unsopported opperand type. The code must be int or float.
#If the user enter a division by 0, the exception will raise as ZeroDivisionError()

result = None
a = 'a'
b = 2

try:
    result = a / b
except Exception as identifier:
    print('Result:', result)
    print('Error:', identifier)
    print(type(identifier))

print('Result:', result)
print('The program continues...', '\n')

#With Else and Finally
#Else is an optional block
#When a Finally is coded, it will go thru it

result_one = None
a = 10
b = 2

try:
    result_one = a/b
except Exception as identifier:
    print('Error:', identifier)
else:
    print('No exceptions detected')

print('Result:', result_one)
print('The program continues...', '\n')

result_two = None
a = 10
b = 2

try:
    result_two = a/b
except Exception as identifier:
    print('Error:', identifier)
else:
    print('No exceptions detected')
finally:
    print('End of block Try')

print('Result:', result_two)
print('The program continues...', '\n')

#Costumize own exceptions

class IdenticalNumbersException(Exception):
    def __init__(self, message):
        self.message = message

a = 2
b = 2

try:
    if a == b:
        raise IdenticalNumbersException('Identical numbers')
except Exception as identifier:
    print('Error: ', identifier)
finally:
    print('End of block Try')

print('The program continues...')
