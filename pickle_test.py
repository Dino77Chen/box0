import pickle

# 我们存储相关对象的文件的名称
shop_list_file = 'shop_list.data'
# 需要购买的物品清单
shop_list = ['apple', 'mango', 'carrot']

# 准备写入文件
f = open(shop_list_file, 'wb')
# 转储对象至文件
pickle.dump(shop_list, f)
f.close()

# 清除 shop_list 变量
del shop_list

# 重新打开存储文件
f = open(shop_list_file, 'rb')
# 从文件中载入对象
stored_list = pickle.load(f)
print(stored_list)
