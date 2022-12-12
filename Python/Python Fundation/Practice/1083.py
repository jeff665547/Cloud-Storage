m = eval(input())

secret = dict(zip(("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"),
                  (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26)))

AA = []
score = []

for i in range(0, m):
    n = input()
    AA.append(n.upper())
    sigma = 0
    for j in range(0, len(AA[i])):
        sigma += secret[AA[i][j]] 
    score.append(sigma)

for i in range(0, m):
    print(AA[i],"=", score[i])

final = dict(zip((score),(AA)))
inverse_final = dict(zip((AA),(score)))

if(score.count(max(score)) == 1):
    print(final[max(score)],"is the key.")
else:
    AA.sort()
    i = 0
    while True:
        if(inverse_final[AA[i]] == max(score)):
            print(AA[i],"is the key.")
            break
        else:
            i += 1
            continue
        