# 元组 tuple案例
students = (
    ("5001", "王林", 85, 92, 78),
    ("5002", "李慕婉", 92, 88, 95),
    ("5003", "十三", 78, 85, 95),
)



# 1.计算学生总分，各科平均分，然后一并输出来，保留一位小数
print("学号\t姓名\t语文\t数学\t英语\t总分\t平均分")

for s in students:
    total = s[2] + s[3] + s[4]
    avg = total / 3
    print(f"{s[0]} \t {s[1]} \t {s[2]} \t {s[3]} \t {s[4]} \t {total} \t {avg:.1f}")




# 2.1获取各科成绩列表
chinese_scores = [s[2] for s in students]
math_scores = [s[3] for s in students]
English_scores = [s[4] for s in students]

# 2.2统计各科最低分,最高分，平均分，并输出
print(f"语文最低分:{min(chinese_scores)},最高分：{max(chinese_scores)},平均分：{sum(chinese_scores)/len(chinese_scores)}")

# 2.3成绩优秀者
print("优秀学生")
for s in students:
    total = s[2] + s[3] + s[4]
    avg = total / 3
    if avg > 90:
        print(f"学号:{s[0]},姓名：{s[1]}, 平均分：{avg}")