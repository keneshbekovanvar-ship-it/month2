from blessed import Terminal
from homework_1 import Person

term = Terminal()


p1 = Person("Иван", "20.02.2000", "студент", True)
p2 = Person("Анна", "15.05.1999", "дизайнер", False)

p1.introduce()
p2.introduce()

print()


fruits = [
    "🍎 Apple",
    "🍌 Banana",
    "🍊 Orange",
    "🍇 Grape",
    "🍓 Strawberry",
    "🍍 Pineapple",
    "🍒 Cherry"
]

colors = [
    term.red,
    term.yellow,
    term.darkorange,
    term.purple,
    term.hotpink,
    term.green,
    term.cyan
]


for fruit, color in zip(fruits, colors):
    print(color + fruit + term.normal)
