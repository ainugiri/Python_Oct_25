import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

rand_numbers = np.random.randint(4,40,500)
print(rand_numbers)



# plt.hist(rand_numbers,bins=20)
# plt.title('Random Numbers Histogram')
# plt.xlabel('Value Range')
# plt.ylabel('Frequency')
# plt.show()

df = pd.DataFrame({'Score': rand_numbers})

mean_score = df['Score'].mean() 
plt.hist(df['Score'], bins=5, color='lightgreen', edgecolor='black', density=True)
plt.axvline(mean_score, color='red', linestyle='dashed', linewidth=1)
plt.show()