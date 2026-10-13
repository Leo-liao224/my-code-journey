score = 700
if score > 680:
    print("欢迎你来到清华")




ok_account = "13631230127"
ok_password = "1234567890"



# 1.提示用户输入账号和密码
account = input("请输入账户号码：")
password = input("请输入密码：")

# 2.判断账号和密码是否正确，如果账号和密码都正确，则登陆成功，进入b站首页

if ok_account == account and ok_password == password:
    print("密码输入正确，欢迎")


# 3.如果账号和密码有一个错误，则登录失败，提示错误信息
if ok_account !=account or ok_password != password:
    print("账户或密码输入错误，请重试")