print(type("黑马程序员"))
name = "黑马程序员"
name_type = type(name)
print(name_type)     






# num = int("黑马")
# print(type(num))

# 字符串转整数 重点：内容会影响转换，例如内容不能包含非数字字符，否则会报错
num_type = int("123")
print(type(num_type), num_type)

# 字符串转浮点数
float_type = float("3.14")
print(type(float_type), float_type)

# 浮点数转字符串
float_to_str = str(3.14)
print(type(float_to_str), float_to_str)

# 整数转字符串
int_to_str = str(123)
print(type(int_to_str), int_to_str)

# 浮点数转整数
float_to_int = int(3.14)
print(type(float_to_int),float_to_int)

# 整数转浮点数
int_to_float = float(123)
print(type(int_to_float),int_to_float)
