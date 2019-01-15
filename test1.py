# 输出类型
# print(type(8))
#判断是不是整数
"""
# if else
#判断是不是整数
number=input("请输入一个整数：")
num=int(number)
# 记得if else后加：
if num%2==0:
    print("是整数")
    if num % 3==0:
        print ("也能被3整除")
else:
    print("不是整数")
"""
# 判断成绩的等级
'''
# 判断成绩的等级
score=input("输入成绩：")
# 判断空字符串
if score !="":
    score=int(score)
    if 0<=score <=100:
        if score ==100:
            print("s")
        elif score>90:
            print("a")
        elif score>80:
            print("b")
        elif  score>70:
            print("d")
        elif score>60:
            print("e")
        else:
            print("f")
    else:
        print("有误")
else:
    print("没输入内容")
'''
# 判断闰年
'''
# 判断闰年
year=input("输入年份：")
if year:
    y=int(year)
    if (y%400==0)or(y%4==0 and y %100!=0):
        print("是闰年")
    else:
        print("不是闰年")
else:
    print("输入无效")
'''
# 分别输入各位上的数
'''
number=input("请输入1-99999的数：")
n=int(number)
n1=n%10
n10=n//10%10
n100=n//100%10
n1000=n//1000%10
n10000=n//10000%10
print(f"个位{n1}十位{n10}百位{n100}千位{n1000}万位{n10000}")
'''
# 猜拳
import random
number =random.randint(1,3)
user_number=input("1.剪刀\n2.石头\n3.布\n请输入一个值：")
user_number=int(user_number)
print(f"电脑{number}")
if number==user_number:
    print("pingle")
else:
    if user_number>number and not (user_number==3and number==1):
        print("you win")
    elif user_number==1 and number==3:
        print("youwin")
    else:
        print("youlose")

