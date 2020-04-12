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
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class AttackUnit(Unit): #똑같은 부분을 상속
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1}  방향으로 적군을 공격합니다. [공격력 {2}]" .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} :  파괴되었습니다" .format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly (self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable): #다중상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")





# marine1 = Unit("마린", 40, 5)
# marine1 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름: {0}, 공격력 {1}".format(wraith1.name,wraith1.damage))

# #마인드 컨트롤 
# wraith2 = Unit("레이스", 80, 5)
# wraith2.clockin = True

# if wraith2.clockin = true:
#     print("{0}")