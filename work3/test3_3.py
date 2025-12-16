# 3、用python中的字典来编程，输入一个1到7的数字，输出对应的星期名的缩写

# 定义星期字典
week_dict = {
    1: 'Mon',
    2: 'Tue',
    3: 'Wed',
    4: 'Thu',
    5: 'Fri',
    6: 'Sat',
    7: 'Sun'
}

# 输入数字
num = int(input("请输入一个1到7的数字："))

# 输出对应的星期缩写
if num in week_dict:
    print(f"对应的星期名缩写是：{week_dict[num]}")
else:
    print("输入错误！请输入1到7之间的数字。")


