import numpy as np

def separator():
    print('----------------------')

# create an array of 10 zeros
arr = np.zeros(10)
print(arr)
separator()

#create an array of 10 ones
arr = np.ones(10)
print(arr)
separator()

# create an array of 10 fives
arr = np.ones(10)
print(arr * 5)
separator()

# create an array of integers from 10 to 50
arr = np.arange(10, 51)
print(arr)
separator()

# create 3*3 matrix with values ranging from 0 to 8
arr = np.arange(0, 9)
arr_2d = arr.reshape((3, 3))
print(arr_2d)
separator()

# creaste 3*3 identity matrix
arr = np.eye(3)
print(arr)
separator()

# generate 25 random numbers sampled from a normal distribution
arr = np.random.randn(25)
print(arr)
separator()

# create a matrix
arr = np.arange(1, 101).reshape(10, 10)
print(arr)
print(arr / 100.0)


# create an array of 20 linerarly points between 0 and 1
arr = np.linspace(0, 1, 20)
print(arr)
separator()

# reprouduce
arr = np.arange(1, 26).reshape(5, 5)
print(arr)
arr_filtered = arr[2:, 1:]
print(arr_filtered)
separator()

# get the number of 20
print(arr[3][4])
separator()

# select
arr_filtered = arr[:3, 1:2]
print(arr_filtered)
separator()

# select
arr_filtered = arr[4:, :]
print(arr_filtered)
separator()

#select
arr_filtered = arr[3:, :]
print(arr_filtered)
separator()

# get the sum of the arr
print(np.sum(arr))
separator()

# get the standard deviation of arr
print(np.std(arr))
separator()

# get the sum of all rows in arr
print(arr.sum(axis = 0))
separator()
