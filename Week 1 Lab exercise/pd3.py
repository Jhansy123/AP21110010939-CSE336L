import pandas as pd

#Write a Pandas program to display most frequent value in a given series and replace everything else as &#39;Other&#39; in the series.
my_series = pd.Series([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
most_frequent_value = my_series.mode().iloc[0]
my_series = my_series.apply(lambda x: most_frequent_value if x == most_frequent_value else 'Other')

print(my_series)
