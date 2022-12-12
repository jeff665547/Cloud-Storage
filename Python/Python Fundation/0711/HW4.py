score = int(input())

if(score >= 95):
    print("獎金 2000 元")
elif(90 <= score <= 94):
    print("獎金 1000 元")
elif(score >= 80 and score <= 89):
    print("獎金 500 元")
else:
    print("獎金 0 元")
