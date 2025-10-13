import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
data = {
    'Name': ['Giri','Steve','Rose','Anitha','Samyuksha','Stuart','Ricky','Miller','Sam','Rob'],
    'GenAI_Score': np.random.randint(45,100,10),
    'CloudComputing_Score': np.random.randint(49,97,10),
    'DevOps_Score': np.random.randint(55,90,10)
}

df = pd.DataFrame(data)

df['Average_Score'] = df[['GenAI_Score', 'CloudComputing_Score', 'DevOps_Score']].mean(axis=1)
print(df)



# plt.figure(figsize=(10,6))
# plt.scatter(df['GenAI_Score'], df['CloudComputing_Score'], s=df['DevOps_Score']*10, alpha=0.1, c='blue', edgecolors='black')
# plt.title('Bubble Chart - Student Scores')
# plt.xlabel('GenAI Score')
# plt.ylabel('CloudComputing Score')
# for i, v in enumerate(df['Name']):
#     plt.text(df['GenAI_Score'][i]+0.5, df['CloudComputing_Score'][i]+0.5, v, fontsize=8)
# plt.grid()
# plt.show()


sns.scatterplot(data=df, x='GenAI_Score', y='CloudComputing_Score', size='DevOps_Score', hue='Average_Score', sizes=(20, 200), palette='viridis', alpha=0.7, edgecolor='black')
plt.title('Bubble Chart - Student Scores')
plt.xlabel('GenAI Score')
plt.ylabel('CloudComputing Score')
for i, v in enumerate(df['Name']):
    plt.text(df['GenAI_Score'][i]+0.5, df['CloudComputing_Score'][i]+0.5, v, fontsize=8)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.grid()
plt.show()