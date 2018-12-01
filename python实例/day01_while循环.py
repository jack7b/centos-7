print("今日物不知期数，三三之数剩二，五五数之剩三，七七数之剩二，问几何")
none = True
number = 0 #计数的变量
while none:
    number += 1#计数加1
    if number%3==2 and number %5 == 3 and number % 7 == 2:#判断是否符合条件
        print("答曰：这个数是",number)#输出符合条件的个数
        none = False#将循环条件的变量赋值为否
