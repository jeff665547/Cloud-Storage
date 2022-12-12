
score = eval(input())

if(1 <= score <= 59):
    GPA = 0
    Grade =  "F"
elif(60 <= score <= 62):
    GPA = 1.7
    Grade =  "C-"
elif(63 <= score <= 66):
    GPA = 2.0
    Grade =  "C"
elif(67 <= score <= 69):
    GPA = 2.3
    Grade =  "C+"
elif(70 <= score <= 72):
    GPA = 2.7
    Grade =  "B-"
elif(73 <= score <= 76):
    GPA = 3.0
    Grade =  "B"
elif(77 <= score <= 79):
    GPA = 3.3
    Grade =  "B+"
elif(80 <= score <= 84):
    GPA = 3.7
    Grade =  "A-"
elif(85 <= score <= 89):
    GPA = 4.0
    Grade =  "A"
elif(90 <= score <= 100):
    GPA = 4.3
    Grade =  "A+"

if(GPA != 0 ):
    print('%.1f'%(GPA), Grade, sep = "\n")
else:
    print(GPA, Grade, sep = "\n")
