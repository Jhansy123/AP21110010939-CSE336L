import numpy as np

#Write a NumPy program to save a NumPy array to a text file.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.savetxt('output_array.txt', arr, fmt='%d', delimiter=',')

print("Array has been saved to 'output_array.txt'")
