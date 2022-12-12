
grade = eval(input())

if(grade == 1):
    score = eval(input())
    if(100 >= score >= 60):
        print("pass")
    elif(59 >= score >= 0):
        print("fail")
    else:
        print("score error")
elif(grade == 2):
    score = eval(input())
    if(100 >= score >= 70):
        print("pass")
    elif(69 >= score >= 0):
        print("fail")
    else:
        print("score error")
else:
    print("roll error")