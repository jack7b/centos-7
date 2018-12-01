#条件一个数，除以三余二，除以五余三，除以七余二
b =0
while b <=100:
    if b % 3 == 2 and b % 5 == 3 and b % 7 == 2:
        print("符合条件%d" %b)
        break
    else:
        print("不符合，停止运算：")
        b +=1
    
