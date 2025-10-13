import pandas as pd
import matplotlib.pyplot as plt

# data = {
#     'days': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
#     'sales': [1500, 1700, 1200, 1900, 2100, 2300, 2000]
# }

# df = pd.DataFrame(data)

# days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
# sales = [1500, 1700, 1200, 1900, 2100, 2300, 2000]
# plt.bar(days, sales, color='orange')
# plt.title('Daily Sales')
# plt.xlabel('Days of the Week')
# plt.ylabel('Sales in USD')
# plt.show()


data = {
    'Days':['Weekday','Weekend','Holiday','Weekday','Weekend','Holiday','Weekday','Weekend','Holiday','Weekday'],
    'mobile_sales':[200,220,250,210,230,260,215,225,255,205],
    'laptop_sales':[150,180,200,160,190,210,155,185,205,165],
    'tablet_sales':[100,120,130,110,125,135,105,115,140,108]
}

df = pd.DataFrame(data)
avg_sales = df.groupby('Days')[['mobile_sales', 'laptop_sales', 'tablet_sales']].mean()
print(avg_sales)

plt.bar(avg_sales.index, avg_sales['mobile_sales'], width=0.2, label='Mobile Sales', color='blue', align='center')
plt.bar(avg_sales.index, avg_sales['laptop_sales'], width=0.2, label='Laptop Sales', color='green', align='edge')
plt.bar(avg_sales.index, avg_sales['tablet_sales'], width=0.2, label='Tablet Sales', color='orange', align='edge')
plt.title('Average Sales by Product Category')
plt.xlabel('Day Type')
plt.ylabel('Average Sales')
plt.legend()
plt.show()

