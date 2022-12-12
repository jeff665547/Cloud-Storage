
N = eval(input())

if (N <= 540000):
    J = 0.05
    L = 0
elif (N <= 1210000):
    J = 0.12
    L = 37800
elif (N <= 2420000):
    J = 0.2
    L = 134600
elif (N <= 4530000):
    J = 0.3
    L = 376600
elif (N <= 10310000):
    J = 0.4
    L = 829600
else:
    J = 0.45
    L = 1345100

K = N * J
M = K - L

print(int(J*100), "%", sep = "", end = " ")
print(int(K), L, int(M), end = " ")
