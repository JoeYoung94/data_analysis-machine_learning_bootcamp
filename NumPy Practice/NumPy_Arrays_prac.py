import numpy as np

def separator():
    print('----------------------')

# casting a normal python list into an array
separator()
my_list = [1, 2, 3, 4, 5, 6]
arr = np.array(my_list)
print(type(arr))
print(arr)
separator()

# arange
# generating an array from the start number to the end number, with step numbers
arr = np.arange(0, 11, 1) # 1 is optional
print(type(arr))
print(arr)
separator()

# zeros, ones
# generate 1D zeros
arr = np.zeros(5)
print(type(arr))
print(arr)
# generate 2D ones
arr = np.ones((5, 5)) # note: it must be tuple in the brackets
print(type(arr))
print(arr)
separator()


# linspace
# generate n numbers in the range of (low, high)
arr = np.linspace(0, 10, 5)
print(type(arr))
print(arr)
separator()

# .eye()
# generating n*n matrix
arr = np.eye(3)
print(type(arr))
print(arr)
separator()

# random methods
print(np.random.rand(5)) # 1D random array with 5 elements from 0 to 1
#print(np.random.rand((5, 4))) # 2D random matrix (5 * 4)

print(np.random.randn(2))
#print(np.random.randn((4, 4)))

print(np.random.randint(0, 10))  # returns a single random number
print(np.random.randint(0, 10, 3)) # returns an array of random numbers
separator()

# reshape
# converting 1D to 2D n*N matrix
arr = np.arange(0, 25)
print(type(arr))
print(arr)

arr_new = arr.reshape(5, 5)
print(type(arr_new))
print(arr_new)
separator()

# max() and min()
arr = np.random.randint(0, 100, 5)
print(arr)
print(arr.max())
print("The index of the max number is {a}".format(a = arr.argmax()))
print(arr.min())
print("The index of the min number is {}".format(arr.argmin()))
separator()

# shape function
arr = np.arange(0, 25)
print(arr)
arr_2d = arr.reshape(5 , 5)
print(arr_2d)
# shape
print(arr_2d.shape)
separator()

# dtype: data type
arr = np.random.randint(0, 100, 5)
print(arr)
print(arr.dtype)
separator()

# alternative for np.random.randint:
from numpy.random import randint as ri
print(ri(2, 10, 3))
separator()
