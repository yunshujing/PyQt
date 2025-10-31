"""
题目1：输入半径r，计算圆的面积和周长
"""
import math

r = float(input("请输入圆的半径r: "))
# 计算面积和周长
area = math.pi * r ** 2
zc = 2 * math.pi * r
# 输出结果
print(f"圆的面积为: {area:.2f}")
print(f"圆的周长为: {zc:.2f}")

