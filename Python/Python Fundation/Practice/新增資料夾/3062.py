AA = []

for i in range(5, 0, -1):
    AA.append(i)
    print("data", i)
print()
for i in range(5, 0, -1):
    i = AA.pop()
    print("data", i)


