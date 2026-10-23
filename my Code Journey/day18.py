# 猜数字游戏
import random
random_num = random.randint(1,1000000)
while True:
    num = int(input("请输入数字："))
    if num > random_num:
        print("大于随机数字")
    elif num < random_num:
        print("小于随机数字")
    else:
        print("正确")
        break
    print()