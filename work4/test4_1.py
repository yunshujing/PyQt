"""
题目1：写一函数，求n!,在主程序中输入n,并调用该函数，输出n! 的值！
"""

def factorial(n):
    if n < 0:
        return "错误：n必须是非负整数"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


if __name__ == "__main__":
    try:
        n = int(input("请输入一个非负整数n: "))
        result = factorial(n)
        print(f"{n}! = {result}")
    except ValueError:
        print("输入错误，请输入一个有效的整数！")

