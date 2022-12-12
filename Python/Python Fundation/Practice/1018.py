
AA = "y"

while( AA == "y" ):
    score = eval(input())
    if(score >= 60):
        print("pass")
    else:
        print("fail")
    AA = input()
