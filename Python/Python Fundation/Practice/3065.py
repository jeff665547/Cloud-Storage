
itemsA = {"蘋果","香蕉","鳳梨","芭樂"}
itemsB = {"鳳梨","蘋果","水梨","蓮霧"}

AA = itemsA.intersection(itemsB)
BB = itemsA.union(itemsB)
CC = BB.difference(AA)
Ans = list(CC)
Ans.sort()
print(Ans)


