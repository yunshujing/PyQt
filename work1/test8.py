"""
题目8：综合运用循环结构、列表实现以下程序：
（1）冒泡排序
（2）选择排序
"""

def sort1(arr):
    """冒泡排序"""
    n = len(arr)
    # 复制数组，避免修改原数组
    arrs = arr.copy()
    
    # 外层循环控制排序趟数
    for i in range(n - 1):
        # 内层循环进行相邻元素比较和交换
        for j in range(n - 1 - i):
            if arrs[j] > arrs[j + 1]:
                # 交换元素
                arrs[j], arrs[j + 1] = arrs[j + 1], arrs[j]

    return arrs


def sort2(arr):
    """选择排序"""
    n = len(arr)
    # 复制数组，避免修改原数组
    arrss = arr.copy()
    
    # 外层循环控制排序趟数
    for i in range(n - 1):
        # 找到未排序部分的最小值索引
        min_idx = i
        for j in range(i + 1, n):
            if arrss[j] < arrss[min_idx]:
                min_idx = j
        
        # 将最小值与当前位置交换
        arrss[i], arrss[min_idx] = arrss[min_idx], arrss[i]

    return arrss


if __name__ == "__main__":
    # 输入数组
    print("请输入要排序的数字 (用空格分隔): ", end="")
    alist = list(map(int, input().split()))
    print(f"\n原始数组: {alist}")
    
    # 冒泡排序
    maopao = sort1(alist)
    print(f"冒泡排序结果: {maopao}")
    
    # 选择排序
    xuanze = sort2(alist)
    print(f"选择排序结果: {xuanze}")




