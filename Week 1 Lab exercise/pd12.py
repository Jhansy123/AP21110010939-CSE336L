import pandas as pd
import numpy as np

#Write a Pandas program to remove infinite values from a given DataFrame.
data = {
    'Name': ['Rue','Jules','Maddy','Cassie'],
    'Score': [90, np.inf, 75, -np.inf]
}
df = pd.DataFrame(data)
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df_cleaned = df.dropna()

print("Original DataFrame:")
print(df)

print("\nDataFrame after removing infinite values:")
print(df_cleaned)
