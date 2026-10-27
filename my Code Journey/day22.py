# 邮箱验证
#方式一
# 1.接受用户邮箱
mall = input("请输入邮箱：")

# 2.判断邮箱格式
if mall.count("@") == 1 and mall.count(".") >= 1:
    print(f"{mall}是合法邮箱")
else:
    print(f"{mall}是非法邮箱")


# 方式二：运算符---> 判断字串是否在1字符串中，存在，返回True，否则，返回false
# 1.接受用户邮箱
mall = input("请输入邮箱：")

# 2.判断邮箱格式
if mall.count("@") == 1 and "." in mall:
    print(f"{mall}是合法邮箱")
else:
    print(f"{mall}是非法邮箱")
