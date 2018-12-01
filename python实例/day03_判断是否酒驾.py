print("\n 为了您和他人的安全，严禁酒后开车！")
proof = int(input("请输入每100毫升血液酒精含量"))
if proof < 20:
    print("\n 您还是不构成饮酒行为，可以开车，但要注意安全！")
else:
    if 80 >proof >=20:
        print("\n 已经达到酒后酒驾驾驶标准，请不要开车！")
    else:
        print("\n 已经达到醉酒驾驶标准，千万不要开车")
