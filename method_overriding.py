# # 마린 : 공격 유닛, 군인, 총을 쓸 수 있음

# name = "마린"
# hp = 40
# damage = 5

# print("{0} 유닛이 생성되었습니다" .format(name))
# print("체력{0}, 공격력{1}\n".format(hp,damage))

# # 탱크 : 공격

# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{0} 유닛이 생성되었습니다" .format(tank_name))
# print("체력{0}, 공격력{1}\n".format(tank_hp,tank_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))

# attack(name, "1시", damage)
# attack(tank_damage, "1시", tank_damage)

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

class AttackUnit(Unit): #똑같은 부분을 상속
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1}  방향으로 적군을 공격합니다. [공격력 {2}]" .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} :  파괴되었습니다" .format(self.name))


class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly (self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable): #다중상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) #지상스피드는 0으로 처리
        Flyable.__init__(self, flying_speed) 

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

vulture = AttackUnit("벌쳐 ", 80,10 ,20)

battlecuriser = FlyableAttackUnit("배틀크루져", 500, 25, 3)
battlecuriser.move("3시")


