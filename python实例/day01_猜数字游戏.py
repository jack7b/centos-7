import random #导入随机数模块

print("-----------猜数字游戏-------------")
random = random.randint(1,10)#生成1到10之间的随机数
print("请输入1~10之间的任意一个数字：")
while True:
    guess = input()#获取输入的数字
    if int(guess)!=0 and int(guess)<random:
        print("太小，请重新输入")
    elif int(guess) != 0 and int(guess)>random:
        print("太大，请重新输入")
    elif int(guess)==random:
        print("恭喜你，你赢了，猜中的数字是：",random)
        print("--------游戏结束-----------")
        break
    elif guess == "0":
        print("退出游戏")
        break

