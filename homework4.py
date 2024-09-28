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

zoo = Zoo()

animal1 = Animal("Лео", "Лев", 5)
animal2 = Animal("Эля", "Слон", 10)
employee1 = Employee("Иван", "Дрессировщик")
employee2 = Employee("Мария", "Ветеринар")

zoo.add_animal(animal1)
zoo.add_animal(animal2)
zoo.add_employee(employee1)
zoo.add_employee(employee2)

zoo.show_animals()
zoo.show_employees()
