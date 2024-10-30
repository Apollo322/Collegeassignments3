a = input("请输入一个字符串：")
print("第一个元素为：" + a[0])
print("最后一个元素为："+a[-1])
if len(a)%2 != 0:
    print("中间元素为："+a[len(a)//2])
print("倒数三个元素为："+a[-1]+a[-2]+a[-3])
b = list(reversed(a))
print(b)

