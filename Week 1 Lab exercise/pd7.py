import pandas as pd

#Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels.
data = {
    'Name': ['Quinn', 'Bethany', 'Joe', 'Marienne'],
    'Age': [20, 19, 20, 19],
    'City': ['India', 'Paris', 'Seoul', 'Los Angeles']
}
index_labels = ['Person1', 'Person2', 'Person3', 'Person4']
df = pd.DataFrame(data, index=index_labels)

print(df)
