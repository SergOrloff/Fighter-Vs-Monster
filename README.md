# Применение принципа открытости/закрытости (Open/Closed Principle) в разработке простой игры "Fighter vs Monster"

## Цель
Закрепить понимание и навыки применения принципа открытости/закрытости (Open/Closed Principle), одного из пяти SOLID принципов объектно-ориентированного программирования. Принцип открытости/закрытости гласит, что программные сущности (классы, модули, функции и т.д.) должны быть открыты для расширения, но закрыты для модификации.

## Описание задания
Разработать простую игру, где игрок может использовать различные типы оружия для борьбы с монстрами. Программа должна быть спроектирована таким образом, чтобы легко можно было добавлять новые типы оружия, не изменяя существующий код бойцов или механизм боя.

## Шаги реализации
1. **Создаём абстрактный класс для оружия:**
   - Создан абстрактный класс `Weapon`, который содержит абстрактный метод `attack()`.

2. **Реализуем конкретные типы оружия:**
   - Созданы два класса, унаследованных от `Weapon` (`Sword`(меч) и `Bow`(лук)). Каждый из этих классов реализует метод `attack()` своим уникальным способом.

3. **Модифицируем класс Fighter:**
   - Добавлено в класс `Fighter` поле, которое будет хранить объект класса `Weapon`.
   - Добавлен метод `changeWeapon()`, который позволяет изменить оружие бойца.

4. **Реализация боя:**
   - Реализован простой механизм для демонстрации боя между двумя бойцами, сражающимися один на один с каждым из двух монстров, исходя из выбранного оружия.

## Запуск программы

1. Создайте файл `bd04.py` и вставьте в него следующий код:

```python
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

# Создаём экземпляры бойцов и монстров
fighter1 = Fighter("Добрыня Никитич")
fighter2 = Fighter("Илья Муромец")
monster1 = Monster("'Змей Горыныч'")
monster2 = Monster("'Огненный Дракон'")

# Выбираем меч и атакуем монстров
sword = Sword()
fighter1.changeWeapon(sword)
print(f"\n{fighter1.name} выбирает меч.")
fighter1.attack(monster1)

fighter2.changeWeapon(sword)
print(f"\n{fighter2.name} выбирает меч.")
fighter2.attack(monster1)

# Выбираем лук и атакуем монстров
bow = Bow()
fighter1.changeWeapon(bow)
print(f"\n{fighter1.name} выбирает лук.")
fighter1.attack(monster2)

fighter2.changeWeapon(bow)
print(f"\n{fighter2.name} выбирает лук.")
fighter2.attack(monster2)

# Выбираем меч и атакуем теперь другого монстра
fighter1.changeWeapon(sword)
print(f"\n{fighter1.name} выбирает меч.")
fighter1.attack(monster2)

fighter2.changeWeapon(sword)
print(f"\n{fighter2.name} выбирает меч.")
fighter2.attack(monster2)

# Выбираем лук и атакуем теперь другого монстра
fighter1.changeWeapon(bow)
print(f"\n{fighter1.name} выбирает лук.")
fighter1.attack(monster1)

fighter2.changeWeapon(bow)
print(f"\n{fighter2.name} выбирает лук.")
fighter2.attack(monster1)
```

2. Запустите программу:
    ```sh
    python bd04.py
    ```

## Вывод
Программа демонстрирует применение принципа открытости/закрытости: новые типы оружия можно легко добавлять, не изменяя существующие классы бойцов и механизм боя. Программа выводит результат боя в консоль, как указано в примере результата.

## Контакты

Для вопросов и предложений вы можете связаться с автором проекта по электронной почте: [6202818@gmail.com](mailto:6202818@gmail.com).

## Лицензия

Этот проект лицензирован под MIT License. Подробности см. в файле `LICENSE`.