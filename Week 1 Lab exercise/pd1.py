import pandas as pd

#Write a Pandas program to convert Series of lists to one Series.
series_of_lists = pd.Series([[1, 2, 3], [4, 5], [6, 7, 8]])

result_series = series_of_lists.explode()

print("Original Series of Lists:")
print(series_of_lists)

print("\nConverted Series:")
print(result_series)
