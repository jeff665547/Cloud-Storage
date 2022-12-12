#f = open("C:/Users/jeff/Desktop/ALL/Python Fundation/Practice/Data/stores_old.csv", "r", encoding = "big5")
f = open("../app/stores_old.csv", "r", encoding = "big5")

txt = f.readlines()
f.close()

txt1 = []
for i in txt:
    i = i.strip()
    i = i.split(",")
    txt1.append(i)
    
newfile = []

for i in range(len(txt1)):
    newline = []
    for j in range(len(txt1[0])):
        if (j == 0 or j == 3 or j == 5 or j == 6):
            newline.append(txt1[i][j])
    newfile.append(newline)
    
#fnew = open("C:/Users/jeff/Desktop/ALL/Python Fundation/Practice/Data/stores_new.csv", "w", encoding = "big5")
fnew = open("../app/stores_new.csv", "w", encoding = "big5")

for i in newfile:
    fnew.write(",".join(i) + "\n")
fnew.close()


#fnewr = open("C:/Users/jeff/Desktop/ALL/Python Fundation/Practice/Data/stores_new.csv", "r", encoding = "big5")
fnewr = open("../app/stores_new.csv", "r", encoding = "big5")
NEWread = fnewr.readlines()
fnewr.close()

for i in NEWread:
    print(i.strip() + ",")
