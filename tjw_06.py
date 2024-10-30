import random
b = []
for i in range(10):
    random_num = random.randint(1,100)
    b.append(random_num)
print(b)
min_value = min(b)
print(min_value)