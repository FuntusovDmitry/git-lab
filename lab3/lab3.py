



print("синглтон")
print()


class Config:
    _obj = None

    def __new__(cls):
        if cls._obj is None:
            obj = super().__new__(cls)
            obj.program_name = "lab3"
            obj.environment = "release"
            obj.loglevel = "verbose"
            obj.version = "1.6.7"
            cls._obj = obj
        return cls._obj


config1 = Config()
config2 = Config()
config3 = Config()

print(config1 is config2)
print(config1 is config3)

print()
print("фабричный метод")
print()

from abc import ABC, abstractmethod


class FileData(ABC):
    @abstractmethod
    def extract(self):
        pass


class FileProcessor(ABC):
    def process(self):
        data = self.generate_data()
        print(f'Данные для отправки: {data.extract()}')

    @abstractmethod
    def generate_data(self):
        pass


class TableData(FileData):
    def extract(self):
        return 'Данные из таблицы'


class JsonData(FileData):
    def extract(self):
        return 'Данные из json'


class TableProcessor(FileProcessor):
    def generate_data(self):
        return TableData()


class JsonProcessor(FileProcessor):
    def generate_data(self):
        return JsonData()


table_proc = TableProcessor()
json_proc = JsonProcessor()

table_proc.process()
json_proc.process()


print()
print("абстрактная фабрика")
print()

from abc import ABC, abstractmethod


class Food(ABC):
    @abstractmethod
    def eat(self):
        pass


class Toy(ABC):
    @abstractmethod
    def play(self):
        pass


class DogFood(Food):
    def eat(self):
        return "Собака ест сухой корм для собак"


class DogToy(Toy):
    def play(self):
        return "Собака грызет резиновую игрушку"


class CatFood(Food):
    def eat(self):
        return "Кошка ест корм для кошек"


class CatToy(Toy):
    def play(self):
        return "Кошка играет с мышкой"


class PetFactory(ABC):
    @abstractmethod
    def create_food(self):
        pass

    @abstractmethod
    def create_toy(self):
        pass


class DogFactory(PetFactory):
    def create_food(self):
        return DogFood()

    def create_toy(self):
        return DogToy()


class CatFactory(PetFactory):
    def create_food(self):
        return CatFood()

    def create_toy(self):
        return CatToy()


def care_for_pet(factory: PetFactory):
    food = factory.create_food()
    toy = factory.create_toy()
    print(food.eat())
    print(toy.play())
    print()


care_for_pet(DogFactory())

care_for_pet(CatFactory())

print()
print("билдер")
print()
class Plane:
    def __init__(self):
        self.brand = None
        self.engine = None
        self.model = None
        self.year_of_creation = None
        self.number_of_seats = None
        self.doors = None
        self.color = 'white'
        self.number_of_engines = 2
        self.airline_affiliation = "AEROFLOT"


class PlaneBuilder:
    def __init__(self):
        self._plane = Plane()

    def set_brand(self, brand):
        self._plane.brand = brand
        return self

    def set_engine(self, engine):
        self._plane.engine = engine
        return self

    def set_model(self, model):
        self._plane.model = model
        return self

    def set_year_of_creation(self, year_of_creation):
        self._plane.year_of_creation = year_of_creation
        return self

    def set_number_of_seats(self, number_of_seats):
        self._plane.number_of_seats = number_of_seats
        return self

    def set_doors(self, doors):
        self._plane.doors = doors
        return self

    def build(self):
        if self._plane.brand is None:
            raise ValueError('Не указана марка самолета')

        if self._plane.engine is None:
            raise ValueError('Не указан тип двигателя самолета')

        if self._plane.model is None:
            raise ValueError('Не указана модель самолета')

        if self._plane.year_of_creation is None:
            raise ValueError('Не указан год выпуска конкретного самолета')

        if self._plane.number_of_seats is None:
            raise ValueError('Не указано количество посадочных мест самолета')

        if self._plane.doors is None:
            raise ValueError('Не указано количество выходов самолета')

        plane = self._plane
        self._plane = Plane()
        return plane


class PlaneDirector:
    def __init__(self, builder):
        self._builder = builder

    def create_boeing_777(self):
        return (
            self._builder
            .set_brand("Boeing")
            .set_engine("GE90-115B")
            .set_model("777-300er")
            .set_year_of_creation(2010)
            .set_number_of_seats(390)
            .set_doors(10)
            .build()
        )

    def create_airbus_a320(self):
        return (
            self._builder
            .set_brand("Airbus")
            .set_engine("CFM56-5B")
            .set_model("A320")
            .set_year_of_creation(2018)
            .set_number_of_seats(180)
            .set_doors(8)
            .build()
        )


def print_plane_info(plane):
    print(f"Информация о самолете: {plane.brand} {plane.model}")
    print('-' * 30)
    print(f"Двигатель: {plane.engine}")
    print(f"Год выпуска: {plane.year_of_creation}")
    print(f"Мест для пассажиров:{plane.number_of_seats}")
    print(f"Количество выходов: {plane.doors}")
    print(f"Цвет: {plane.color}")
    print(f"Количество двигателей: {plane.number_of_engines}")
    print(f"Авиакомпания: {plane.airline_affiliation}")
    print('=' * 30)


builder = PlaneBuilder()
director = PlaneDirector(builder)

boeing = director.create_boeing_777()
print_plane_info(boeing)

airbus = director.create_airbus_a320()
print_plane_info(airbus)