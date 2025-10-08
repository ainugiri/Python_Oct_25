'''
numeric -> int, float, complex (real + imaginary)
Boolean
sequence -> string, list, tuple
Dictionaries
Set
'''

# complex - real + j
x = 10 + 4j
y = 20 - 2j
z = x + y
print(f" The value of x is {x}, type of z is {type(x)}")
print(f" The value of y is {y}, type of z is {type(y)}")
print(f" The value of z is {z}, type of z is {type(z)}")


x = 10 + 4j
y = 20 - 2j
z = x * y
print(f" The value of x is {x}, type of z is {type(x)}")
print(f" The value of y is {y}, type of z is {type(y)}")
print(f" The value of z is {z}, type of z is {type(z)}")


name = 'value'
p1 = """This is a multiline string
This is the second line
This is the third line
"""

print(f" The value of name is {name}, type of name is {type(name)}")
print(f" The value of p1 is {p1}, type of p1 is {type(p1)}")


word = 'Python'
print(word[0])      # First character P
print(word[-1])     # Last character n
print(word[3:6])    # Characters from index 3 to 5
print(word[1:])     # Characters from index 1 to end
print(word[:3])     # Characters from start to index 2


name = 'Giri Prasad P'

for char in name:
    print(char)

