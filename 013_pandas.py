import pandas as pd
list = [1,2,3,4,5]
print(list)
col1 = pd.Series(list)
print(col1)
print(col1[0])

col1 = pd.Series(list, index = ['A', 'B', 'C', 'D', 'E'])
print(col1)
print(col1['A'])
col1['C'] = 25
print(col1)

# DataFrame - multi dimensional table
data = {
    'DASID': ['A825662','A825663', 'A825664', 'A825665'],
    'Name': ['John', 'Jane',None, 'Smith'],
    'Age': [28, 34, 29, 42],
    'City':['Chennai','Pune','Mumbai','Delhi']
}
df = pd.DataFrame(data)
print(df)
# drop the row, if it is having None
# df = df.dropna()
# print(df)

# replace a value for None
df = df.fillna('Guest',inplace=False)
print(df)
print("Hello")

df = pd.read_csv('./newdata.csv')
print(df)
meanValue = df['pptime'].mean()
print(meanValue)
df['pptime'] = df['pptime'].fillna(meanValue)
print(df)
# df['name'] = df['name'].fillna('Guest')
# print(df)

df = df.dropna(subset=['name'], inplace=False)
# df['name'] = df['name'].str.lower()
# df['name'] = df['name'].str.upper()
print(df)
df['name']=df['name'].str.strip()
print(df)

df['name']=df['name'].str.replace(' ','')
print(df)


data = {
    'DASID': ['A825662','A825663','A825665', 'A825664', 'A825665','A825665'],
    'Name': ['John', 'Jane','Jane',None, 'John', 'Jane'],
    'Age': [28, 34, 29,30, 28, 29],
    'City':['Chennai','Pune','Delhi','Mumbai','Chennai','Delhi']
}
df = pd.DataFrame(data)
print(df)
print(df.duplicated(['DASID']).sum())
print(df.index[df['DASID'].duplicated()].to_list())

df.drop_duplicates(keep='first', inplace=True)
print(df)

df.drop_duplicates(subset=['DASID'], keep='first', inplace=True)
print(df)

