#　基本玩家資訊
class Player:
    def __init__(self,name,health,attack,defence):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defence

    def take_damage(salf,damage):
        if damage > salf.defense:
            salf.health -= damage - salf.defense
            return f"{salf.name}受到了{damage} 點傷害!"
        else:
            return f"{salf.name}成功抵擋攻擊!!"
class Mage(Player):
    def __init__(self, name, health, attack, defence,magic_power):
        super().__init__(name,health,attack,defence)
    def cast_spell(self):
        self.magic_power -= 10 
        return self.attack+self.magic_power
# 戰士類別
class Warrior(Player): # 繼承Player類別
    def __init__(self, name, health, attack, defense, armor):   
        """初始化戰士, name: 名稱, health: 血量, attack: 攻擊, defense: 防禦, armor: 裝甲"""
        super().__init__(name, health, attack, defense)
        self.armor = armor
    def use_armor(self):
        self.health += self.armor
        return f"{self.name} 使用裝甲，增加了 {self.armor} 點體力！"

        return f"{self.name}使用裝甲增加了{self.armor}點體力"
Player1 = Warrior("SCP Angus615",100,15,10,5)
Player2 = Mage("Angus",80,10,5,20)
print(f"{Player1.name}血量剩餘: {Player1.health}")
print(Player1.use_armor())
print(f"{Player1.name}血量剩餘: {Player1.health}")
print(f"{Player2.name}目前魔力: {Player2.magic_power}")
Player1.take_damage(Player2.cast_spell())
print(f"{Player2.name}對{Player1.name}施放魔法攻擊！")
print(f"{Player2.name}目前魔力: {Player2.magic_power}")
print(f"{Player1.name}血量剩餘: {Player1.health}")
# Player1 = Player("GG",100,20,9)
# print(f"玩家名稱:{Player1.name}")
# print(f"玩家血量:{Player1.health}")
# print(f"玩家攻擊:{Player1.attack}")
# print(f"玩家防禦:{Player1.defense}")
# Player2 = Player("GG_gg",50,10,5)
# print(f"玩家名稱:{Player2.name}")
# print(f"玩家血量:{Player2.health}")
# print(f"玩家攻擊:{Player2.attack}")
# print(f"玩家防禦:{Player2.defense}")

# print(Player2.take_damage(Player1.attack))
# print(f"玩家1血量剩餘:{Player2.health}")


        