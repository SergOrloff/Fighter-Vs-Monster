from abc import ABC, abstractmethod


# Шаг 1: Создаём абстрактный класс Weapon
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


# Шаг 2: Реализуем конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "удар мечом"


class Bow(Weapon):
    def attack(self):
        return "выстрел из лука"

# Шаг 3: Модифицируем класс Fighter


class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def changeWeapon(self, weapon):
        self.weapon = weapon

    def attack(self, monster):
        if self.weapon:
            attack_action = self.weapon.attack()
            print(f"{self.name} наносит {attack_action}.")
            monster.defeat()
        else:
            print(f"{self.name} не имеет оружия для атаки.")


class Monster:
    def __init__(self, name):
        self.name = name

    def defeat(self):
        print(f"Монстр {self.name} побеждён!")


# # Шаг 4: Реализация боя
# Создаём экземпляры бойца Добрыню Никитича и монстра Змея Горыныча
fighter1 = Fighter("Добрыня Никитич")
fighter2 = Fighter("Илья Муромец")
monster1 = Monster("'Змей Горыныч'")
monster2 = Monster("'Огненный Дракон'")

# Выбираем меч и атакуем Змея Горыныча
sword = Sword()
fighter1.changeWeapon(sword)
print(f"\n{fighter1.name} выбирает меч.")
fighter1.attack(monster1)

fighter2.changeWeapon(sword)
print(f"\n{fighter2.name} выбирает меч.")
fighter2.attack(monster1)


# Выбираем лук и атакуем Огненного Дракона
bow = Bow()
fighter1.changeWeapon(bow)
print(f"\n{fighter1.name} выбирает лук.")
fighter1.attack(monster2)

fighter2.changeWeapon(bow)
print(f"\n{fighter2.name} выбирает лук.")
fighter2.attack(monster2)

# Выбираем меч и атакуем теперь Огненного Дракона
sword = Sword()
fighter1.changeWeapon(sword)
print(f"\n{fighter1.name} выбирает меч.")
fighter1.attack(monster2)

fighter2.changeWeapon(sword)
print(f"\n{fighter2.name} выбирает меч.")
fighter2.attack(monster2)

# Выбираем лук и атакуем теперь Огненного Дракона
bow = Bow()
fighter1.changeWeapon(bow)
print(f"\n{fighter1.name} выбирает лук.")
fighter1.attack(monster1)

fighter2.changeWeapon(bow)
print(f"\n{fighter2.name} выбирает лук.")
fighter2.attack(monster1)
