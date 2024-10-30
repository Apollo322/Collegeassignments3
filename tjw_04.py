a = [1,2,3,4,5]
print("正向输出为:")
for i in a:
    print(i,end = ' ')
print()
print("隔两个元素输出：")
print(a[0::2])
b = list(reversed(a))
print("逆向输出为：")
for j in b:
    print(j,end = ' ')
    