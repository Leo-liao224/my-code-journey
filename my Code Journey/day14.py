"""# for 循环
import time
msg = input("请输入字符串：")
for i in msg:
    print(f"变量：{i}")
    time.sleep(0.1)
else:
    print("结束")


# 100以内的奇数之和
total = 0
for i in range(1,101):
    if i % 2 == 1:
        total += i
print(f"总数：{total}")


# 简化
total = 0
for i in range(1,101,2):
        total += i
print(f"总数：{total}")
"""
# 计算100到500之间所有3的倍数的数字之和
num = 0
for i in range(100,501):
    if i % 3 == 0:
        num += i
print(f"总数：{num}")
