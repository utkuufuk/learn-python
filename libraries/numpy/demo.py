from numpy import *

# numpy arrays are more efficient than python lists
a = array([1, 2, 3, 4])
b = array([5, 6, 7, 8])

# array info
print(type(a))                                                  # array type
print(a.dtype)                                                  # element data type
print(a.itemsize)                                               # bytes per element
print(a.size)                                                   # array size
print(a.nbytes)                                                 # number of bytes in memory
print(a.shape)                                                  # array dimensions
print(a.ndim)                                                   # number of array dimensions

# elementwise operations
print(a * b)                
print(a + b)

# cross product
print(a @ b)

# find elements by condition
print(where(a % 2 == 0))

# 2D arrays
c = array([[2, 3, 4], [6, 7, 8]])                               # 2D array with 2 rows & 3 cols
d = arange(30).reshape(5, 6)                                    # create a 2D array with 5 rows & 6 cols
print(d[-1, -1])                                                # access an array element

# Array Methods
print(d.sum())                                                  # sum all elements
print(d.prod())                                                 # multiply all elements
print(d.mean())                                                 # mean of all elements
print(d.max())                                                  # max value in array
print(d.min())                                                  # min value in array
print(d.argmin())                                               # 1D index of the min value
print(d.argmax())                                               # 1D index of the max value
print(unravel_index(d.argmin(), d.shape))                       # 2D index of the min value
print(unravel_index(d.argmax(), d.shape))                       # 2D index of the max value

print(d.sum(axis=0))                                            # sum of each row
print(d.sum(axis=1))                                            # sum of each column

# read from txt file
simple_data = loadtxt('simple_data.txt')
print(simple_data)

complex_data = loadtxt('complex_data.txt', delimiter=',',
                       comments='%', usecols=(0, 1, 2, 4),
                       dtype=int, skiprows=1)
print(complex_data)

# copying arrays
x = array([1, 2, 3, 4, 5])
y = x[1:3]                                                      # modifying elements of y affects x
z = x[1:3].copy()                                               # referencing is the default behavior

q = zeros(10)                                                   # create an array of zeros
q[:len(x)] = x                                                  # copy the elements in a to the beginning of q
