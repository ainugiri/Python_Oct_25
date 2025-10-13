import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
np.random.seed(42)

data = {
    'Gender': np.random.choice(['M','F'], 100),
    'Sub': np.random.choice(['Math', 'Science', 'English'], 100),
    'Score': np.random.randint(45,100,100)
}
df = pd.DataFrame(data)
plt.figure(figsize=(10,6))
sns.violinplot(x='Sub', y='Score', data=df, hue='Gender', palette=['lightblue', 'lightpink'], split=True, inner='box')
sns.stripplot(x='Sub', y='Score', data=df, color='black', size=3, jitter=True, alpha=0.5)
plt.title('Violin Plot Marks Distribution')
plt.ylabel('Marks')
plt.xlabel('Subjects')
plt.grid()
plt.show()