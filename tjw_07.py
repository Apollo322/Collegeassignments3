list_student = []
print("请输入学生姓名：")
i = ' '
while True:
    i = input()
    if i == 'esc':
        break
    if i and i not in list_student:
        list_student.append(i)
print(list_student)