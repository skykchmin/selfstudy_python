cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(5))
print(cabinet.get(5,"사용가능"))

cabinet = {"A-3": "유재석", "B-4": "김종국"}
print(cabinet["A-3"])

del cabinet["A-3"]
print (cabinet)

#key 들만 출력
print(cabinet.keys())

#value 들만 출력
print(cabinet.values())