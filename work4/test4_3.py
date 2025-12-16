"""
题目3：使用函数统计指定数字的个数
本题要求实现一个统计整数中指定数字的个数的简单函数：
countdigit(number,digit), 其中number是整数，digit 为[1，9]区间内的整数。
函数countdigit应返回number 中的digit出现的次数
"""

def countdigit(number, digit):
    # 将数字转换为字符串，并取绝对值处理负数
    number_str = str(abs(number))
    digit_str = str(digit)
    
    # 统计出现次数
    count = number_str.count(digit_str)
    
    return count


# 主程序
if __name__ == "__main__":
    try:
        number = int(input("请输入一个整数: "))
        digit = int(input("请输入要统计的数字 (1-9): "))
        
        if digit < 1 or digit > 9:
            print("错误：digit必须在1-9之间")
        else:
            count = countdigit(number, digit)
            print(f"数字{digit}在{number}中出现了{count}次")
            
    except ValueError:
        print("输入错误，请输入有效的整数！")

