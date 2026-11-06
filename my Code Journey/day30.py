# 初始化存储学生信息的字典
students = {}

def show_menu():
    """显示菜单"""
    print("\n############################【菜单】############################")
    print("# 1. 添加学生信息  2. 修改学生信息  3. 删除学生信息")
    print("# 4. 查询学生信息  5. 列出所有学生  6. 统计班级成绩  7. 退出系统 #")
    print("##############################################################")

def add_student():
    """1. 添加学生信息"""
    name = input("请输入学生姓名：")
    if name in students:
        print(f"【{name}】已存在！")
        return
    
    try:
        chinese = float(input("请输入语文成绩："))
        math = float(input("请输入数学成绩："))
        english = float(input("请输入英语成绩："))
    except ValueError:
        print("输入错误，成绩必须是数字！")
        return
    
    students[name] = {"语文": chinese, "数学": math, "英语": english}
    print(f"添加【{name}】成功")

def modify_student():
    """2. 修改学生信息"""
    name = input("请输入要修改的学生姓名：")
    if name not in students:
        print(f"未找到【{name}】的信息。")
        return
    
    print(f"当前【{name}】的成绩为：{students[name]}")
    try:
        chinese = float(input("请输入修改后的语文成绩："))
        math = float(input("请输入修改后的数学成绩："))
        english = float(input("请输入修改后的英语成绩："))
    except ValueError:
        print("输入错误，成绩必须是数字！")
        return
    
    students[name] = {"语文": chinese, "数学": math, "英语": english}
    print(f"修改【{name}】信息成功")

def delete_student():
    """3. 删除学生信息"""
    name = input("请输入要删除的学生姓名：")
    if name in students:
        del students[name]
        print(f"删除【{name}】信息成功")
    else:
        print(f"未找到【{name}】的信息。")

def query_student():
    """4. 查询学生信息"""
    name = input("请输入要查询的学生姓名：")
    if name in students:
        info = students[name]
        print(f"【{name}】的成绩：语文:{info['语文']}, 数学:{info['数学']}, 英语:{info['英语']}")
    else:
        print(f"未找到【{name}】的信息。")

def list_all_students():
    """5. 列出所有学生"""
    if not students:
        print("系统暂无学生信息。")
        return
    
    print(f"{'姓名':<10} {'语文':<10} {'数学':<10} {'英语':<10}")
    print("-" * 40)
    for name, scores in students.items():
        print(f"{name:<10} {scores['语文']:<10} {scores['数学']:<10} {scores['英语']:<10}")

def statistics_scores():
    """6. 统计班级成绩"""
    if not students:
        print("暂无学生成绩，无法统计。")
        return
    
    # 初始化各科数据列表
    subjects = ["语文", "数学", "英语"]
    
    for sub in subjects:
        # 获取该科目的所有成绩及对应的姓名
        scores_list = [(name, info[sub]) for name, info in students.items()]
        
        # 提取纯分数列表用于计算
        just_scores = [score for name, score in scores_list]
        
        # 计算最高分、最低分、平均分
        max_score = max(just_scores)
        min_score = min(just_scores)
        avg_score = sum(just_scores) / len(just_scores)
        
        # 获取最高分和最低分的学生姓名（可能有多人同分，这里以逗号分隔）
        max_names = "，".join([name for name, score in scores_list if score == max_score])
        min_names = "，".join([name for name, score in scores_list if score == min_score])
        
        print(f"--- {sub}成绩统计 ---")
        print(f"最高分：{max_score} (学生：{max_names})")
        print(f"最低分：{min_score} (学生：{min_names})")
        print(f"平均分：{avg_score:.2f}")

def main():
    """主程序入口"""
    while True:
        show_menu()
        choice = input("请选择要执行的操作(1-7): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            modify_student()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            query_student()
        elif choice == '5':
            list_all_students()
        elif choice == '6':
            statistics_scores()
        elif choice == '7':
            print("感谢使用，再见！")
            break
        else:
            print("输入无效，请输入1-7之间的数字。")

if __name__ == "__main__":
    main()