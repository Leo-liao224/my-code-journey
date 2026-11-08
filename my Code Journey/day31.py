# 函数
def out_line():
    print("This is a line of output.")
    print("This is another line of output.")

out_line()
out_line()
out_line()




def circle_area(r):
    area = 3.14 * r ** 2
    return area

print(circle_area(5))


def rectangle_area(length, width):
    area = length * width
    return area

print(rectangle_area(5, 3))


def circle_area_len(r):
    """
    橘子神c的代码
    """
    help(circle_area_len)
    return round(3.14*r*r, 1), round(2*3.14*r, 1)

print(circle_area_len(3))
area, length = circle_area_len(3)
print(area)


# 函数的嵌套调用

def function_a():
    print("a ... before")
    function_b()
    print("a ... after")

def function_b():
    print("b ... before")
    function_c()
    print("b ... after")

def function_c():
    print("c ...")

function_a()

print("函数调用完毕 ~")




# 案例
# 1.三角形面积
def triangle_area(base, height):
    return base * height/2

print(triangle_area(2, 3))

# 2.计算元音字母个数
def count_aeiou(s):
    """
    计算字符串中元音字母的个数
    """
    num = 0
    for w in s:
        if w in "aeiouAEIOU":
            num += 1
    return num

print(count_aeiou("Hello, World!"))


# 3.计算成绩最高分和最低分，平均分
def score_statistics(scores):
    """
    计算成绩的最高分、最低分和平均分
    """
    max_score = max(scores)
    min_score = min(scores)
    avg_score = sum(scores) / len(scores)
    return max_score, min_score, avg_score

print(score_statistics([85, 92, 78, 90, 88]))