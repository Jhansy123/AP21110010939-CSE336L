import numpy as np

#Write a NumPy program to find the missing data in a given array.
nums = np.array([[6, 8, np.nan, 1],
                 [10, 2, 10, 9],
                 [5, np.nan, 7, np.nan]])

print("Original array:")
print(nums)

#the missing data (NaN) in the array using np.isnan()
#returns a boolean array of the same shape as 'nums', where True represents NaN values
print("\nFind the missing data of the said array:")
print(np.isnan(nums)) 
