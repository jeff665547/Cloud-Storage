score = [[76, 73, 85],
         [88, 84, 76],
         [92, 82, 92],
         [82, 91, 85],
         [72, 74, 73]]

def listinfo(score):
    All = []
    for i in range(0, len(score)):
        All.append([sum(score[i]), "%.2f" %(sum(score[i])/len(score[i])), len(score[i])])
    return(All)    
    
output = listinfo(score)

for i in range(0, len(score)):
    print("student", i+1)
    for j in range(0, len(score[i])):
        print(" ", j+1,": ", score[i][j], sep ="")
    print(" sum:", output[i][0])
    print(" avg:", output[i][1])

total = 0
n_score = 0
highlist = []

for i in range(0, len(output)):
    highlist.append(eval(output[i][1]))
    total += output[i][0]
    n_score += output[i][2]
    
highdict = dict(zip(tuple(highlist), (1,2,3,4,5)))
highdict[max(highlist)]

totalavg = total/n_score
print("total: ", total, ", avg: ","%.2f" %(totalavg), sep = "")
print("highest avg: ","student ", highdict[max(highlist)],": ","%.2f" %(max(highlist)), sep = "")