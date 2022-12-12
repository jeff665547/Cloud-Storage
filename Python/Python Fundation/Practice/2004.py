AA = []
BB = []

for i in range(0, 3):
    A = input()
    A = A.split(" ")
    Ai = []
    for j in range(0, 3):
        Ai.append(eval(A[j]))
    AA.append(Ai)

for i in range(0, 3):
    B = input()
    B = B.split(" ")
    Bi = []
    for j in range(0, 3):
        Bi.append(eval(B[j]))
    BB.append(Bi)


def matrixproduct(AA, BB):
    CC = []

    def smatrixproduct(AA, BB):
        Sum = 0
        for i in range(len(AA)):
            x = AA[i]*BB[i]
            Sum += x
        return(Sum)
    
    def t(BB):
        DD = []
        for i in range(len(BB[0])):
            Di = []
            for j in range(len(BB)):
                Di.append(BB[j][i])
            DD.append(Di)
        return(DD)
    
    EE = t(BB)
    
    for i in range(0, len(AA)):
        Ci = []
        for j in range(0, len(EE)):
            Ci.append(smatrixproduct(AA[i], EE[j]))
        CC.append(Ci)

    for i in range(len(CC)):
        for j in range(len(CC[i])):
            if (j !=len(CC[i])-1 ):
                print("%-5d"%(CC[i][j]), end = "")
            else:
                print("%-5d"%(CC[i][j]))
        
CC = matrixproduct(AA, BB)
