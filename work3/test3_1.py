# 1、用二维列表编程：使古诗横排变竖排

# 原始古诗（横排）
poem = [
    ['白', '日', '依', '山', '尽'],
    ['黄', '河', '入', '海', '流'],
    ['欲', '穷', '千', '里', '目'],
    ['更', '上', '一', '层', '楼']
]

print("原始古诗（横排）：")
for line in poem:
    print(''.join(line))

print("\n转换后的古诗：")
# 顺时针旋转90度：每一列从下往上变成新的一行
for col in range(len(poem[0])):  # 从第一列到最后一列
    for row in range(len(poem) - 1, -1, -1):  # 从最后一行到第一行
        print(poem[row][col], end='')
    print()  # 换行

