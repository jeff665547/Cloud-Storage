AA = []
length = []
while True:
    n = input()
    if(n == "-1"):
        wall = input()
        break
    AA.append(n)
for i in range(len(AA)):
    length.append(len(AA[i]))
print(wall*(max(length)+2))
for i in range(len(AA)):
    print(wall, AA[i], " "*(max(length) - len(AA[i])), wall, sep = "")
print(wall*(max(length)+2))
