# 문제1-1
pin = "881120-1068234"
yyyymmdd = pin[0:6]
num = pin[7:]
yyyymmdd = 1
print(yyyymmdd)
print(num)

# 문제 1-2
pin = "881120-1068234"
print(pin[7])

# 리스트 문제 1
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

# 리스트 문제 2
a = ['Life', 'is' , 'too', 'short']
result = " ".join(a)
print(result)

# 튜플 문제 1
a = (1, 2, 3)
a = a + (4,)
print(a)

# 딕셔너리 

a = {'A': 90, 'B': 80, 'C': 70}
result = a.pop('B')
print(a.items())
print(result)

# 집합
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)

