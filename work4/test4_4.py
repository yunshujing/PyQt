"""
题目4：计算身体质量指数BMI
BMI是根据体重和身高来衡量健康的一种方法。
通过以千克为单位的体重除以以米为单位的身高的平方计算出BMI。

BMI分类标准（中国16岁以上人群）：
BMI<18.5      偏瘦
18.5<=BMI<24  正常
24<=BMI<30    偏胖
30<=BMI       肥胖
"""

class BMI:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getWeight(self):
        return self.weight
    
    def getHeight(self):
        return self.height
    
    def getBMI(self):
        bmi = self.weight / (self.height ** 2)
        return bmi
    
    def getStatus(self):
        bmi = self.getBMI()
        
        if bmi < 18.5:
            return "偏瘦"
        elif bmi < 24:
            return "正常"
        elif bmi < 30:
            return "偏胖"
        else:
            return "肥胖"
    
    def displayInfo(self):
        print(f"\n===== BMI信息 =====")
        print(f"姓名：{self.getName()}")
        print(f"年龄：{self.getAge()}岁")
        print(f"体重：{self.getWeight()}千克")
        print(f"身高：{self.getHeight()}米")
        print(f"BMI值：{self.getBMI():.2f}")
        print(f"身体状况：{self.getStatus()}")
        print("=" * 20)


# 主程序
if __name__ == "__main__":
    print("欢迎使用BMI计算器")
    print("=" * 30)
    
    try:
        name = input("请输入姓名: ")
        age = int(input("请输入年龄: "))
        weight = float(input("请输入体重(千克): "))
        height = float(input("请输入身高(米): "))

        person = BMI(name, age, weight, height)

        person.displayInfo()

        status = person.getStatus()
        if status == "偏瘦":
            print("\n建议：适当增加营养摄入，保持健康饮食。")
        elif status == "正常":
            print("\n建议：保持良好的生活习惯，继续保持！")
        elif status == "偏胖":
            print("\n建议：适当控制饮食，增加运动量。")
        else:  # 肥胖
            print("\n建议：建议咨询医生，制定科学的减重计划。")
            
    except ValueError:
        print("\n输入错误，请输入有效的数值！")
    except ZeroDivisionError:
        print("\n错误：身高不能为0！")

