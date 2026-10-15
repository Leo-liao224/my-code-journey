# if elif else---> 用户名和密码：juzishen/123123或juzishen/123456或juzisheng/13631230127
username = input("请输入用户名：")
password = int(input("请输入密码："))

if username == username and password == 123123:
    print("登陆成功")
elif username == username and password == 123456:
    print("登陆成功")
elif username == username and password == 13631230127:
    print("登陆成功")
else:
    print("登录失败，密码或用户名错误")
    