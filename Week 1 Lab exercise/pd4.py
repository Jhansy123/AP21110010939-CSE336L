import pandas as pd

#Write a Pandas program to find the positions of numbers that are multiples of 5 of a given series.
my_series = pd.Series([1, 5, 10, 15, 20, 25, 30, 35, 40])

positions_of_multiples_of_5 = my_series.index[my_series % 5 == 0]

print("Original Series:")
print(my_series)

print("\nPositions of numbers that are multiples of 5:")
print(positions_of_multiples_of_5)
