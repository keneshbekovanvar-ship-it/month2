class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        edu = "есть высшее образование" if self.higher_education else "высшего образования нет"
        print(f"Меня зовут {self.name}, я родился {self.birth_date}, "
              f"по профессии {self.occupation}, {edu}.")


person1 = Person("Азамат","12.06.1999", "Программист", True)
person2 = Person("Айгерим", "03.09.2001", "Дизайнер", False)
person3 = Person("Бекзат", "25.01.1995", "Учитель", True)


print(person1.name, person1.birth_date, person1.occupation, person1.higher_education)
print(person2.name, person2.birth_date, person2.occupation, person2.higher_education)
print(person3.name, person3.birth_date, person3.occupation, person3.higher_education)

print()


person1.introduce()
person2.introduce()
person3.introduce()