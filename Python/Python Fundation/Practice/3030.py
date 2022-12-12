Original = eval(input())

Adjusted = (Original**(1/2))*10
difference = Adjusted - Original
if(difference >= 0):
    difference = "(+" + str('%.0f'%(difference)) + ")"
    
print("Original: " , '%.2f'%(Original), sep = "")
print("Adjusted: ", '%.2f'%(Adjusted), difference, sep = "")

