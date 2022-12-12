AA = []

while (True):
    n = input()
    m = n.replace("-", "")
    m = m.replace(".", "")
    if (m.isdecimal() == 0):
        if(m == "q"):
            break
        else:
            print("Please Enter Numbers Only")
            continue
    else:
        n = eval(n)
        AA.append(n)
        continue

print(AA)
BB = AA.copy()
BB.sort()
print(BB)
BB.reverse()
print(BB)
print(AA)












