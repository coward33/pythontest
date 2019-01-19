# 水仙花数
'''
r=[i for i in range(100,1000) if (i==(i%10)**3+((i//10%10)**3)+((i//100%10)**3))]
print(f"{r[0]}是100-1000内最小的水仙花数")
'''
# 100内的质数
'''
l=[]
for i in range(2,100):
    a=True
    for j in range(2,i-1):
        if i%j == 0:
            a=False
            break
    if a:
        l.append(i)
print(l)
'''
# 九九乘法表
'''
for i in range(1,10):
    for j in range(1,10):
        print(f"{i}*{j}={i*j:2d}",end=" ")
    print("")
'''
