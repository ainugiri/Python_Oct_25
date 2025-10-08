# collection of items

# To create a list:  [ , , , , , ]


my_list1 = list()  # empty list
print(type(my_list1))

my_list2 = []      # empty list
print(type(my_list2))

my_list3 = [10, 20, 30, 40, 50]
print(type(my_list3))


purchase= ['apple', 'banana', 'grapes', 'orange', 'kiwi', 'apple']
print(type(purchase))
print(purchase)  # ['apple', 'banana', 'grapes', 'orange', 'kiwi', 'apple']
print(purchase[2])  # grapes

# add, delete, update
# add -> append(), insert(), extend()

# append() -> add item at the end of the list

purchase.append('watermelon')
print(purchase)  # ['apple', 'banana', 'grapes', 'orange', 'kiwi', 'apple', 'watermelon']


# insert(index, value) -> add item at the specified index
purchase.insert(2, 'mango')
print(purchase)  # ['apple', 'banana', 'mango', 'grapes', 'orange', 'kiwi', 'apple', 'watermelon']

# extend() -> add multiple items at the end of the list
purchase.extend(['papaya', 'pear', 'peach'])
print(purchase)  # ['apple', 'banana', 'mango', 'grapes', 'orange', 'kiwi', 'apple', 'watermelon', 'papaya', 'pear', 'peach']

# delete -> remove(), pop(), clear(), del
# remove(value) -> remove the first occurrence of the specified value

purchase.remove('apple')
print(purchase)  # ['banana', 'mango', 'grapes', 'orange', 'kiwi','apple', 'watermelon', 'papaya', 'pear', 'peach']

# pop
purchase.pop()  # removes the last item
print(purchase)  # ['banana', 'mango', 'grapes', 'orange', 'kiwi','apple', 'watermelon', 'papaya', 'pear']

purchase.pop(3)  # removes the item at index 3
print(purchase)  # ['banana', 'mango', 'grapes', 'kiwi','apple', 'watermelon', 'papaya', 'pear']

del purchase[4]  # removes the item at index 4
print(purchase)  # ['banana', 'mango', 'grapes', 'kiwi', 'watermelon', 'papaya', 'pear']


print(my_list3 + purchase)
my_list2.extend([1,2])
print(my_list2)  # [1, 2]
print(my_list2 + purchase)  # [1, 2, 'banana', 'mango', 'grapes', 'kiwi', 'watermelon', 'papaya', 'pear']

print(my_list2 * 2)


mylist1 = [10,20,30,40,50]
print(len(mylist1))  # 5
print(mylist1)       # [10, 20, 30, 40, 50]
print(mylist1[1:4])   # [20, 30, 40]
print(mylist1[:2])  # [10, 20]
print(mylist1[:4])  # [10, 20, 30, 40]
print(mylist1[::2])  # [10, 30, 50]
print(mylist1[::-1])  # [50, 40, 30, 20, 10]


for value in purchase:
    print(value)

for i in range(len(purchase)):      #len : 5, range(5) -> 0,1,2,3,4
    print(purchase[i])


purchase.append('banana')
purchase.remove('papaya')
purchase.reverse()
print(purchase)  # ['pear', 'papaya', 'watermelon', 'kiwi', 'grapes', 'mango', 'banana', 'banana']


purchaselist1 = purchase.copy()
print(purchaselist1)  # ['pear', 'watermelon', 'kiwi', 'grapes', 'mango', 'banana', 'banana']

del mylist1
del my_list1
del my_list2
del my_list3

print(purchase)
purchase[2]='blueberry'
print(purchase)

