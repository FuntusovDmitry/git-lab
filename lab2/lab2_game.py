from abc import ABC, abstractmethod


# ---------- Интерфейсы (Реализация через абстрактный класс)----------
class Attacker(ABC):
    "Атаковать юнита."
    @abstractmethod
    def attack(self, unit: "Unit") -> None:
        pass

class Moveable(ABC):
    "Переместиться в точку (x, y)."
    @abstractmethod
    def move_to(self, x: int, y: int) -> None:
        pass

# ---------- Базовый класс ----------
class GameObject(ABC):
    def __init__(self, id: int, name: str, x: int, y: int):
        self._id = id
        self._name = name
        self._x = x
        self._y = y

    def get_id(self) -> int:
        return self._id

    def get_name(self) -> str:
        return self._name

    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y

# ---------- Юниты ----------
class Unit(GameObject, ABC):
    def __init__(self, id: int, name: str, x: int, y: int, hp: float):
        super().__init__(id, name, x, y)
        self._hp = hp

    def is_alive(self) -> bool:
        return self._hp > 0

    def get_hp(self) -> float:
        return self._hp

    def receive_damage(self, damage: float) -> None:
        self._hp = max(0.0, self._hp - damage)

class Archer(Unit, Attacker, Moveable):
    def __init__(self, id: int, name: str, x: int, y: int,
                 hp: float = 100.0, damage: float = 15.0):
        super().__init__(id, name, x, y, hp)
        self._damage = damage

    def attack(self, unit: Unit) -> None:
        if not self.is_alive():
            print(f"{self.get_name()} мёртв и не может атаковать")
        elif not unit.is_alive():
            print(f"цель {unit.get_name()} уже мертва")
        else:
            unit.receive_damage(self._damage)

    def move_to(self, x: int, y: int) -> None:
        if self.is_alive():
            self._x, self._y = x, y
            print(f"{self.get_name()} at {(self._x, self._y)}")
        else:
            print(f"{self.get_name()} мертв и не может двигаться")

# ---------- Постройки ----------
class Building(GameObject, ABC):
    def __init__(self, id: int, name: str, x: int, y: int, built: bool = False):
        super().__init__(id, name, x, y)
        self._built = built

    def is_built(self) -> bool:
        return self._built

    def build(self) -> None:
        self._built = True


class Fort(Building, Attacker):
    def __init__(self, id: int, name: str, x: int, y: int,
                 built: bool = False, damage: float = 30.0):
        super().__init__(id, name, x, y, built)
        self._damage = damage

    def attack(self, unit: Unit) -> None:
        if not self.is_built():
            print(f"стрелять нельзя, крепость {self.get_name()} не построена")
        elif unit.is_alive():
            unit.receive_damage(self._damage)
        else:
            print(f"{self.get_name()}: цель уже мертва")


class MobileHouse(Building, Moveable):
    def __init__(self, id: int, name: str, x: int, y: int, built: bool = False):
        super().__init__(id, name, x, y, built)

    def move_to(self, x: int, y: int) -> None:
        if not self.is_built():
            print(f"дом {self.get_name()} не построен, его перемещение невозможно")
            return
        self._x, self._y = x, y
        print(f"{self.get_name()} at {(self._x, self._y)}")


# ---------- Демонстрация ----------
if __name__ == "__main__":
    archer = Archer(1, "Robin", 0, 0)
    enemy = Archer(2, "Enemy", 5, 5, hp=20)
    enemy1 = Archer(5, "Enemy1", 5, 5, hp=50)
    fort = Fort(3, "Fort1", 10, 10)
    house = MobileHouse(4, "house", 1, 1)

    archer.attack(enemy)
    archer.move_to(6, 7)

    print(enemy.get_name(), "hp:", enemy.get_hp(), "alive:", enemy.is_alive())
    archer.attack(enemy)
    print(enemy.get_name(), "hp:", enemy.get_hp(), "alive:", enemy.is_alive())

    archer.attack(enemy)
    print(enemy.get_name(), "hp:", enemy.get_hp(), "alive:", enemy.is_alive())

    print(enemy1.get_name(), "hp:", enemy1.get_hp(), "alive:", enemy1.is_alive())

    fort.attack(enemy1)
    print(enemy1.get_name(), "hp:", enemy1.get_hp(), "alive:",

    enemy1.is_alive())

    fort.attack(enemy1)
    print(enemy1.get_name(), "hp:", enemy1.get_hp(), "alive:", enemy1.is_alive())

    house.move_to(7, 7)

    print("----------------------------------------------------")

    fort.build()
    house.build()

    fort.attack(enemy1)
    print(enemy1.get_name(), "hp:", enemy1.get_hp(), "alive:", enemy1.is_alive())

    fort.attack(enemy1)
    print(enemy1.get_name(), "hp:", enemy1.get_hp(), "alive:", enemy1.is_alive())

    house.move_to(8, 7)







