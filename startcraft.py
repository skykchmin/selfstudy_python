class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    def move(self, location):
        print("[지상유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} :  파괴되었습니다" .format(self.name))

class AttackUnit(Unit): #똑같은 부분을 상속
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1}  방향으로 적군을 공격합니다. [공격력 {2}]" .format(self.name, location, self.damage))

# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)
    
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다.(HP 10감소)".format(self.name))
        else:
            print("{0}: 체력이 부족하여 스팀팩을 사용할 수 없습니다." .format(self.name))

class Tank(AttackUnit):
    seize_developed = False #시즈모드 개발여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다." .format(self.name))
            self.damage *=2
            self.seize_mode = True
        else:
            print("{0} : 시즈모드로 해제합니다." .format(self.name))
            self.damage /=2
            self.seize_mode = False



class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable): #다중상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) #지상스피드는 0으로 처리
        Flyable.__init__(self, flying_speed) 

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 레이스

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__("레이스", 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocking == True: #클로킹 모드
            print("{0} : 클로킹 모드 해제합니다".format(self.name))
            self.clocked = False
        else:
            print("{0} : 클로킹 모드 설정합니다".format(self.name))
            self.clocked = True





