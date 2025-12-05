# 题目1：删除字符串左右两边的空格，中间连续空格保留一个

s = " This  is  a  test  "
print(f"原字符串: '{s}'")

result = ' '.join(s.strip().split())
print(f"处理后: '{result}'")







# 方法1：使用strip()和split()+join()
# strip()删除左右空格，split()按空格分割（自动处理连续空格），join()用单个空格连接

# 方法2：使用正则表达式
# import re
# s2 = " This  is  a  test  "
# result2 = re.sub(r'\s+', ' ', s2.strip())
# print(f"正则处理后: '{result2}'")
