class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age


    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Возраст не может быть отрицательным!")


    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Гав-гав!"


class Cat(Animal):
    def make_sound(self):
        return "Мяу!"


dog = Dog("Шарик", 3)
cat = Cat("Мурка", 2)

print("Звуки животных:")
print(dog.get_name(), "говорит:", dog.make_sound())
print(cat.get_name(), "говорит:", cat.make_sound())


dog.set_name("Бобик")
dog.set_age(4)

cat.set_name("Снежок")
cat.set_age(3)

print("\nПосле изменения атрибутов:")
print(dog.get_name(), dog.get_age())
print(cat.get_name(), cat.get_age())
