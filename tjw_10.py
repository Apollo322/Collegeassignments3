a = int(input("请输入学生人数："))
grades = [int(input("请输入学生成绩："))for i in range(a)]
print(grades)
max_value = int(max(grades))
print("最高分: %d"%max_value)
min_value = int(min(grades))
print("最低分：%d"%min_value)
sum_value = sum(grades)
print("总分：%d"%sum_value)
