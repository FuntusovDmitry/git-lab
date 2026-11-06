
# singlton
class GameLogger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.logs = []
        return cls._instance

    def log(self, message: str):
        self.logs.append(message)
        print(f"[LOG]: {message}")

    def show_logs(self):
        print("--- Все логи ---")
        for log in self.logs:
            print(log)


# Демонстрация Singleton
logger1 = GameLogger()
logger1.log("Игра началась")

logger2 = GameLogger()
logger2.log("Лучник атаковал крепость")

# Проверяем, что это один и тот же объект
print(f"logger1 is logger2: {logger1 is logger2}")  # True
logger1.show_logs()  # Выведет оба лога, так как список общий


# "--- FaktMeth ---"


from abc import ABC, abstractmethod


# --- Продукты ---
class Unit(ABC):
    @abstractmethod
    def attack(self):
        pass


class Archer(Unit):
    def attack(self):
        print("Лучник стреляет из лука!")


class Swordsman(Unit):
    def attack(self):
        print("Мечник рубит мечом!")


# --- Фабрика ---
class UnitFactory(ABC):
    @abstractmethod
    def create_unit(self) -> Unit:
        pass

    def spawn_and_attack(self):
        unit = self.create_unit()
        print(f"Создан юнит: {unit.__class__.__name__}")
        unit.attack()


class ArcherFactory(UnitFactory):
    def create_unit(self) -> Unit:
        return Archer()


class SwordsmanFactory(UnitFactory):
    def create_unit(self) -> Unit:
        return Swordsman()


# --- Демонстрация Factory Method ---
print("\n--- Factory Method ---")
factory1 = ArcherFactory()
factory1.spawn_and_attack()

factory2 = SwordsmanFactory()
factory2.spawn_and_attack()



# --- Abstract Factory ---



# --- Абстрактные продукты ---
class Warrior(ABC):
    @abstractmethod
    def fight(self):
        pass


class Worker(ABC):
    @abstractmethod
    def work(self):
        pass


# --- Продукты Людей ---
class HumanWarrior(Warrior):
    def fight(self):
        print("Человек-воин машет мечом!")


class HumanWorker(Worker):
    def work(self):
        print("Человек-рабочий строит дом.")


# --- Продукты Орков ---
class OrcWarrior(Warrior):
    def fight(self):
        print("Орк-воин бьет топором!")


class OrcWorker(Worker):
    def work(self):
        print("Орк-рабочий добывает руду.")


# --- Абстрактная фабрика ---
class RaceFactory(ABC):
    @abstractmethod
    def create_warrior(self) -> Warrior:
        pass

    @abstractmethod
    def create_worker(self) -> Worker:
        pass


# --- Конкретные фабрики ---
class HumanFactory(RaceFactory):
    def create_warrior(self) -> Warrior:
        return HumanWarrior()

    def create_worker(self) -> Worker:
        return HumanWorker()


class OrcFactory(RaceFactory):
    def create_warrior(self) -> Warrior:
        return OrcWarrior()

    def create_worker(self) -> Worker:
        return OrcWorker()


# --- Клиентский код ---
def create_army(factory: RaceFactory):
    warrior = factory.create_warrior()
    worker = factory.create_worker()
    print("Армия создана!")
    warrior.fight()
    worker.work()


# --- Демонстрация Abstract Factory ---
print("\n--- Abstract Factory ---")
print("Создаем армию людей:")
create_army(HumanFactory())

print("\nСоздаем армию орков:")
create_army(OrcFactory())


# "-------Builder--------"


from abc import ABC, abstractmethod

# --- Продукт ---
class Knight:
    def __init__(self):
        self.weapon = None
        self.armor = None
        self.helmet = None
        self.shield = None

    def __str__(self):
        return (f"Рыцарь с оружием: {self.weapon}, "
                f"броней: {self.armor}, шлемом: {self.helmet}, щитом: {self.shield}")


# --- Интерфейс строителя ---
class KnightBuilder(ABC):
    @abstractmethod
    def build_weapon(self) -> None: pass

    @abstractmethod
    def build_armor(self) -> None: pass

    @abstractmethod
    def build_helmet(self) -> None: pass

    @abstractmethod
    def build_shield(self) -> None: pass

    @abstractmethod
    def get_result(self) -> Knight: pass


# --- Конкретный строитель 1: Тяжелый рыцарь ---
class HeavyKnightBuilder(KnightBuilder):

    def __init__(self):
        self.knight = Knight()


    def build_weapon(self) -> None:
        self.knight.weapon = "Двуручный меч"


    def build_armor(self) -> None:
        self.knight.armor = "Тяжелая кольчуга"


    def build_helmet(self) -> None:
        self.knight.helmet = "Закрытый шлем"


    def build_shield(self) -> None:
        self.knight.shield = "Башенный щит"


    def get_result(self) -> Knight:
        return self.knight


# --- Конкретный строитель 2: Легкий рыцарь ---
class LightKnightBuilder(KnightBuilder):
    def __init__(self):
        self.knight = Knight()

    def build_weapon(self) -> None:
        self.knight.weapon = "Короткий меч"

    def build_armor(self) -> None:
        self.knight.armor = "Кожаная броня"

    def build_helmet(self) -> None:
        self.knight.helmet = "Кожаный шлем"

    def build_shield(self) -> None:
        self.knight.shield = "Нет"

    def get_result(self) -> Knight:
        return self.knight


# --- Директор ---
class KnightDirector:
    def __init__(self, builder: KnightBuilder):
        self.builder = builder

    def construct(self) -> None:
        self.builder.build_weapon()
        self.builder.build_armor()
        self.builder.build_helmet()
        self.builder.build_shield()


# --- Демонстрация Builder ---
if __name__ == "__main__":
    print("\n--- Builder ---")

    # Один и тот же директор, разные строители -> разные рыцари
    for builder in (HeavyKnightBuilder(), LightKnightBuilder()):
        director = KnightDirector(builder)
        director.construct()
        print(builder.get_result())