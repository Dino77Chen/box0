my_dic = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}
my_dic_1 = {"k": "gg", "k2": "yy"}
my_dic_list = [{"k3": "mm"}, {"k4": "jj", "k5": "qq"}]

print(my_dic[1])
print(my_dic)
print(my_dic[1][2])

my_dic[2] = my_dic[3]
print(my_dic)

my_dic[3] = 'abc'
print(my_dic)

# 错误
# my_dic[2] = my_dic[3] + 1

my_dic.update(my_dic_1)
print(my_dic)
my_dic.update(my_dic_list[1])
print(my_dic)

my_list = [x for x in range(1, 6)]
print(my_list)

for i in my_list:
    print(my_dic[i])
