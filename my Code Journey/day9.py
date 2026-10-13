# 1.奇数和偶数判断
num = int(input("请输入数字："))
if num % 2 != 0: 
    print("奇数")
else :
    print("偶数")

# 2.是否有成年
age = int(input("请输入年龄："))
if age >= 18:
    print("已经成年")
else:
    print("未成年")

# 3.该数字是正数还是负数
num1 = int(input("请输入数字："))
if num1 > 0:
    print("正数")
else:
    print("负数")       

# 4.分数是否及格
score = int(input("请输入分数："))
if score >= 60:
    print("及格")
else:
    print("不及格")
