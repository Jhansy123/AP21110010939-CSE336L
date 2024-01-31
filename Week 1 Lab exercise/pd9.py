import pandas as pd

#Write a Pandas program to append a new row &#39;k&#39; to data frame with given values for each column. Now delete the new row and return the original DataFrame.
data = {'Name': ['Betty','Veronica','Archie','Reggie']}
df = pd.DataFrame(data)

new_row_values = {'Name': 'Andy'}
df = pd.concat([df, pd.DataFrame([new_row_values])], ignore_index=True)

print("DataFrame with New Row:")
print(df)

df = df.drop(df[df['Name'] == 'Andy'].index)

print("\nOriginal DataFrame after Deleting 'Andy':")
print(df)
