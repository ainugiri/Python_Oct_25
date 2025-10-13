import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Name': ['Giri','Steve','Rose','Anitha','Samyuksha','Stuart','Ricky','Miller','Sam','Rob'],
    'Gender': ['M','M','F','F','F','M','F','F','M','M'],
    'Progress1':[80,75,90,60,85,70,95,55,88,92],
    'Progress2':[85,70,88,65,80,75,90,60,82,95],
    'Progress3':[78,72,85,62,83,73,93,58,86,90],
    'Progress4':[82,68,89,64,81,74,91,59,84,93],
    'Progress5':[88,74,92,66,87,76,94,61,89,96]
}

df = pd.DataFrame(data)
print(df)

avg_progress = df[['Progress5']].mean().values[0]
print(f'Average Progress: {avg_progress}')
colors1 = {'M':'blue', 'F':'red'}
plt.scatter(df['Gender'], df['Progress1'], c= df['Gender'].map(colors1), edgecolors='black',marker='o')
plt.scatter(df['Gender'], df['Progress2'], c= df['Gender'].map(colors1), edgecolors='black',marker='x')
plt.scatter(df['Gender'], df['Progress3'], c= df['Gender'].map(colors1), edgecolors='black',marker='^')
plt.scatter(df['Gender'], df['Progress4'], c= df['Gender'].map(colors1), edgecolors='black',marker='s')
plt.scatter(df['Gender'], df['Progress5'], c= df['Gender'].map(colors1), edgecolors='black',marker='D')
plt.title('Average Progress')
plt.ylabel('Average Progress')
plt.xlabel('Gender')
plt.show()

# plt.scatter(df['Name'], df['Progress2'], color='blue',marker='x')
# plt.scatter(df['Name'], df['Progress1'], color='red',marker='o')
# plt.scatter(df['Name'], df['Progress3'], color='green',marker='^')
# plt.scatter(df['Name'], df['Progress4'], color='orange',marker='s')
# plt.scatter(df['Name'], df['Progress5'], color='purple',marker='D')

# for i, v in enumerate(df['Progress1']):
#     plt.text(i, v+1, str(v), ha='left', fontsize=8, color='red')
# for i, v in enumerate(df['Progress2']):
#     plt.text(i, v+1, str(v), ha='left', fontsize=8, color='blue')
# for i, v in enumerate(df['Progress3']):
#     plt.text(i, v+1, str(v), ha='left', fontsize=8, color='green')
# for i, v in enumerate(df['Progress4']):
#     plt.text(i, v+1, str(v), ha='left', fontsize=8, color='orange')
# for i, v in enumerate(df['Progress5']):
#     plt.text(i, v+1, str(v), ha='left', fontsize=8, color='purple')
# plt.xlabel('Name')
# plt.ylabel('Progress1 & Progress2')
# plt.grid()
# plt.show()

# colors1 = {'M':'blue', 'F':'red'}
# plt.figure(figsize=(10,6))
# for gender, group in df.groupby('Gender'):
#     plt.scatter(group['Progress1'], group['Progress2'], label=gender, color=colors1[gender],edgecolors='black')

# plt.title('Progress1 vs Progress2')
# plt.xlabel('Progress1')
# plt.ylabel('Progress2')
# plt.grid()
# plt.legend()
# plt.show()