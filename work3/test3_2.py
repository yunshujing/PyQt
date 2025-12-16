# 2、利用列表+元组来实现学生信息的输入和输出

students = []  # 用列表存储学生信息

print("请输入5个同学的学号和姓名：")
for i in range(5):
    student_id = input(f"请输入第{i+1}个同学的学号：")
    name = input(f"请输入第{i+1}个同学的姓名：")
    students.append((student_id, name))  # 用元组存储每个学生的信息

# 输出学生信息
print("\n学号\t\t姓名")
for student in students:
    print(f"{student[0]}\t{student[1]}")


