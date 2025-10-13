import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'Days':['Weekday','Weekend','Holiday','Weekday','Weekend','Holiday','Weekday','Weekend','Holiday','Weekday'],
    'mobile_sales':[200,220,250,210,230,260,215,225,255,205],
    'laptop_sales':[150,180,200,160,190,210,155,185,205,165],
    'tablet_sales':[100,120,130,110,125,135,105,115,140,108]
}

width = 0.2
df = pd.DataFrame(data)

x = np.arange(len(df['Days'].unique())) # 0,1,2,3

plt.bar(x - width, df.groupby('Days')['mobile_sales'].mean(), width=width, label='Mobile Sales', color='blue', align='center')
plt.bar(x, df.groupby('Days')['laptop_sales'].mean(), width=width, label='Laptop Sales', color='green', align='center')
plt.bar(x + width, df.groupby('Days')['tablet_sales'].mean(), width=width, label='Tablet Sales', color='orange', align='center')
plt.xticks(ticks=x, labels=df['Days'].unique())
plt.legend()
plt.title('Average Sales by Sales Days')
plt.show()