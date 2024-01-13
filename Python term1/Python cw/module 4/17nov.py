# #take random data
# import numpy as np
# data=np.random.randn(2,3)
# print(data)

#math operation of the data
#2 and 3 are row s and column
# import numpy as np
# data=np.random.randn(2,3)  #will take form 0 and 1 i.e mean values
# print(data)
# print(data*10)
# print(data+data)
# # a dtype, an object describing the data type of the array
# print(data.dtype)

#Creating ndarrays
#create an array
# this accepts any sequence-like objects(including other arrays)and produces a new Numpy array containing the passed data
# import numpy as np
# data=[6,7.5,8,0,1]
# arr=np.array(data)
# print(arr)

#nested sequences,like a list of equal-length lists,will be converted into a  multidimenional array:
# import numpy as np
# data2=[[1,2,3],[4,5,6]]
# ar1=np.array(data2)
# print(ar1)


# print(ar1.ndim)
# print(arr1.shape)
# print(arr1.dtype)

#there are no of other funtio
#1D
# import numpy as np
# print(np.zeros(10))

# #2D
# print(np.zeros((3,6)))

#data types
#data types for ndarrays
# import numpy as np
# ar1=np.array([1,2,3],dtype=np.float64)
# print(ar1,ar1.dtype)

# ar2=np.array([1,2,3],dtype=np.int32)
# print(ar2,ar2.dtype)

#convert or cast
# converting or cast an array from one dtype to another using ndarray's astype method
# import numpy as np
# arr=np.array([1,2,3,4,5])
# print(arr,arr.dtype)
# float_arr=arr.astype(np.float64)
# print(float_arr,float_arr.dtype)


#numpy.string_type.as string data in NumPy is fixed size and may turncate without warning
# import numpy as np
# numeric_strings=np.array(['1.25','9.6',42],dtype=np.string)
# print(numeric_strings.astype(float))
# print(numeric_strings.dtype)


#Basic indexing and slicing
# import numpy as np
# arr=np.arange(10)
# print(arr[5])
# print(arr[5:8])


# arr[5:8]=12
# print(arr)
# arr_slice=arr[5:8]
# print(arr_slice)
# arr_slice[1]=12345
# print(arr_slice)

#in 2d array the elements at each index are no longer scalars but rather 1d arrays
# import numpy as np
# arr2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr2d[2])

# print(arr2d[0][2])      #or arr2d[0,2]


# ar=([[1,2,3],[4,5,6],[7,8,9]])
# #print(ar[:2])       #printing till 1st row here only
# #ar([:2])
# print(ar[:2,1:])         #row and column


import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr[:2,1:])
# print(arr[1, 2:4])
# print(arr[:,1])
# print(arr[2:,2:])
# print(arr[1::2, ::2])
w,v=np.linalg.eig(arr)
print(w)
print(v)