print("今有物不知其数，三三之剩二，五五之剩三，七七数之剩二，问几何\n")
for number in range(100):
    if number%3 == 2 and number%5==3 and number%7==2:
        print("答曰:这个数是",number)
        
