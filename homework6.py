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


class Zoo():
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

    def save_to_txt(self, filename):
        """Сохраняет текущее состояние зоопарка в текстовый файл"""
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("Животные:\n")
            for animal in self.animals:
                file.write(f"{animal.name},{animal.species},{animal.age}\n")
            file.write("\nСотрудники:\n")
            for employee in self.employees:
                file.write(f"{employee.name},{employee.position}\n")
        print(f"Состояние зоопарка сохранено в текстовый файл {filename}")

    @staticmethod
    def load_from_txt(filename):
        """Загружает состояние зоопарка из текстового файла"""
        try:
            zoo = Zoo()
            with open(filename, 'r', encoding='utf-8') as file:
                section = None
                for line in file:
                    line = line.strip()
                    if line == "Животные:":
                        section = "animals"
                    elif line == "Сотрудники:":
                        section = "employees"
                    elif section == "animals" and line:
                        name, species, age = line.split(',')
                        zoo.add_animal(Animal(name, species, int(age)))
                    elif section == "employees" and line:
                        name, position = line.split(',')
                        if position == "Смотритель зоопарка":
                            zoo.add_employee(ZooKeeper(name))
                        elif position == "Ветеринар":
                            zoo.add_employee(Veterinarian(name))
                        else:
                            zoo.add_employee(Employee(name, position))
            print(f"Состояние зоопарка загружено из текстового файла {filename}")
            return zoo
        except FileNotFoundError:
            print(f"Файл {filename} не найден.")
            return None

    # Пример использования
zoo = Zoo()
zoo.add_animal(Animal("Лео", "Лев", 5))
zoo.add_animal(Animal("Эля", "Слон", 10))
zoo.add_employee(ZooKeeper("Алексей"))
zoo.add_employee(Veterinarian("Ольга"))

    # Сохранение и загрузка данных в текстовый файл
zoo.save_to_txt("zoo_state.txt")
loaded_zoo = Zoo.load_from_txt("zoo_state.txt")
if loaded_zoo:
    loaded_zoo.show_animals()
    loaded_zoo.show_employees()