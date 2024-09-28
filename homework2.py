class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):
        print(f"{self.name} любит кушать {food}.")

# Подкласс Mammal (Млекопитающее)
class Mammal(Animal):
    def __init__(self, name, age, has_fur):
        super().__init__(name, age)  # Наследуем атрибуты name и age
        self.has_fur = has_fur  # Специфический атрибут для млекопитающих (наличие шерсти)

    def make_sound(self):
        return "Звук млекопитающего"

# Подкласс Dog, который является млекопитающим
class Dog(Mammal):
    def make_sound(self):
        return "Гав"

# Подкласс Cat, который также является млекопитающим
class Cat(Mammal):
    def make_sound(self):
        return "Мяу"

# Подкласс Bird (Птица)
class Bird(Animal):
    def __init__(self, name, age, can_fly):
        super().__init__(name, age)
        self.can_fly = can_fly  # Специфический атрибут для птиц (могут ли летать)

    def make_sound(self):
        return "Чирик"

# Подкласс Reptile (Пресмыкающееся)
class Reptile(Animal):
    def __init__(self, name, age, is_poisonous):
        super().__init__(name, age)
        self.is_poisonous = is_poisonous  # Специфический атрибут для рептилий (является ли ядовитой)

    def make_sound(self):
        return "Шшш"

# Создаем экземпляры классов
dog = Dog("Шарик", 3, True)  # Млекопитающее с шерстью
cat = Cat("Мурка", 2, True)  # Млекопитающее с шерстью
bird = Bird("Чижик", 1, True)  # Птица, которая может летать
snake = Reptile("Кобра", 5, True)  # Пресмыкающееся, которое ядовито

# Используем методы
print(f"{dog.name} (возраст: {dog.age} лет) говорит: {dog.make_sound()}")
dog.eat("корм")

print(f"{cat.name} (возраст: {cat.age} лет) говорит: {cat.make_sound()}")
cat.eat("рыбу")

print(f"{bird.name} (возраст: {bird.age} лет) говорит: {bird.make_sound()}")
bird.eat("семена")

print(f"{snake.name} (возраст: {snake.age} лет) говорит: {snake.make_sound()}")
snake.eat("мышей")
