'''
arithetic : +, -, *, /, %

'''
a = 23
b = 20
print("Addition + ", a+b )
print("Sub -", a-b)
print("Modulus %", a%b)
print("Expo", 2**a)
print("Expo", 2**(1/2))
print("Expo", 2**(1/3))
print("Expo", 25**0.5)




# comparion 

# int, float, str
# bool - 0,1 - True or False
isAvailable = True
print(type(isAvailable))

print("a is greater than b", a>b)
print(f"{a} is greater than {b}", a>b)
print("a is less than b statment is", a<b)
print(f"{a} is less than {b} statement is", a<b)


print(f"statement: {a} is equal to {b} is ", a==b)
print(f"statement: {a} is not equal to {b} is ", a!=b)
print(f"statement: {a} is greater than or equal to {b}", a>=b)
print(f"statement: {a} is less than or equal to {b}", a<=b)

# Logical operator
# bool    bool  AND         OR      NOT(bool1)
# True    True  True        True    False
# True    False False       True    False
# False   True  False       True    True
# False   False False       False   True

a = True
b = True 
print(f"{a} and {b} \t", a and b)
print(f"{a} or {b}\t", a or b)
print(f'not({a})\t', not(a))


a = True
b = False 
print(f"{a} and {b} \t", a and b)
print(f"{a} or {b}\t", a or b)
print(f'not({a})\t', not(a))


a = False
b = True 
print(f"{a} and {b} \t", a and b)
print(f"{a} or {b}\t", a or b)
print(f'not({a})\t', not(a))


a = False
b = False 
print(f"{a} and {b} \t", a and b)
print(f"{a} or {b}\t", a or b)
print(f'not({a})\t', not(a))


a = -10
b = 10
c = a+b-20

print(a<b and b<c)

# assignment operator
a = 10
b = 20
a = a + 20
print(a)
a += 20
print(a)
a = a - 10
print(a)
a -=10
print(a)
a*=10
print(a)
