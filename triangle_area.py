import math

#设置变量底边base
print("请输入三角形的底边：")
base=float(input())

#设置变量高height
print("请输入三角形的边长：")
a=float(input())

print("请输入三角形的另一条边长：")
#设置另一个边长
c=float(input())

#设置变量面积s
p=1
s=1

if a>0.0 or c>0.0 or base>0.0:
    sum1=a+c
    sum2=a+base
    sum3=c+base
    if sum1>base and sum2>c and sum3>a :
        p=(a+c+base)/2
        s=p*(p-a)*(p-base)*(p-c)
        area=math.sqrt(s)
        print("该三角形面积为："+str(area))
    else:
        print("这不是三角形")
else:
    print("这不是三角形")






