# 字符串
# 字符串的三种定义方式
s1 = "hello world" # 双引号
s2 = 'hello world' # 单引号
s3 = """hello world""" # 三引号
print(type(s1))
print(type(s2))
print(type(s3))




# 字符串 ---> It's very good
msg1 = "It's very good" # 双引号定义的字符串中可以包含单引号
msg2 = "It\"s very good" # 双引号定义的字符串中可以包含双引号
msg3 = 'It\'s very good' # 单引号定义的字符串中可以包含单引号
msg4 = 'It"s very good' # 单引号定义的字符串中可以包含双引号
msg5 = """It's very good""" # 三引号定义的字符串中可以包含单引号
msg6 = """It"s very good""" # 三引号定义的字符串中可以包含双引号
msg7 = "hello的意思是\"你好\"" # 双引号定义的字符串中可以包含双引号，使用转义字符\来实现
msg8 = "hello的意思是\"你好\"\n\t很高兴见到你" # 双引号定义的字符串中可以包含双引号，使用转义字符\来实现，
# \t表示制表符，\n表示换行符
print(msg1)
print(msg2)
print(msg3)
print(msg4)
print(msg5)
print(msg6)
print(msg7)
print(msg8)
print(type(msg1))
print(type(msg2))
print(type(msg3))
print(type(msg4))
print(type(msg5))
print(type(msg6))
print(type(msg7))
print(type(msg8))
print("再见", "拜拜") # 直接打印用逗号隔开