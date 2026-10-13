import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('scores.csv')


plt.figure(figsize=(10,6))

plt.scatter(df['student_id'], df['math'], label='Math', alpha=0.8)
plt.scatter(df['student_id'], df['python'], label='Python', alpha=0.8)
plt.scatter(df['student_id'], df['database'], label='Database', alpha=0.8)

plt.xlabel('student_ID')
plt.ylabel('Score')
plt.title('Scores in scattered plot')

plt.legend()
plt.savefig('scattered.png')
plt.close

fig, axes = plt.subplots(1, 3)
axes[0].hist(df['math'])
axes[1].hist(df['python'])
axes[2].hist(df['database'])
plt.savefig('histo.png')
plt.close()


plt.figure()
df[['math', 'python', 'database']].boxplot()
plt.savefig('box.png')
plt.close()