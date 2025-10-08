mytup = tuple()
print(type(mytup))  # <class 'tuple'>

mytup = ()
print(type(mytup))  # <class 'tuple'>

mytup = (1,2,3,4,5)
print(type(mytup))  # <class 'tuple'>
print(mytup)        # (1, 2, 3, 4, 5)
print(mytup[0])     # 1

l1 = list(mytup)
l1[2] = 30
mytup = tuple(l1)
print(mytup)        # (1, 2, 30, 4, 5)

print(mytup[1:4])  # (2, 30, 4)


x1, x2, x3, x4, x5 = mytup
print(x1)  # 1
print(x2)  # 2
print(x3)  # 30
print(x4)  # 4
print(x5)  # 5

tup1 = ('A','B','C')

tup2 = (1,2,3)

tup3 = tup1 + tup2
print(tup3)  # ('A', 'B', 'C', 1, 2, 3)
# tup3.remove('B')  # AttributeError: 'tuple' object has no attribute 'remove'
# tup3.reverse()    # AttributeError: 'tuple' object has no attribute 'reverse'

del tup1
del tup2
del tup3