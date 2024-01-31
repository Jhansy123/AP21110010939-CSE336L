import numpy as np

#Write a NumPy program to test whether each element of a 1-D array is also present in second array.
list1 = [1,2,3]
arr1 = np.array(list1)
print("Array 1: ")
print(arr1)
list2 = [1,2,3,4,5,6,7]
arr2 = np.array(list2)
print(arr2)
print("Comparing and checking whether each element in arr1 is in arr2: ")
print(np.in1d(arr1,arr2))
