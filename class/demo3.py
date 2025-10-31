print("打折活动")
xq=input("请输入星期几:")
time=int(input("请输入时间:"))
if (xq=="星期二") and (time>=10 and time<=11) or (xq=="星期五" and time<=17):
    print("恭喜你")
else:
    print("谢谢惠顾")