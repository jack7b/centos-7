print("\n----------10086查询功能------------\n")
print(" 输入1.查询当前余额\n 输入2.查询当前剩余流量\n 输入3.查询当前剩余通话\n 输入0.退出自助查询系统！")

while True:
    call = int(input())
    if call == 1:
        print("当前余额为:999")
    elif call == 2:
        print("当前剩余流量为:5G")
    elif call == 3:
        print("当前剩余通话时间为：189分钟")
    elif call == 0:
        print("退出自助查询系统！")
        
        break
