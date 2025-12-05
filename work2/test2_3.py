# 题目3：使用二维列表打印杨辉三角

# 创建二维列表
triangle = []
n = 5  # 打印5行

for i in range(n):
    row = []
    for j in range(i + 1):
        if j == 0 or j == i:
            # 每行的第一个和最后一个元素都是1
            row.append(1)
        else:
            # 其他元素等于上一行相邻两个元素之和
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
    triangle.append(row)

# 打印杨辉三角
print("杨辉三角：")
for row in triangle:
    for num in row:
        print(num, end="    ")
    print()
