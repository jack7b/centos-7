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
        
