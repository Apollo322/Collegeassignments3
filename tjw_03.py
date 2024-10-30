a = input("请输入一个字符串：")
b = list(reversed(a))
c = list(a)
if c == b:
    print("该字符串为回文")