fm = open("../app/math_list.csv", "r", encoding = "Big5")
#fm = open("C:\\Users\\jeff\\Desktop\\ALL\\Python Fundation\\Practice\\Data\\math_list.csv", "r", encoding ="big5")
txtm = fm.readlines()
fm.close()

fe = open("../app/english_list.csv", "r", encoding = "Big5")
#fe = open("C:\\Users\\jeff\\Desktop\\ALL\\Python Fundation\\Practice\\Data\\english_list.csv", "r", encoding ="big5")
txte = fe.readlines()
fe.close()

title = {"學號"}
datam = []

for i in txtm:
    i = i.strip()
    i = i.split(",")
    datam.append(i[0])

math = set(datam)
math.difference_update(title)

datae = []

for i in txte:
    i = i.strip()
    i = i.split(",")
    datae.append(i[0])

english = set(datae)
english.difference_update(title)

both = english.intersection(math)
engnomath = english.difference(both)
mathnoeng = math.difference(both)
one = engnomath.union(mathnoeng)
All = one.union(both)

both = list(both)
engnomath = list(engnomath)
mathnoeng = list(mathnoeng)
one = list(one)
All =  list(All)

both.sort()
engnomath.sort()
mathnoeng.sort()
one.sort()
All.sort()

print(both)
print(one)
print(mathnoeng)
print(engnomath)
print(All, end = "")

