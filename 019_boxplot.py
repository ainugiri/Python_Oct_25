import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
# data = {    
#     's1':np.random.randint(45,100,100),
#     's2':np.random.randint(49,97,100),
#     's3':np.random.randint(55,90,100)
# }
# df = pd.DataFrame(data)
# print(df)

# plt.boxplot([df['s1'], df['s2'], df['s3']], labels=['CloudComputing', 'DevOps', 'GenAI'])
# plt.title('Box Plot Marks Distribution')
# plt.ylabel('Marks')
# plt.xlabel('Subjects')
# plt.grid()
# plt.show()


# sns.boxplot(data=df, palette='Set2')
# plt.title('Box Plot Marks Distribution')
# plt.ylabel('Marks')
# plt.xlabel('Subjects')
# plt.grid()
# plt.show()

data = {
    'Gender': np.random.choice(['M','F'], 200),
    'Subject': np.random.choice(['CloudComputing', 'DevOps', 'GenAI'], 200),
    'Score': np.random.randint(45,100,200)
}
df = pd.DataFrame(data)
plt.figure(figsize=(10,6))
sns.boxplot(x='Subject', y='Score', hue='Gender', data=df, palette='Set3')
plt.title('Box Plot Marks Distribution')
plt.ylabel('Marks')
plt.xlabel('Subjects')
plt.grid()
plt.show()
