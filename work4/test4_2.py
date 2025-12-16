"""
题目2：使用函数求特殊数列和
给定两个均不超过9的正整数a和n,要求编写函数fn(a,n),
求a+aa+aaa+….+aa…aaa(n个a)之和,fn须返回的是数列和。
"""

def fn(a, n):
    total_sum = 0
    current_number = 0
    
    for i in range(1, n + 1):
        current_number = current_number * 10 + a
        total_sum += current_number
    
    return total_sum


# 主程序
if __name__ == "__main__":
    try:
        a = int(input("请输入数字a (1-9): "))
        n = int(input("请输入项数n (不超过9): "))
        
        if a < 1 or a > 9:
            print("错误：a必须在1-9之间")
        elif n < 1 or n > 9:
            print("错误：n必须在1-9之间")
        else:
            result = fn(a, n)
            print(f"数列和为: {result}")
            
            # 显示数列
            numbers = []
            current = 0
            for i in range(1, n + 1):
                current = current * 10 + a
                numbers.append(str(current))
            print(f"数列: {' + '.join(numbers)} = {result}")
            
    except ValueError:
        print("输入错误，请输入有效的整数！")

