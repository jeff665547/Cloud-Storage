passbook = {'1':" Wor", 2.2:"gic", "Three":"rd", 4:" Ma", "Six":"ld.", 5:"A"}

true = """ 5-4-2.2-'1'-"Six"  """
true = true.strip()
true = true.split("-")

for i in true:
    print(passbook[eval(i)], end = "")
    