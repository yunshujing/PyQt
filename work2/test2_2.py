# 题目2：输入6个评分，去掉最高最低，计算平均分，剩余评分从高到低排序

# 输入6个评分
scores = []
print("请输入6个评分：")
for i in range(6):
    score = float(input(f"请输入第{i+1}个评分: "))
    scores.append(score)

print(f"\n原始评分: {scores}")

# 找出最高分和最低分
max_score = max(scores)
min_score = min(scores)
print(f"最高分: {max_score}")
print(f"最低分: {min_score}")

# 复制列表并去掉一个最高分和一个最低分
remaining_scores = scores.copy()
remaining_scores.remove(max_score)
remaining_scores.remove(min_score)

# 计算平均分
average = sum(remaining_scores) / len(remaining_scores)
print(f"\n去掉最高分和最低分后的评分: {remaining_scores}")
print(f"最后得分（平均分）: {average:.2f}")

# 从高到低排序
remaining_scores.sort(reverse=True)
print(f"剩余评分从高到低排序: {remaining_scores}")

