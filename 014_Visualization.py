# matplotlib - line,bar,scatter,pie,histogram
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Car_age': [1,1,1,1,1,1,
                2,2,2,2,2,2,
                3,3,3,3,3,3,
                4,4,4,4,4,4,
                5,5,5,5,5,5,
                6,6,6,6,6,6,
                7,7,7,7,7,7],
    'carPrice':[19.1,19.09,19.11,19.08,19.1,19.5,
                18.1,18.09,18.11,18.08,18.1,18.5,
                17.1,17.09,17.11,17.08,17.1,17.5,
                16.1,16.09,16.11,16.08,16.1,16.6,
                15.1,15.09,15.11,15.08,15.1,15.5,
                14.1,14.09,14.11,14.08,14.1,14.5,
                13.1,13.09,13.11,13.08,13.1,13.5]
}

df = pd.DataFrame(data)
# print(df)

# plt.scatter(df['Car_age'], df['carPrice'])
# plt.title('Car Age vs Price')
# plt.xlabel('Car Age (Years)')
# plt.ylabel('Car Price (Lakhs)')
# plt.show()


# data = {
#     'overs':[1,2,3,4,5,6,7,8,9,10],
#     'score':[12,15,21,33,34,45,70,71,92,112]
# }
# data1 = {
#     'overs':[1,2,3,4,5,6,7,8,9,10],
#     'score':[10,21,25,27,34,40,55,61,82,101]
# }
# df = pd.DataFrame(data)
# df1 = pd.DataFrame(data1)
# plt.plot(df['overs'], df['score'], marker='o',color='blue')
# plt.plot(df1['overs'], df1['score'], marker='x',color='green')
# plt.title('Overs vs Score')
# plt.xlabel('Overs')
# plt.ylabel('Score')
# plt.grid()
# for i, v in enumerate(df['score']):
#     plt.text(i, v+2, str(v), ha='center', fontsize=8, color='red')

# for i, v in enumerate(df1['score']):
#     plt.text(i, v+2, str(v), ha='center', fontsize=8, color='blue')

# plt.show()


data = {
    'DASID':['D001','D002','D003','D004','D005','D006','D007','D008','D009','D010'],
    'Age':[25,30,22,35,28,40,32,38,26,29],
    'Exp':[2,5,1,8,3,10,4,6,2,7]

}

df = pd.DataFrame(data)
plt.barh(df['DASID'], df['Age'],color='orange')
plt.title('Age Details')
plt.xlabel('Name')
plt.ylabel('Age')
for i,v in enumerate(df['Age']):
    plt.text(i,v+1,str(v), fontsize=10,color='black')
plt.show()