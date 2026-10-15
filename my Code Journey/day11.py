# 1.输入三角形三遍边长
a = int(input("输入边长："))
b = int(input("输入边长："))
c = int(input("输入边长："))

# 2.判断是否是三角形，三种类型，等边三角形，等腰三角形，普通三角形
if a + b > c and b + c > a and a + c > b:
    if a == b and b == c:
        print(f"{a}{b}{c}三边长构成等边三角形")
    elif a == b or b == c or a == c:
        print(f"{a}{b}{c}三边长构成等腰三角形")    
    else:
        print(f"{a}{b}{c}三边长构成普通三角形")
else:
    print(f"{a}{b}{c}三边长构成的不是三角形")