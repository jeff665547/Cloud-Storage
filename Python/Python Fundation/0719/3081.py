f2 = open("../app/stores_old.csv", "r", encoding = "big5")
txt1 = f2.readlines()
f2.close()

for i in txt1:
    print(i.strip())
