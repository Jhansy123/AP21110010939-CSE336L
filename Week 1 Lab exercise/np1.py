import numpy as np

#Write a NumPy program to multiply two given arrays of same size element-by-element
list1 = [1,2,3]
arr1 = np.array(list1)
print("Array 1: ")
print(arr1)
list2 = [4,5,6]
arr2 = np.array(list2)
print("Array 2:")
print(arr2)
print("Multiplication of array 1 and array 2: ")
print(np.multiply(arr1,arr2))
