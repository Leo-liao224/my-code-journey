# 算数运算符---> + -  * / // % **

print("10+5=",10+5)
print("10-5=",10-5)
print("10*5=",10*5)
print("10/5=",10/5)

print("10//5=",10//5) # 整除，省略小数

print("10%5=",10%5) # 取余数

print("10**5=",10**5) # 幂运算，10的5次方



# 优先级--->** * / // % + -

print("10+5*2=",10+5*2) # 乘法优先于加法





# # 例子 输入x和y，计算x - y以及 x + y的结果

# x = int(input("请输入x的值:"))

# y = int(input("请输入y的值:"))

# print("x-y=",x-y)

# print("x+y=",x+y)





# 赋值运算符
num = 10


num += 10 # num = num + 10

print("num += 10 后,num =",num)

num -= 10 # num = num - 10

print("num -= 10 后,num =",num)

num *= 10 # num = num * 10

print("num*= 10 后,num =",num)

num /= 10 # num = num / 10

print("num /= 10 后,num =",num) 

num //= 10 # num = num // 10

print("num //= 10 后,num =",num)


num %= 10 # num = num % 10

print("num %= 10 后,num =",num)




# 比较运算符

print("100 == 100 吗：",100 == 100)

print("100 != 100 吗：",100 != 100)

print("100 > 100 吗：",100 > 100)

print("100 < 100 吗：",100 <100)

print("100 >= 100 吗：",100 >= 100)

print("100 <= 100 吗：",100 <= 100)





# 逻辑运算符

n = int(input("请输入数字："))  # 大于10并且小于20的数字
print(f"满足条件的有：{n}",n > 10 and n <20)

s = int(input("请输入数字：")) # 小20或者大于30的数字
print(f"满足条件的有：{s}",s <20 or s >30)

