class HouseMin():
    lastname = "민"
    def __init__(self, name): # 생성자를 만듬과 동시에 입력값을 주면 동시에 전달이 가능하다
        self.fullname = self.lastname + name
    def travel(self, place):
        print("%s, %s 여행을 가다" %(self.fullname,place))
    def love(self,other):
        print("%s, %s 사랑에 빠졌네" %(self.fullname, other.fullname))
    def fight(self, other):
        print("%s, %s 싸우네" %(self.fullname, other.fullname))  
    def __add__(self, other):
        print("%s, %s 결혼했네" %(self.fullname, other.fullname))
    def __sub__(self, other):
        print("%s, %s 이혼했네" %(self.fullname, other.fullname)) 

class HouseKim(HouseMin): #상속
    lastname="김"
    def travel(self, where, day):
        print("%s, %s여행 %d일가네" %(self.fullname, where, day))

pey = HouseMin("경전")
julitet = HouseKim("경민")
pey.travel("부산")
julitet.travel("부산", 3)
pey.love(julitet)
pey + julitet
pey.fight(julitet)
pey - julitet
