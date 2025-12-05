# 题目6：生成20个1-20的随机数，剔除重复的数

import random

# 生成20个1-20的随机数
random_numbers = [random.randint(1, 20) for _ in range(20)]
print(f"生成的20个随机数: {random_numbers}")



# 方法2：保持原顺序去重（使用列表）
unique_ordered = []
for num in random_numbers:
    if num not in unique_ordered:
        unique_ordered.append(num)
print(f"\n保持原顺序去重: {unique_ordered}")
print(f"去重后的个数: {len(unique_ordered)}")

# # 方法1：使用集合剔除重复
# unique_numbers = list(set(random_numbers))
# print(f"\n方法1 - 使用集合去重: {unique_numbers}")
# print(f"去重后的个数: {len(unique_numbers)}")

# # 方法3：使用dict.fromkeys()保持顺序去重
# unique_dict = list(dict.fromkeys(random_numbers))
# print(f"\n方法3 - 使用dict.fromkeys()去重: {unique_dict}")
# print(f"去重后的个数: {len(unique_dict)}")

