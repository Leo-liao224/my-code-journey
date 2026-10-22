# 账号和密码登录
username = input("请输入账号：")
password = input("请输入密码：")

while True:
    if username == " " or password == " ":
        print("账号和密码不能输入为空,请重新登陆")

    elif username == "橘子神c" and password == "13631230127":
        print("登陆成功")
        break 
    elif username == "橘子神c" and password == "123123123":
        print("登陆成功")
        break 
    else:
        print("账号或密码错误,请重新登陆")


