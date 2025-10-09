# key - value

A825662 = {
    'name': 'Giri',
    'age': 40,
    'city': 'Chennai',
    'is_married': True,
    'hobbies': ['reading', 'traveling', 'swimming'],
    'address': {
        'street': '123 Main St',
        'zip': '600001'
    },
    'phone_numbers': ('123-456-7890', '987-654-3210'),  # tuple
    'email': 'giriprasa@gmail.com'
}

print(A825662)
print(type(A825662))
print(f" Name: {A825662['name']}, Age: {A825662['age']}, City: {A825662['city']}")

del A825662['email']

del A825662['city']
print(A825662)

A825662.popitem()
print(A825662)
