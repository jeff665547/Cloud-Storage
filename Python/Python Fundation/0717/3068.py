keys = "P", "M", "H"
vals = "Pikachu", "Mickey Mouse" ,"Hello kitty"

d1 = dict(zip(keys, vals))

while True:
    qkey = input()
    if(qkey == "-1"):
        break
    if(qkey not in d1):
        print(qkey, "does not exist. Enter a new one:")
        AA = input()
        d1[qkey] = AA
    else:
        print(d1[qkey])    


