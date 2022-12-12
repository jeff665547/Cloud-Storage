
f2 = open("../app/sim.txt", "r", encoding = "gb2312")
txt1 = f2.readlines()
f2.close()



for i in txt1:
    print(i.strip())


