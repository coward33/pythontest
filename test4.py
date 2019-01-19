# 将首字母拼接成字符串
'''
l=['Food','Moon','Loop']
r=[i[0] for i in l]
s="".join(r)
print(s)
'''
# 找出同时存在l1 l2 的元素
'''
l1=[2,4,6,8,10,12]
l2=[3,6,9,12]
r=[i for i in l1 if i in l2]
print(r)
'''
# 将元素打印在控制台
l=[1,3,5,7,9]
[print(i) for i in l]