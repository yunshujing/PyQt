# 题目5：用字典编程，输入一行字符，求每个字符出现的次数

# 输入一行字符
text = input("请输入一行字符: ")

# 使用字典统计每个字符出现的次数
char_count = {}

for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("\n每个字符出现的次数：")
for char, count in char_count.items():
    # 对于特殊字符（如空格）进行特殊显示
    if char == ' ':
        print(f"'空格': {count}次")
    else:
        print(f"'{char}': {count}次")






# 方法2：使用字典的get方法（更简洁）
# print("\n--- 使用get方法的实现 ---")
# char_count2 = {}
# for char in text:
#     char_count2[char] = char_count2.get(char, 0) + 1
# print(char_count2)

