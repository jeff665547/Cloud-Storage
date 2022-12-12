
N = eval(input())
AA = input()

AA = AA.split(" ")
BB = []
for i in range(N):
    BB.append(eval(AA[i]))
sma = BB.index(min(BB))
big = BB.index(max(BB))

print(big+1, max(BB))
print(sma+1, min(BB))
