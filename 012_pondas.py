# pip install pandas
import pandas as pd
import numpy as np


# arr1 = np.array([112,198,167,198,151])
# print(arr1)

# convert numpy array to pandas series
# ser1 = pd.Series(arr1)
# print(ser1)

MathScore = pd.Series([112,198,167,198,151], index=['Arun','Ajay','Charlie','David','Edward'])
print(MathScore)

data = {
    'Name': ['Arun', 'Ajay', 'Charlie', 'David', 'Edward'],
    'Maths': [112, 198, 167, 198, 151],
    'Science': [122, 188, 177, 178, 161],
    'English': [132, 158, 147, 168, 191]
}
df = pd.DataFrame(data)
print(df)

# read data from csv file - store in dataframe
df1 = pd.read_csv('./training.csv')
print(df1)
print(df1.head(3))  # first 3 rows
print(df1.tail(3))  # last 3 rows   
print(df1.columns)  # all columns
print(df1.describe())  # statistical data
print(df1.dtypes)  # data types of each column
print(df1['name'])  # access single column

# filtering data
print(df1[df1['age'] < 30])  # all rows where age < 30
print(df1['name'][df1['age'] < 30])  # all rows where age < 30


data = {
    'City':['Chennai', 'Bangalore', 'Pune', 'Mumbai', 'Pune','Chennai','Pune', 'Mumbai','Pune','Pune']
}
df2 = pd.DataFrame(data)
print(df2)
print(df2['City'].unique())  # unique cities
print(df2['City'].nunique())  # number of unique cities
print(df2['City'].value_counts())


data1 = {
    'DASID': [101,102,103,104,105,106,107,108,109,110],
    'Name' : ['Arun', 'Ajay', 'Charlie', 'David', 'Edward', 'Frank', 'George', 'Harry', 'Ian', 'John'],
    'City' : ['Chennai', 'Bangalore', 'Pune', 'Mumbai', 'Pune','Chennai','Pune', 'Mumbai','Pune','Pune'],
    'Age' : [23,45,56,32,25,67,34,78,89,21] 
}

data2 = {
    'DASID' : [101,102,103,104,105,106,107,108,109,110],
    'Salary' : [25000,35000,45000,55000,65000,75000,85000,95000,105000,115000],
    'Experience' : [2,3,4,5,6,7,8,9,10,11]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print(df1)
print(df2)

df3 = pd.concat([df1, df2], axis=1)  # combine two dataframes column wise
print(df3)

df3 = pd.merge(df1, df2, on='DASID')  # combine two dataframes based on common column
print(df3)