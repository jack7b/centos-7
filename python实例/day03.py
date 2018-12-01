'''age = int(input("输入你的年龄"))
if age >18 :
    print("你已经成年，可以上网")
if age <18:
    print("你的年龄不到18岁，回家好好看书")

money_all =56.75 +72.91+88.50+26.37+68.51
money_all_str =str(money_all)
print("商品总金额为:"+money_all_str)
money_real = int(money_all)
money_real_str=str(money_real)
print("实收金额为:"+money_real_str)
'''
'''
Python = 95
English = 92
c = 89
sub = Python - English
avg = (Python + English +c)/3
print(sub)
print(avg)
''''
#计算BIM指数的改进版
name =input("请输入姓名：")
height = float(input("请输入身高："))
weight = float(input("请输入体重："))
bim =weight/(height*height)
print("姓名:"+str(name))
print("体重："+str(weight))
print("身高："+str(height))
print("BIM指数："+str(bim))
if bim <=18.5:
    print("您的体重过轻")
if bim >=18.5 and bim <24.9:
    print("正常范围，可以接受，注意保持")
if bim >=23.9 and bim <29.9:
    print("您的体重过重")
if bim >=29.9:
    print("您过于肥胖")
        























