print("查询能量请输入能量来源！退出程序请输入0")
print("能量来源如下：\n生活缴费、行走捐、共享单车、线下支付、网络购票")

print()
while True:
    power =input()
    if power =="行走捐":
        print("200g")
    elif power =="生活缴费":
        print("100g")
    elif power =="共享单车":
        print("10g")
    elif power =="线下支付":
        print("20g")
    elif power == '0':#加引号是因为0是个字符串
        print("已退出！")
        break

