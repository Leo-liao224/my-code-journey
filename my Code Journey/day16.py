"""# 嵌套循环案例:打印99乘法表
for i in range(1,10): # 行
    for j in range(1,i+1):  # 列
        print(f"{i} x {j} = {i * j}",end="\t")
    print()
"""
"""
# 1.打印等腰直角三角形，例如10
import time
n = int(input("请输入数字："))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(f"*",end="  ")
        time.sleep(0.1)
    print()
"""
"""
# 2.输入数字，打印金字塔
num = int(input("请输入数字："))
for i in range(1,num+1):
    print()
    for j in range(1,i+1):
        print(j,end="     ")
    print()
"""


# 3.国际象棋
for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            print(0,end="")
        else:
            print(1,end="")
    print()