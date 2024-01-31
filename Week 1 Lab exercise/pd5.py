import pandas as pd

#Write a Pandas program to calculate the number of characters in each word in a given series.
my_series = pd.Series(['January', 'February', 'March', 'April', 'May'])
word_lengths = my_series.str.len()

print("Original Series:")
print(my_series)

print("\nNumber of characters in each word:")
print(word_lengths)
