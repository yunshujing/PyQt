"""
题目2：编写程序，判断今年是闰年还是平年，并将结果输出
"""

year = int(input("请输入今年年份: "))
# 判断闰年和平年
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year}年是闰年")
else:
    print(f"{year}年是平年")

