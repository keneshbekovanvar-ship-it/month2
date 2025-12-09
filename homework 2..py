class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        print(f"Привет! Меня зовут {self.name}. Я родился {self.birth_date}, работаю {self.occupation}.")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name


    def introduce(self):
        print(
            f"Привет! Меня зовут {self.name}. "
            f"Я одноклассник/одногруппник, учусь в группе {self.group_name}. "
            f"Родился {self.birth_date}, работаю {self.occupation}."
        )


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby


    def introduce(self):
        print(
            f"Привет! Меня зовут {self.name}. "
            f"Я друг, мое хобби — {self.hobby}. "
            f"Родился {self.birth_date}, работаю {self.occupation}."
        )


classmate1 = Classmate("Бектур", "12.05.2005", "студент", True, "Backend-27")
classmate2 = Classmate("Айтуган", "03.02.2004", "студент", False, "Backend-27")

friend1 = Friend("Алмаз", "05.12.2000", "программист", True, "футбол")
friend2 = Friend("Айдана", "11.08.2001", "дизайнер", True, "рисование")

classmate1.introduce()
classmate2.introduce()
friend1.introduce()
friend2.introduce()


objects = [classmate1, classmate2, friend1, friend2,
           Person("Каныкей", "01.01.1999", "учитель", True)]

print("\n--- Дополнительное задание: вывод списка объектов ---")
for obj in objects:
    obj.introduce()