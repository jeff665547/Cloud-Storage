
n = input()

if (n.isupper()):
    print(n, "is a capital letter.")
elif(n.islower()):
    print(n, "is a lowercase letter.")
elif(n.isdigit()):
    print(n, "is a number.")
else:
    print(n, "is a punctuation.")
