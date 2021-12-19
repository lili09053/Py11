import random

file = open("input.txt", "w", encoding="utf-8")

st = " "

for _ in range(10):
    st += str(random.randint(-50, 50))
    st += "\n"

file.write(st)
file.close()



file = open("input.txt", "r", encoding="utf-8")

print(max(file))