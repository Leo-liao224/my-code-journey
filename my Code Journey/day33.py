# 函数的参数类型
def circle_area(r):
    area = 3.14 * r ** 2
    return area

area = circle_area(10)
print(area)


def calc_score(score_list):
    max_s = max(score_list)
    min_s = min(score_list)
    avg_s = round(sum(score_list) / len(score_list), 1)
    return max_s, min_s, avg_s

s_list = [589, 609, 605, 643, 677, 455, 477, 489, 503]
max_score, min_score, avg_score = calc_score(s_list)


def add (x, y):
    return x+y

def subtract (x, y):
    return x-y

def calc(x, y, oper):
    return oper(x, y)

result = calc(10, 20, add)
print(result)
