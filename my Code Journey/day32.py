"""# 函数进阶
# 传参变量
def reg_student(name, age, gender):
    print(f'姓名：{name}，年龄：{age}，性别：{gender}')
    return f'姓名：{name}，年龄：{age}，性别：{gender}'

reg_student("Alice", 20, "Female")
"""

# 不定长参数
# 计算这批数据最大值，最小值，平均值
def calc_data(*args):
    max_value = max(args)
    min_value = min(args)
    avg_value = sum(args) / len(args)
    return max_value, min_value, avg_value

print(calc_data(1, 2, 3, 4, 5))

# 关键字传递
def calc_data2(*args, **kwargs):
    max_value = max(args)
    min_value = min(args)
    avg_value = sum(args) / len(args)
    return max_value, min_value, avg_value, kwargs

print(calc_data2(1, 2, 3, 4, 5, name="Alice", age=20))
