class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):
        print(f"{self.name} любит кушать {food}.")

class Dog(Animal):
    def make_sound(self):
        return "Гав"

class Cat(Animal):
    def make_sound(self):
        return "Мяу"

    # Экземпляры подклассов
dog = Dog("Шарик", 3)
cat = Cat("Мурка", 2)

    # Используем методы
print(f"{dog.name} (возраст: {dog.age} лет) говорит: {dog.make_sound()}")
dog.eat("корм")

print(f"{cat.name} (возраст: {cat.age} лет) говорит: {cat.make_sound()}")
cat.eat("рыбу")
