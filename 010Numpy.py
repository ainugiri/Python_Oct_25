import numpy as np
# numerical python - how to work with arrays

# a = np.array([1, 2, 3])

# print(a)
# print(type(a))


# # x,y
# b = np.array([[0,1,2],[3,4,5]])
# print(b)
# print(type(b))



# 0 0 0 
# 0 0 0
# 0 0 0

allzeros = np.zeros((2,3))
# print(allzeros)

#  1,1,1
#  1 1,1
#  1,1,1
allones = np.ones((3,3))
# print(allones)

# np.arange(start, end, step) -> 0, 100, 20 -> 0,20,40,60,80
# print(np.arange(0, 1, 0.1)) -> 0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9

# print(np.arange(0, 10, 2))
c = np.arange(0,20,4)
# print(c)

a = np.array([[10,20,30],[11,22,33],[1,2,3]])
# print(a)

# print(a[1,1])


b = np.array([1,2,3,4,5,6])
# print(b)
# print(b[3])
# print(b[0:3])


x = np.array([10,20,30])
y = np.array([1,2,3])

add = x + y
print('ADDITION',add)

subtract = x - y
print('subtract', subtract)

x = np.array([1,2,3])
y = np.array([10,20,30])
multiply = x * y 
print('multiply', multiply)



x = np.array([[10,20],[30,40]])
y = np.array([[1,2],[3,4]])

add = x + y
print('ADDITION \n',add)

subtract = x - y
print('subtract \n', subtract)


multiply = x * y
print('multiply \n', multiply)

# matrix multiplication
# mat_mul = x.dot(y)
# mat_mul = np.matmul(x,y)
mat_mul = x @ y
print(' matrix x and y \n', x, '\n', y)
print('matrix multiply \n', mat_mul)    

list1 = [('A825662','Giri',41,600063),
         ('A825663','Anand',49,600064),
         ('A825664','Karthik',31,600065),
         ('A825665','Praggnanandhaa',18,600066),
         ('A825666','Harika',24,600067)]

dtype = [('DASID','S10'),('Name','S20'),('Age',int),('Code',int)]

arr = np.array(list1, dtype=dtype)
# print(arr)

# sort based on age np.sort(arr, order='Age')
# print(np.sort(arr, order='Age'))


matA = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(matA)
transpose = matA.T
# print('transpose \n', transpose)