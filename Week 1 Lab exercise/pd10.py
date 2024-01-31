import pandas as pd

#Write a Pandas program to sort the DataFrame first by &#39;name&#39; in descending order, then by &#39;score&#39; in ascending order.
data = {
    'Name': ['Betty','Veronica','Archie','Reggie'],
    'Score': [85, 90, 75, 80]
}
df = pd.DataFrame(data)
df_sorted = df.sort_values(by=['Name', 'Score'], ascending=[False, True])

print("DataFrame sorted by 'Name' in descending order, then by 'Score' in ascending order:")
print(df_sorted)
