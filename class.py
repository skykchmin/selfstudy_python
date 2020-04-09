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
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다" .format(self.name))
        print("체력{0}, 공격력{1}\n".format(self.hp,self.damage))

marine1 = Unit("마린", 40, 5)
marine1 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)