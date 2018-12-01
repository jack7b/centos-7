total= 99
for number in range(1,100):#从1开始到100
    if number % 7 == 0:
        print(number)
        continue#继续下次循环
        
    else:
        string = str(number)
        if string.endswith("7"):#判断是否以数字7结尾
            continue#继续下一次循环
        total -=1
print("从1数到99共拍腿",total,"次数")
