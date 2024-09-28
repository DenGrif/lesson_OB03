class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.species}), Возраст: {self.age}"


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self):
        return f"{self.name}, должность: {self.position}"


class ZooKeeper(Employee):
    def __init__(self, name):
        super().__init__(name, "Смотритель зоопарка")

    def feed_animal(self, animal):
        print(f"{self.name} кормит животное {animal.name} ({animal.species}).")


class Veterinarian(Employee):
    def __init__(self, name):
        super().__init__(name, "Ветеринар")

    def heal_animal(self, animal):
        print(f"{self.name} лечит животное {animal.name} ({animal.species}).")


class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Добавлено животное: {animal}")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Добавлен сотрудник: {employee}")

    def show_animals(self):
        print("Животные зоопарка:")
        for animal in self.animals:
            print(f"- {animal.name} (возраст: {animal.age} лет)")

    def show_employees(self):
        print("Сотрудники зоопарка:")
        for employee in self.employees:
            print(f"- {employee}")


# Создание объектов животных
animal1 = Animal("Лео", "Лев", 5)
animal2 = Animal("Эля", "Слон", 10)

# Создание объектов сотрудников
employee1 = Employee("Иван", "Дрессировщик")
employee2 = Employee("Мария", "Ветеринар")

# Создание специализированных сотрудников
zoo_keeper = ZooKeeper("Алексей")
veterinarian = Veterinarian("Ольга")

# Создание зоопарка и добавление объектов
zoo = Zoo()
zoo.add_animal(animal1)
zoo.add_animal(animal2)
zoo.add_employee(employee1)
zoo.add_employee(employee2)
zoo.add_employee(zoo_keeper)
zoo.add_employee(veterinarian)

# Демонстрация функционала зоопарка
zoo.show_animals()
zoo.show_employees()

# Специфические действия сотрудников
zoo_keeper.feed_animal(animal1)
veterinarian.heal_animal(animal2)
