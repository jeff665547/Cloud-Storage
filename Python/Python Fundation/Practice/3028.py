
edge1 = eval(input())
edge2 = eval(input())
edge3 = eval(input())

if( (edge1 + edge2 > edge3) and
    (edge1 + edge3 > edge2) and
    (edge2 + edge3 > edge1) ):
    
    print("True")
    
    if( (edge1**2 + edge2**2 == edge3**2) or
        (edge1**2 + edge3**2 == edge2**2) or
        (edge2**2 + edge3**2 == edge1**2) ):
        
        print("Right Triangle")
    
    else:
        print("Non-Right Triangle")
    
else:
    print("False")





