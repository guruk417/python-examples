import pandas as pd

df_file1 = pd.read_csv('C:/Users/Guru/Downloads/rdd-examples-master/rdd-examples-master/data/cred_txn.csv',sep='~')
df_file2 = pd.read_csv('C:/Users/Guru/Downloads/rdd-examples-master/rdd-examples-master/data/cust_name.csv',sep='~')

print(df_file1.columns)
print(df_file2.columns)
df3 = df_file1.merge(df_file2, on='AccNum')
print(df3.groupby('AccNum')['Amount'].sum())