name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Hello", name, "you are", age, "years old.")
# print("Hello %s you are %d years old." %(name, age)) -> C style formatting
# java : System.out.printf("Hello %s you are %d years old.", name, age);

print(f"Hello {name} you are {age} years old.")  # f-string formatting -> Python 3.6+

a,b,c = input("Enter 3 values: ").split()
print(type(a), 'value of a is ', a) 
print(type(b), 'value of b is ', b) 
print(type(c), 'value of c is ', c) 

a,b,c = map(int, input("Enter 3 values: ").split())
print(type(a), 'value of a is ', a) 
print(type(b), 'value of b is ', b) 
print(type(c), 'value of c is ', c) 