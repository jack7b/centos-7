print("计算1+2+3+....+100的结果：")
result = 0#保存累加结果的变量
for i in range(101):
    result += i#实现累加功能
print(result)#在循环结束时输出结果
'''使用了range()函数，该函数时Python内置的函数，用于生成一系列连续的整数，
多用于for循环语句中。
range (start,end,step)
start 起始值 从0开始
end 结束值
'''
for i in range(1,10,2):#从1开始间隔2个数范围是1~10
    print(i,end=" ")
