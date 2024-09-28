class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):
        print(f"{self.name} любит кушать {food}.")

# Подкласс Mammal (Млекопитающее)
class Mammal(Animal):
    def __init__(self, name, age, has_fur):
        super().__init__(name, age)
        self.has_fur = has_fur

    def make_sound(self):
        return "Звук млекопитающего"

# Подкласс Dog
class Dog(Mammal):
    def make_sound(self):
        return "Гав"

# Подкласс Cat
class Cat(Mammal):
    def make_sound(self):
        return "Мяу"

# Подкласс Bird (Птица)
class Bird(Animal):
    def __init__(self, name, age, can_fly):
        super().__init__(name, age)
        self.can_fly = can_fly

    def make_sound(self):
        return "Чирик"

# Подкласс Reptile (Пресмыкающееся)
class Reptile(Animal):
    def __init__(self, name, age, is_poisonous):
        super().__init__(name, age)
        self.is_poisonous = is_poisonous

    def make_sound(self):
        return "Шшш"

# Создаем экземпляры классов
dog = Dog("Шарик", 3, True)
cat = Cat("Мурка", 2, True)
bird = Bird("Чижик", 1, True)
snake = Reptile("Кобра", 5, True)

# Функция полиморфизма
def animal_sound(animals):
    for animal in animals:
        print(f"{animal.name} говорит: {animal.make_sound()}")

# Делаем список животных и вызываем функцию
animals = [dog, cat, bird, snake]
animal_sound(animals)
