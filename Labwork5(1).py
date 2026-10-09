import pandas as pd

df = pd.read_csv('students.csv')



print(df.head())

row,cols = df.shape
print(f"{row} rows, {cols} columns")

print(df[['name','GPA']])

print(df[df['GPA']>=3.5])

df_sorted = df.sort_values(by= 'GPA',ascending= False)
print(df_sorted)


avg_gpa=df.groupby('major')['GPA'].mean()
print(avg_gpa)