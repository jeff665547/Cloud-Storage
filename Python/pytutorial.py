class Vector2:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return  f"({self.x}, {self.y})"

	def __add__(self, rhs):
		return Vector2(self.x + rhs.x, 
									 self.y + rhs.y)

	def __iadd__(self, rhs):
		self.x += rhs.x
		self.y += rhs.y
		return self

	def length(self):
		return (self.x**2 + self.y**2)**0.5

	def __abs__(self):
		return self.length()

	def __getitem__(self, index):
		if index == 0:
			return self.x
		elif index == 1:
			return self.y
		else:
			raise IndexError

	def __len__(self):
		return 2

	def __iter__(self):
		index = 0
		try:
			while True:
				yield self.__getitem__(index)
				index += 1
		except IndexError:
			pass

	def __contains__(self, x):
		for val in self:
			if val == x: return True
		return False

	def __bool__(self):
		return self.length() > 0

	def normalize(self):
		l = self.length()
		try:
			self.x /= l
			self.y /= l
		except ZeroDivisionError:
			pass


p = Vector2(3, 4)
print(p.x, p.y)                # 3, 4

print(p)                       # (3, 4)

q = Vector2(5, 6)
print(p + q)                   # (8, 10)

l = Vector2(3, 4)
l += Vector2(4, 3)
print(l)                       # (7, 7)

print(p.length())              # 5.0
print(abs(p))                  # 5.0

print(p[0], p[1])              # 3 4

print(len(p))                  # 2

for i in range(len(p)):
  print(p[i])                  # 3 
                               # 4
for val in p:
  print(val)                   # 3
                               # 4

print(3 in p)                  # True
print(4 in p)                  # True
print(5 in p)                  # False

print(max(p))                  # 4
print(min(p))                  # 3

print(bool(Vector2(3, 4)))     # True
print(bool(Vector2(0, 0)))     # False

if Vector2(3, 4):
    print("Non-zero")          # Non-zero
if not Vector2(0, 0):
    print("Zero")              # Zero

p.normalize()
print(p)                       # (0.6, 0.8)

l = Vector2(0, 0)
l.normalize()
print(l)                       # (0, 0)




# User Cases
m1 = {"A": 10, "B": 5}
m2 = {"A": 20, "C": 10}

m3 = {**m1}
print(m3)

m4 = {**m3, "C": 6}
print(m4)

m5 = {**m1, **m2}
print(m5)

e = {**m5}
print(e)

del e["A"]
print(e)
print(m5)

ll = [*m5]
print(ll)

ss = {*m5}
print(ss)




# 每個實例一開始其實都是個空的字典，幫他塞資料之後就會存在字典裏面(屬性)
# __class__會儲存該物件所屬的類別
# type的type是type <=> type(type) -> type  p13
# p14 & p15 意思等價
# 
# duck typing 是一種脆弱的(隱晦)平衡 (e.g. draw and draw_all) -> 較不清楚 除非去看實作or文件
# 當 python 的 co-worker 人數很多 (>=10) 時,巨大的程式碼相較於使用C++, Java寫的程式碼會變得較難以閱讀以及使用
# 因此才有繼承的出現 (把class間共用的部分全部抽出來，自成一個新類別)
# 
# p.44 
# 當建構class時，預設會繼承內建的object類別，而最後的object類別則是自己繼承自己。
class A(object):
    pass

a = A()
print(a)
print(str(a))
print(a.__str__())
print(type(a).__str__(a))
print(A.__str__(a))
print(type.__str__(A, a)) # 當實例沒有該屬性的時候會去問該實例的type()是否有該屬性
print(object.__str__(a))
# p51
# 當r沒有該屬性時就去問Rectangle,當Rectangle沒有該屬性時就去問type,
# type會幫忙把Rectangle所繼承的所有父類別依序(Rectangle -> Shape -> Object)去檢查一次看有沒有該屬性,
# 如果都沒有的話就會強制結束。
# 
# p65
# 學習物件導向有個很重要的精神: 當今天發現別人寫的套件或是程式語言default的設定不夠符合自己所預期的使用方法或是結果的時候
# 此時可以使用繼承的方式去建構(擴充、補丁)自己的一套工具，也可以用別種方法(如:合成(composition))來擴充，但最主要的方式還是繼承。
# self[k] = 0 是去呼叫__setitem__
# 為啥要super() ?  因為必須要透過super()來呼叫此類別所繼承的父類別(即python內建的dict),
# 否則會變成自己call自已的迴圈
# 
# p69
# 抽象基底類別: 把規格給講清楚(不同於duck typing的精神)
# 
