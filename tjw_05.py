import random
b = []
for i in range(10):
    random_num = random.randint(1,100)
    b.append(random_num)
print(b)
max_value = max(b)
print(max_value)