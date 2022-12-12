
Math = {"柯南","灰原","步美","美環","光彦"}
English = {"柯南","灰原","丸尾","野口","步美"}

Both = list(Math.intersection(English))
Mathpassonly = list(Math.difference(English))
Englishonly = list(English.difference(Both))

Mathpassonly.sort()
Englishonly.sort()
Both.sort()

print(Mathpassonly, Englishonly, Both, sep = "\n")


