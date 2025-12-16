# 4、输入一行字符，求字符"a","b"和"c"出现的次数

# 输入一行字符
text = input("请输入一行字符：")

# 统计a、b、c出现的次数
count_a = text.count('a')
count_b = text.count('b')
count_c = text.count('c')

# 输出结果
print(f"字符'a'出现的次数：{count_a}")
print(f"字符'b'出现的次数：{count_b}")
print(f"字符'c'出现的次数：{count_c}")


