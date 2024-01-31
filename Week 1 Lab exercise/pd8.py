import pandas as pd

#Write a Pandas program to select the rows where the number of attempts in the examination is greater than 2.
data = {
    'Student': ['Quinn', 'Bethany', 'Joe', 'Marienne'],
    'Attempts': [1, 4, 3, 2]
}
df = pd.DataFrame(data)
selected_rows = df[df['Attempts'] > 2]

print("Original DataFrame:")
print(df)

print("\nSelected rows where the number of attempts is greater than 2:")
print(selected_rows)
