height = eval(input())/100
weight = eval(input())

BMI =  weight/(height**2)

if (BMI < 18.5):
    status = "Underweight"
elif (18.5 <= BMI < 24 ):
    status = "Normal"
elif (24 <= BMI < 27):
    status = "Overweight"
elif (27 <= BMI < 30):
    status = "Obese Class I (Moderately obese)"
elif (30 <= BMI < 35):
    status = "Obese Class II (Severely obese)"
elif (BMI >= 35):
    status = "Obese Class III (Very severely obese)"

#print(BMI, status, sep"\n")

print('%.3f'%(99.9999))
#將99.9999小數點後第三位四捨五入
print('%.2f'%(99.9999))
#將99.9999小數點後第二位四捨五入


#BMI
height = eval(input())/100
weight = eval(input())
BMI = weight/height**2
BMI = eval("%.2f"%(BMI))

if(BMI < 18.5):
    status = "Underweight"
elif(18.5 <= BMI < 24 ):
    status = "Normal"
elif(24 <= BMI < 27):
    status = "Overweight"
elif(27 <= BMI < 30):
    status = "Obese Class I"
elif(30 <= BMI < 35):
    status = "Obese Class II"
elif(BMI >= 35):
    status = "Obese Class III"
else:
    pass

print(BMI, status, sep = "\n")