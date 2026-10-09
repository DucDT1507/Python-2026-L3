import pandas as pd

df_students= pd.read_csv('students.csv')
df_scores= pd.read_csv('scores.csv')

print(df_students.isnull().sum())

print(df_scores.isnull().sum())

df_students_clean = df_students.dropna()
df_scores_clean= df_scores.dropna()

merged_df= pd.merge(df_students_clean,df_scores_clean,on = 'student_id')

print(merged_df.head())

merged_df['avg_score'] = merged_df[['python', 'math', 'database']].mean(axis=1)
student_avg = merged_df[['student_id', 'name', 'avg_score']]
print(student_avg)


top_5 = student_avg.sort_values(by='avg_score', ascending=False).head(5)
print(top_5)


avg_by_major = merged_df.groupby('major')['avg_score'].mean()
print(avg_by_major)




