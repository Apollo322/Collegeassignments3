def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    operator = input("Choose an operator: ")

    if operator in operations:
        result = operations[operator](num1, num2)
        print(f"{num1} {operator} {num2} = {result}")
    else:
        print("输入运算符错误，退出程序")
        break