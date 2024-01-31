import pandas as pd

#Write a Pandas program to replace the &#39;qualify&#39; column contains the values &#39;yes&#39; and &#39;no&#39; with True and False.
data = {
    'Name': ['Rue','Jules','Maddy','Cassie'],
    'Qualify': ['yes', 'no', 'yes', 'no']
}
df = pd.DataFrame(data)
df['Qualify'] = df['Qualify'].replace({'yes': True, 'no': False})

print("DataFrame after replacing 'qualify' values:")
print(df)
