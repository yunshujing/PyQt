"""
题目4：特殊a串数列求和
给定两个均不超过9的正整数a,n，要求编写程序求a+aa+aaa+……+aa…..a(n个a)之和
在一行中输入不超过9的正整数a,n，在一行中按照"s=对应的和"的格式输出。
"""

a, n = map(int, input("请输入a和n (用空格分隔): ").split())
s = 0
m = 0
# 计算特殊a串数列的和
for i in range(1, n + 1):
    m = m * 10 + a
    s += m
print(f"s={s}")


