import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
data = {
    'Gender': np.random.choice(['M','F'], 5),
    'GenAI_Score': np.random.randint(45,100,5),
    'CloudComputing_Score': np.random.randint(49,97,5),
    'DevOps_Score': np.random.randint(55,90,5),
    'Python_Score': np.random.randint(50,95,5),
    'DataScience_Score': np.random.randint(60,99,5)
}

df = pd.DataFrame(data)
print(df.head())


# plt.figure(figsize=(10,6))
# plt.title('Heatmap - Student Scores')
# sns.heatmap(df, cmap='YlGnBu', annot=True)
# plt.ylabel('Classes')
# plt.xlabel('Subjects')
# plt.show()

sns.pairplot(df, hue='Gender', palette={'M':'blue', 'F':'red'}, diag_kind='kde', markers=['o','s'])
plt.suptitle('Pairplot - Student Scores', y=1.02)
plt.show()


