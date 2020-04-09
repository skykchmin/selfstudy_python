print("Python", "Java", sep="," )

# 시험성적
scores = {"수학": 100, "영어": 80 }
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기순번표
# 001, 002, 003

for num in range(1,21):
    print("대기번호:" + str(num).zfill(3)) #0을 채워주는것 