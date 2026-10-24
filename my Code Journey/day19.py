"""# 列表
s = [10,11,12,13,14,15,16]
s[0] = 50
s[-1] = 0
del s[1]
s[2] = "人"
print(s)
"""


"""
s = ["橘","子","神","真","强",]
print(type(s))
print(s[:5:2])
"""



"""
s = [10,11,12,13,14,16,9,55,44,75]

s.append(500) # 追加末尾
print(s)

s.insert(1,3) # 插入
print(s)

s.remove(16) # 移除
print(s)

s.pop(-1) # 弹出
print(s)

s.sort() # 排序
print(s)

s.reverse() # 反转
print(s)
"""

"""

# 1.定义列表
num_list = []

# 2.输入10个数字
for i in range(10):
    num = int(input("请输入数字："))
    num_list.append(num)
print("数字列表：", num_list)

# 3.排序
num_list.sort()
print("排序后数字列表：",num_list)

# 4.最值，平均值
print("最小值: ", num_list[0])
print("最大值: ", num_list[-1])
print("平均值: ", sum(num_list)/len(num_list))
"""

"""
# 1.合并列表
num_list1 = [11,25,14,29,18,38,17,18,19]
num_list2 = [17,12,14,15,19,18,17,13,14]

for num in num_list2:
    num_list1.append(num)
print("合并后的列表：",num_list1)

# 2.去除重复记录
new_list = []
for num in num_list1:
    if num not in new_list:
        new_list.append(num)
    print("新列表：",new_list)
    new_list.sort()
"""
"""
# 简化版(解包)
num_list1 = [11,25,14,29,18,38,17,18,19]
num_list2 = [17,12,14,15,19,18,17,13,14]

new_list = [*num_list1,*num_list2]

new_list1 = [] 

for num in new_list:
    if num not in new_list1:
        new_list1.append(num)
    print("新列表：",new_list1)
    new_list1.sort()
"""






# 1到20的偶数的平方
num_list = [i**2 for i in range(1,21)]
print(num_list)

# 提取整数中的偶数，计算平方，组成一个新的列表
num_list1 = [11,22,15,18,36,17,59,52,56,58,54,26]
new_list = [i**2 for i in num_list1 if i % 2 == 0]
print(new_list)