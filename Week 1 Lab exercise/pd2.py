import pandas as pd

#Write a Pandas program to create a subset of a given series based on value and condition.
my_series = pd.Series([10, 20, 30, 40, 50])
condition = my_series > 30
subset = my_series[condition]

print("Original Series:")
print(my_series)

print("\nSubset based on condition (values greater than 30):")
print(subset)
