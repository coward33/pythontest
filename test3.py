l=list(range(100))
# print(l)
l=[]
# for循环练习
for i in range(5):
    num =input(f"请输入第{i+1}个数：")
    num=int(num)
    l.append(num)
print(f"列表为{l}")
for i in range(len(l)):
    l[i] *=2
print(f"元素都*2组成的新列表{l}")
sum=0
for i in l:
    sum=sum+i
print(f"新列表的和是{sum}")
