import numpy as np

# random number generation 
# a = np.random.randint(low = 20, high = 50, size = 10)
a = np.random.randint(0, 100, (3,3,4))
print(a)



print(np.random.randint(10))

print('Multiplication of 121, 139 is', np.multiply(121, 139))

print(' Square root of 121 is', np.sqrt(121))
print('13 to the power 3 is', np.power(13, 3))
print('log of 2 is', np.round(np.log(2),2))
print('exponential of 2 is', np.round(np.exp(2),3))
print('sin 90 is', np.round(np.sin(90),2))
a = np.random.randint(0, 100, 12)
print(a)
print('minimum value is', np.min(a))
print('maximum value is', np.max(a))
print('sum is', np.sum(a))
print('mean is', np.mean(a))
print('median is', np.median(a))
print('standard deviation is', np.std(a))   
