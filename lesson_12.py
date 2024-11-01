#
#
# # def pow(x):
# #     return x ** 2
# #
# # def some_gen(begin, end, func):
# #     """
# #      begin: перший елемент послідовності
# #      end: кількість елементів у послідовності
# #      func: функція, яка формує значення для послідовності
# #     """
# #     for _ in range(end):
# #         yield begin
# #         begin = func(begin)
# #
# #
# #
# #
# # from inspect import isgenerator
# #
# # gen = some_gen(2, 4, pow)
# #
# # assert isgenerator(gen) == True, 'Test1'
# # assert list(gen) == [2, 4, 16, 256], 'Test2'
# #
# # print('OK')
#
#
# # import re
# #
# # # f""
# # # r""
# # # r"[a-zA-Z']+"
# # # r"\d{12}" номер телефону з 12 цифр    \w [a-zA-Z'] [А-Я] [а-яіїґ]- words    \d [0-9]- digits
# #
# #
# # # def first_word(text):
# # #     """ Пошук першого слова """
# # #     temp = text.replace('.','').replace(',','')
# # #     return temp.split()[0]
# #
# # def first_word(text: str) -> str :
# #     match = re.search(r"[a-zA-Z']+",text)
# #     if match:
# #         return match.group(0)
# #     return ''
# #
# # assert first_word("Hello world") == "Hello", 'Test1'
# # assert first_word("greetings, friends") == "greetings", 'Test2'
# # assert first_word("don't touch it") == "don't", 'Test3'
# # assert first_word(".., and so on ...") == "and", 'Test4'
# # assert first_word("hi") == "hi", 'Test5'
# # assert first_word("Hello.World") == "Hello", 'Test6'
# # print('OK')
#
#
# # def is_even(digit):
# #     return digit % 2 == 0
# #
# # assert is_even(2) == True, 'Test1'
# # assert is_even(5) == False, 'Test2'
# # assert is_even(0) == True, 'Test3'
# # print('OK')
#
#
# ######################################################## OOP ##################################################################
#
# #  Інкапсуляція Поліморфізм Спадкування                    Абстракція Композиція
#
#
# # class Car(object):
# # class Car:
# #     color = "red"
# #
# #     def __init__(self, color, engine, price):
# #         self.color = color
# #         self.engine = engine
# #         self.price = price
# #
# #
# # # car_1 = Car()
# # car_1 = Car("white", 1.8, 15000)
# # # car_1.body = "sedan"
# #
# # print(car_1)
# # print(car_1.color)
# #
# # car_2 = Car("green", 1.8, 15000)
# # # car_1.body = "sedan"
# #
# # print(car_2)
# # print(car_2.color)
#
#
#
#
# # class Cat:
# #
# #     def __new__(cls, *args, **kwargs): # метод, який насправді створює екземпляр класу
# #         print("Creating Cat instance")
# #         self = super().__new__(cls) # про функцію super() трохи пізніше
# #         print(self)
# #         return self # instance
# #
# #     def __init__(self, name, age, color): # метод додавання атрибутів у екземпляр класу
# #         print("Cat instance fields")
# #         self.name = name
# #         self.age = age
# #         self.color = color
# #
# # cat = Cat('Barsik', 5, 'black')
# # print(cat.age)
#
#
#
#
#
# # class Cat:
# #     """This is our cats"""
# #     def __init__(self, name, age, color): # метод додавання атрибутів у екземпляр класу
# #         # print("Cat instance fields")
# #         self.name = name
# #         self.age = age
# #         self.color = color
# #
# #     def cat_sound(self):
# #         return "Meow"
# #
# #     def __str__(self):
# #         return f"Hi my name is {self.name}. I'm {self.age} years old"
# #
# #     def __repr__(self):
# #         return f"Cat {self.name}"
# #
# #
# # cat_1 = Cat('Barsik', 5, 'black')
# # cat_2 = Cat('Tom', 2, 'black')
# #
# # cat_list = [cat_1, cat_2]
# #
# # print(cat_list[0])
# # print(cat_list)
# # # print(cat)
# # # print(cat.__str__())
# # # print(cat.__doc__)
# # # print(cat.cat_sound())
# #
# # # print(cat_1)
# # # print(cat.cat_sound())
#
#
# # def cat_sound():
# #     return "Meow"
# #
# #
# # class Cat:
# #     """This is our cats"""
# #     def __init__(self, name, age, color): # метод додавання атрибутів у екземпляр класу
# #         # print("Cat instance fields")
# #         self.name = name
# #         self.age = age
# #         self.color = color
# #
# #     def __str__(self):
# #         return f"Hi my name is {self.name}. I'm {self.age} years old"
# #
# #     def __repr__(self):
# #         return f"Cat {self.name}"
# #
# #     @staticmethod
# #     def cat_sound(name):
# #         return name + " Meow"
#
#
# # cat_1 = Cat('Barsik', 5, 'black')
# # cat_2 = Cat('Tom', 2, 'black')
# #
# # cat_list = [cat_1, cat_2]
#
# # print(Cat.cat_sound("Tom"))
#
# # print(cat_list[0])
# # print(cat_list)
# # print(cat)
# # print(cat.__str__())
# # print(cat.__doc__)
# # print(cat_1.cat_sound())
#
# # print(cat_1)
# # print(cat.cat_sound())
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# class Phone:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.price = price
#         self.model = model
#
#     def __str__(self):
#         return f'Phone {self.brand} {self.model} {self.price}'
#
#
# class Laptop:
#     def __init__(self, brand, model, price):
#         # Важливо, щоб набір полів був схожим на інші класи, які зберігаються на складі
#         self.brand = brand
#         self.price = price
#         self.model = model
#
#     def __str__(self):
#         return f'Laptop {self.brand} {self.model} {self.price}'
#
#
#
#
#
# # Створимо кілька екземплярів класу Phone
# phone1 = Phone('Samsung', 'A52', 7000)
# # print(phone1)
# phone2 = Phone('Samsung', 'S11', 37000)
# phone3 = Phone('Samsung', 'A12', 4000)
# phone4 = Phone('Xiaomi', 'Redmi Note 11 ', 8700)
# phone5 = Phone('Xiaomi', '12 Lite', 17000)
# # print(phone5)
#
# # print(hash(phone1))
#
#
# class Warehouse:
#
#     def __init__(self, address):
#         self.address = address
#         self.storage = {}
#
#     def add_to_storage(self, item, value):
#         """ Метод додавання товару на склад """
#         self.storage[item] = value
#
#     def remove_from_storage(self, item):
#         """ Метод видалення товару зі складу """
#         value = self.storage.pop(item, None)
#         return value
#
#     def get_item_value(self, item):
#         """ Метод отримання кількості товару на складі """
#         return self.storage.get(item)
#
#     def get_total_value(self):
#         """ Метод отримання загальної вартості товару на складі """
#         total = 0
#         for key, cnt in self.storage.items():
#             total += key.price * cnt
#         return total
#
#     def __str__(self):
#         """ Метод виведення інформації про склад """
#         tmp = ''
#         for item, cnt in self.storage.items():
#             tmp += f'{str(item)}: {cnt} pcs. \n'
#         return f'Warehouse at {self.address} contains:\n{tmp} '
#
#
# wh = Warehouse('Kyiv, vul. Viskozna, 135')
# # print(wh.get_total_value())  # На складі нічого немає
# # #  Додамо на склад кілька телефонів і перевіримо деякі методи
# wh.add_to_storage(phone1, 40)
# wh.add_to_storage(phone2, 23)
# # print(wh.get_total_value())
#
# wh.add_to_storage(phone3, 4)
# wh.add_to_storage(phone4, 52)
# wh.add_to_storage(phone5, 22)
# # print(wh.get_total_value())
#
# # print(wh.get_item_value(phone2))
#
# # print(wh)
# # # # # Видалимо кілька телефонів і перевіримо інформацію по складу
# # print(wh.remove_from_storage(phone2))
# # print(wh.get_item_value(phone2))
# # print(wh)
#
#
#
#
#
# #  Додамо на склад кілька ноутбуків
# notebook = Laptop('HP', 'ProBook 450', 35000)
# notebook1 = Laptop('HP', 'Laptop 15s-eq2054ur', 42000)
# wh.add_to_storage(notebook, 10)
# wh.add_to_storage(notebook1, 3)
# # print(wh.get_total_value())
# print(wh)
#
#
#
#
# # class Cat:
# #     """This is our cats"""
# #     def __init__(self, name, age, color): # метод додавання атрибутів у екземпляр класу
# #         # print("Cat instance fields")
# #         self.name = name
# #         self.age = age
# #         self.color = color
# #
# #     def __str__(self):
# #         return f"Hi my name is {self.name}. I'm {self.age} years old"
# #
# #     def __repr__(self):
# #         return f"Cat {self.name}"
# #
# #     @staticmethod
# #     def cat_sound(name):
# #         return name + " Meow"
# #
# #
# # cat_1 = Cat('Barsik', 5, 'black')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # from datetime import date
# #
# # class Person:
# #
# #     # Дозволяє обчислити дані, і повернути новий екземпляр класу, з цими даними
# #     @classmethod
# #     def from_birth_year(cls, name, year):
# #         return Person(name, date.today().year - year)
# #
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #
# #     # Метод, який не пов'язаний зі змінними ні цього класу, ні його екземплярів
# #     @staticmethod
# #     def is_adult(age):
# #         return age > 18
# #     # # Метод, який не пов'язаний зі змінними ні цього класу, ні його екземплярів
# #     #
# #     # def is_adult(self):
# #     #     return self.age > 18
# #
# #
# # person1 = Person('Michael', 21)
# # person2 = Person.from_birth_year('John', 1996)
# # person3 = person2.from_birth_year('mayank3', 2000)
# #
# # print(person1.age)
# # print(person1.is_adult(person1.age))
# # print(person2.age)
# # print(person3.age)
#
#
#
# # class Animal:
# #
# #     def __init__(self, food, color):
# #             self.food = food
# #             self.color = color
# #
# #     def animal_sound(self):
# #         return "Animal says: "
# #
# #
# # class Tiger(Animal):
# #
# #     def __init__(self, food, color, name, age):
# #             self.name = name
# #             self.age = age
# #             super().__init__(food, color)
# #
# #     def animal_sound(self):
# #         return super().animal_sound() + "Rrhhh"
# #
# # tiger_1 = Tiger("meat", "orage", "Sebastian", 3)
# #
# # print(tiger_1)
# # print(tiger_1.animal_sound())
# # # print(tiger_1.food)
#
#
#
#
#
#
#
#
#
