f = open("../app/score.csv", "r", encoding = "Big5")
#f = open("C:\\Users\\jeff\\Desktop\\ALL\\Python Fundation\\Practice\\Data\\score.csv", "r", encoding = "Big5")
txt = f.readlines()
f.close()

data = []

for i in txt:
    i = i.strip()
    data.append(i.split(","))

i = 1
scoreid = []
scoremath = []
scoreeng = []

for i in range(1, len(data)):
    scoreid.append(data[i][0])
    scoremath.append(eval(data[i][1]))
    scoreeng.append(eval(data[i][2]))
    
eng = dict(zip(scoreid, scoreeng))
math = dict(zip(scoreid, scoremath))

len(eng)
len(scoreeng)
okeng = []
okmath = []
okboth = []
for i in range(len(scoreeng)):
    if scoreeng[i] >= 60:
        okeng.append(scoreid[i])
    if scoremath[i] >= 60:
        okmath.append(scoreid[i])
    if scoreeng[i] >= 60 and scoremath[i] >= 60:
        okboth.append(scoreid[i])

okeng.sort()
okmath.sort()
okboth.sort()
print(okmath)
print(okeng)

ans = list(set(okmath).difference(set(okboth)))
ans.sort()
print(ans)
print(len(scoreid))