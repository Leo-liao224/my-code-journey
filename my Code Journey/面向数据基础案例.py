# """
# 采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过控制台菜单与用户交互，具体的功能如下：
#     1．添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
#         1.1 输入学生姓名、语文成绩、数学成绩、英语成绩
#         1.2 检查学生姓名是否已存在，如果学生不存在，再添加（存在则，不添加）
#         1.3 验证成绩范围（0-100分）
#         1.4 创建学生对象并添加到系统
#     2．修改学生成绩：根据输入的学生姓名，修改对应的学生成绩
#         2.1 输入要修改的学生姓名
#         2.2 根据姓名查找该学生，显示该生当前成绩信息
#         2.3 输入新的语文、数学、英语成绩
#         2.4 更新学生成绩数据
#     3． 删除学生成绩：根据输入的学生姓名，删除对应的学生成绩
#     4．查询指定学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出
#         4.1 输出格式为："姓名：张三｜语文：85 ｜数学：90 ｜英语：88 ｜总分：263"
#     5．展示全部学生成绩：展示出系统中所有学生的成绩
# """

"""
采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过控制台菜单与用户交互
功能：添加、修改、删除、查询、展示全部学生成绩
"""

# 学生类
class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    # 计算总分
    def get_total(self):
        return self.chinese + self.math + self.english

    # 返回格式化字符串（匹配输出要求）
    def __str__(self):
        return f"姓名：{self.name}｜语文：{self.chinese} ｜数学：{self.math} ｜英语：{self.english} ｜总分：{self.get_total()}"


# 教务管理系统类
class ScoreSystem:
    def __init__(self):
        # 存储学生对象的列表
        self.student_list = []

    # 1. 添加学生
    def add_student(self):
        name = input("请输入学生姓名：")
        # 检查姓名是否存在
        for stu in self.student_list:
            if stu.name == name:
                print(f"学生【{name}】已经存在，无法添加！")
                return
        # 输入并验证成绩 0~100
        try:
            chinese = int(input("请输入语文成绩："))
            math = int(input("请输入数学成绩："))
            english = int(input("请输入英语成绩："))
        except ValueError:
            print("成绩必须是数字！添加失败")
            return

        # 校验分数范围
        if not (0 <= chinese <= 100 and 0 <= math <=100 and 0 <= english <=100):
            print("成绩范围必须是0-100分！添加失败")
            return

        # 创建学生对象加入列表
        new_stu = Student(name, chinese, math, english)
        self.student_list.append(new_stu)
        print(f"✅ 学生【{name}】添加成功")

    # 2. 修改学生成绩
    def modify_student(self):
        name = input("请输入要修改成绩的学生姓名：")
        target_stu = None
        for stu in self.student_list:
            if stu.name == name:
                target_stu = stu
                break
        if target_stu is None:
            print(f"找不到学生【{name}】")
            return
        # 显示当前信息
        print("该学生当前信息：", target_stu)
        # 输入新成绩
        try:
            new_chinese = int(input("输入新的语文成绩："))
            new_math = int(input("输入新的数学成绩："))
            new_english = int(input("输入新的英语成绩："))
        except ValueError:
            print("成绩必须是数字！修改失败")
            return
        if not (0 <= new_chinese <=100 and 0 <= new_math <=100 and 0 <= new_english <=100):
            print("成绩必须在0-100之间！修改失败")
            return
        # 更新
        target_stu.chinese = new_chinese
        target_stu.math = new_math
        target_stu.english = new_english
        print(f"✅【{name}】成绩修改完成，更新后：{target_stu}")

    # 3. 删除学生
    def delete_student(self):
        name = input("请输入要删除的学生姓名：")
        for i, stu in enumerate(self.student_list):
            if stu.name == name:
                del self.student_list[i]
                print(f"✅ 学生【{name}】删除成功")
                return
        print(f"找不到学生【{name}】")

    # 4. 查询指定学生
    def query_student(self):
        name = input("请输入要查询的学生姓名：")
        for stu in self.student_list:
            if stu.name == name:
                print(stu)
                return
        print(f"找不到学生【{name}】")

    # 5. 展示全部学生
    def show_all(self):
        if len(self.student_list) == 0:
            print("系统中暂无任何学生数据")
            return
        print("===== 全部学生成绩列表 =====")
        for stu in self.student_list:
            print(stu)

    # 控制台菜单主循环
    def run_menu(self):
        while True:
            print("\n===== 教务成绩管理系统 =====")
            print("1. 添加学生成绩")
            print("2. 修改学生成绩")
            print("3. 删除学生成绩")
            print("4. 查询指定学生成绩")
            print("5. 展示全部学生成绩")
            print("0. 退出系统")
            choice = input("请输入功能编号：")
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.modify_student()
            elif choice == "3":
                self.delete_student()
            elif choice == "4":
                self.query_student()
            elif choice == "5":
                self.show_all()
            elif choice == "0":
                print("程序退出")
                break
            else:
                print("❌ 输入无效，请输入0~5之间的数字")


if __name__ == "__main__":
    system = ScoreSystem()
    system.run_menu()
