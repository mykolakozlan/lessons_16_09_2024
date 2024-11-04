# import codecs
#
#
# def delete_html_tags(html_file: str, result_file: str = 'cleaned.txt') -> None:
#
#     with codecs.open(html_file, 'r', 'utf-8') as file:
#         html_code = file.read()
#
#     # cleaned_text = []
#     cleaned_text = ""
#     is_tag = False
#
#     for char in html_code:
#         if char == '<':
#             is_tag = True
#         elif char == '>':
#             is_tag = False
#         elif not is_tag:
#             # cleaned_text.append(char)
#             cleaned_text += char
#
#     # cleaned_text = ''.join(cleaned_text)
#     cleaned_text = '\n'.join(line.lstrip() for line in cleaned_text.splitlines() if line.strip())
#
#     with codecs.open(result_file, 'w', 'utf-8') as file:
#         file.write(cleaned_text)
#
#
# delete_html_tags('draft.html', 'cleaned.txt')


# import codecs
# import re
#
#
# def delete_html_tags(html_file, result_file='cleaned.txt'):
#     with codecs.open(html_file, 'r', 'utf-8') as file:
#         html = file.read()
#
#     clean_text = re.sub(r'<[^>]+>', '', html)
#
#     cleaned_lines = [line for line in clean_text.splitlines() if line.strip()]
#     clean_text_no_empty_lines = '\n'.join(cleaned_lines)
#
#     with codecs.open(result_file, 'w', 'utf-8') as file:
#         file.write(clean_text_no_empty_lines)
#
#     print(f"HTML-теги та пусті рядки видалено. Текст збережено в '{result_file}'.")
#
#
# delete_html_tags("draft.html")




# from bs4 import BeautifulSoup
# import codecs
#
#
# def delete_html_tags(html_file, result_file='cleaned.txt'):
#
#     with codecs.open(html_file, 'r', 'utf-8') as file:
#         soup = BeautifulSoup(file, 'html.parser')
#         text = soup.get_text(separator=' ').strip()
#
#     with open(result_file, 'w', encoding='utf-8') as result:
#         for line in text.split('\n'):
#             cleaned_line = line.strip()
#             if cleaned_line:
#                 result.write(cleaned_line + '\n')
#
#
# delete_html_tags("draft.html", "cleaned.txt")



# class Item:
#
#     def __init__(self, name, price, description, dimensions):
#         self.price = price
#         self.description = description
#         self.dimensions = dimensions
#         self.name = name
#
#     def __str__(self):
#         return f"{self.name}, price: {self.price}. "
#
#
# class User:
#
#     def __init__(self, name, surname, numberphone):
#         self.name = name
#         self.surname = surname
#         self.numberphone = numberphone
#
#     def __str__(self):
#         return f"{self.name} {self.surname}"
#
#
# class Purchase:
#     def __init__(self, user):
#         self.products = {}
#         self.user = user
#         self._total = 0
#
#     def add_item(self, item, cnt):
#         self.products[item] = cnt
#
#     def _get_total(self):
#         total = 0
#         for key, cnt in self.products.items():
#             total += key.price * cnt
#
#         self.total = total
#         return total
#
#     def __str__(self):
#         '''Метод виведення інформації про кошик'''
#         tmp = f'User: {self.user} \n'
#         for item, cnt in self.products.items():
#             tmp += f"Items:\n{str(item)}: {cnt} pcs. \n"
#         return tmp

#
# lemon = Item('lemon', 5, "yellow", "small", )
# apple = Item('apple', 2, "red", "middle", )
# # print(lemon)  # lemon, price: 5
#
#
# buyer = User("Ivan", "Ivanov", "02628162")
# # print(buyer)  # Ivan Ivanov
#
# cart = Purchase(buyer)
# cart.add_item(lemon, 4)
# cart.add_item(apple, 20)
# print(cart)
# """
# User: Ivan Ivanov
# Items:
# lemon: 4 pcs.
# apple: 20 pcs.
# """
# assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
# assert cart.get_total() == 60, "Всього 60"
# assert cart.get_total() == 60, 'Повинно залишатися 60!'
# cart.add_item(apple, 10)
# print(cart)
# """
# User: Ivan Ivanov
# Items:
# lemon: 4 pcs.
# apple: 10 pcs.
# """
# assert cart.get_total() == 40


################ Imports ###########
#
# import math
# from math import *

# from math import pi
# import sys
# import requests

# 1. Built-in (sys, time)
# 2. Standart libreries(math, json, os)
# 3. Сторонні бібліотеки(pip)
# 4. Створені модулі та пакети в нашому проекті

# print(sys.builtin_module_names)

# print(requests.__name__)
# print(requests.__doc__)
# print(requests.__file__)



################ Поліморфізм ###########

# res = 1 + 2
# res = "1" + "2"


# /,*, **, -, +

# __add__	__radd__	__iadd__	Складання чи конкатенація
# __sub__	__rsub__	__isub__	Віднімання
# __mul__	__rmul__	__imul__	Множення чи повторення
# __truediv__	__rtruediv__	__itruediv__	Справжній поділ
# __floordiv__	__rfloordiv__	__ifloordiv__	Поділ із округленням
# __mod__	__rmod__	__imod__	Розподіл по модулю
# __pow__	__rpow__	__ipow__	Зведення на ступінь



# class Box:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __add__(self, other):
#         # return Box(self.x + other.x, self.y + other.y, self.z + other.z)
#         return Box(self.x + other.x, self.y, self.z)
#
#     def __str__(self):
#         return f"Box [x = {self.x}, y = {self.y}, z = {self.z}]"
#
#
# box_a = Box(1, 2, 3)
# box_b = Box(2, 3, 4)
#
# # box_c = box_a + box_b
# # print(box_c)
#
# # box_a += box_b
# box_a += 1 # error
# #
# print(box_a)




# some_num = "10"
#
# if isinstance(some_num, str):
#     some_num = int(some_num)


# num = "10"
#
# if isinstance(num, str):
#     num = int(num)




# class Box:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __str__(self):
#         return "Box [x = {}, y = {}, z = {}]".format(self.x, self.y, self.z)
#
#     def __iadd__(self, other):
#         if isinstance(other, Box):
#             print("iadd")
#             return Box(self.x + other.x, self.y + other.y, self.z + other.z)
#         return NotImplemented
#
#     def __add__(self, other):
#         print(type(other))
#         if isinstance(other, Box):
#             print("add")
#             return Box(self.x + other.x, self.y + other.y, self.z + other.z)
#         return NotImplemented
#
#
# box_a = Box(1, 2, 3)
# box_b = Box(2, 3, 4)
# #
# # box_a += box_b
# # box_c = box_a + box_b
#
# box_a += 1 # error
# # #
# print(box_a)
#
# box_c = box_a + box_b
# print(box_c)

# box_a += 1 # error


# box_d = box_a + 1 # TypeError говорить про те, що для даного типу операцій ми не маємо реалізації

# # Подібна помилка, коли ми спробуємо знайти суму числа та рядки
# 1 + '1'








# class Box:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __str__(self):
#         return "Box [x = {}, y = {}, z = {}]".format(self.x, self.y, self.z)
#
#     def __iadd__(self, other):
#         return Box.__add__(self, other)
#
#     def __add__(self, other):
#         print("add")
#         if isinstance(other, Box):
#             return Box(self.x + other.x, self.y + other.y, self.z + other.z)
#         if isinstance(other, (int, float)):
#             return Box(self.x + other, self.y + other, self.z + other)
#         return NotImplemented
# #
# #
# box_a = Box(1, 2, 3)
# # box_d = box_a + 10
# # print(box_d)
# box_e = 10 + box_a
# print(box_e)
#
# box_a += 20.0
# print(box_d)



# box_d = 10.0 + box_a #  __radd__ not implemented
















import numbers


# class Box:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __str__(self):
#         return "Box [x = {}, y = {}, z = {}]".format(self.x, self.y, self.z)
#
#     def __iadd__(self, other):
#         return Box.__add__(self, other)
#
#     def __radd__(self, other):
#         """Оскільки метод __radd__ викликається у операнда, який знаходиться праворуч від знака +,
#         то self - це екземпляр класу Box,
#         а other - це операнд, який знаходиться ліворуч від знака +"""
#         print("radd")
#         return Box.__add__(self, other)
#
#     def __add__(self, other):
#         if isinstance(other, Box):
#             print("add")
#             return Box(self.x + other.x, self.y + other.y, self.z + other.z)
#         #  замість int, float перевіряємо приналежність до numbers.Real
#         if isinstance(other, numbers.Real):
#             return Box(self.x + other, self.y + other, self.z + other)
#         return NotImplemented
#
#     # помножити Box на число
#     def __mul__(self, other):
#         if isinstance(other, Box):
#             print("add")
#             return Box(self.x * other.x, self.y * other.y, self.z * other.z)
#         #  замість int, float перевіряємо приналежність до numbers.Real
#         if isinstance(other, numbers.Real):
#             return Box(self.x * other, self.y * other, self.z * other)
#         return NotImplemented
#
# #
# box_a = Box(1, 2, 3)
# box_d = 10 + box_a
# print(box_d)
# box_e = box_a * (10 + box_a)
# print(box_e)

# box_a += 20.0
# print(box_a)


# my_list = [1, 2, 3]
# my_list_2 = [11, 21, 31]
#
# # my_list += my_list_2
# # print(my_list)
# my_list_3 = my_list + my_list_2
# print(my_list_3)









# x.__eq__(y)	y.__eq__(x)	Рівне ==
# x.__ne__(y)	y.__ne__(x)	Не дорівнює
# x.__gt__(y)	y.__lt__(x)	x більше y
# x.__lt__(y)	y.__gt__(x)	x менше за y
# x.__ge__(y)	y.__le__(x)	x більше чи дорівнює y
# x.__le__(y)	y.__ge__(x)	x менше або дорівнює y







# import numbers
#
# class Box:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __iadd__(self, other):
#         return  Box.__add__(self, other)
#
#     def __radd__(self, other):
#         return  Box.__add__(self, other)
#
#     def __add__(self, other):
#         if isinstance(other, Box):
#             print("add")
#             return Box(self.x + other.x, self.y + other.y, self.z + other.z)
#         if isinstance(other, numbers.Real):
#             return Box(self.x + other, self.y + other, self.z + other)
#         return NotImplemented
#
#     def __mul__(self, other):
#         if isinstance(other, numbers.Real):
#             return Box(self.x * other, self.y * other, self.z * other)
#         return NotImplemented
#
#     def volume(self):
#         return self.x * self.y * self.z
#
#     def __eq__(self, other):
#         if isinstance(other, Box):
#             # дві коробки вважаються рівними у разі рівності об'ємів
#             return self.volume() == other.volume()
#         return NotImplemented
#
#     def __gt__(self, other):
#         if isinstance(other, Box):
#             return self.volume() > other.volume()
#         return NotImplemented
#
#     # def __lt__(self, other):
#     #     #if isinstance(other, Box):
#     #        # return self.volume(self) < self.volume(other)
#     #     #return NotImplemented
#     #     return not self > other
#
#     def __str__(self):
#         return "Box [x = {}, y = {}, z = {}]".format(self.x, self.y, self.z)
#
#
# box_a = Box(1, 2, 3)
# box_b = Box(3, 2, 1)
# # print(box_a == box_b)
# # #
# box_c = box_a + box_b
# # print(box_c == box_b)
# # print(box_c > box_b)
# # print(box_b < box_c)
# # # # #
# print(box_c >= box_b) # TypeError немає реалізації методу більше або дорівнює








# class Box:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __str__(self):
#         return "Box [x = {}, y = {}, z = {}]".format(self.x, self.y, self.z)
#
#     def __iadd__(self, other):
#         return Box.__add__(self, other)
#
#     def __radd__(self, other):
#         return Box.__add__(self, other)
#
#     def __add__(self, other):
#         if isinstance(other, Box):
#             print("add")
#             return Box(self.x + other.x, self.y + other.y, self.z + other.z)
#         if isinstance(other, numbers.Real):
#             return Box(self.x + other, self.y + other, self.z + other)
#         return NotImplemented
#
#     def __mul__(self, other):
#         if isinstance(other, numbers.Real):
#             return Box(self.x * other, self.y * other, self.z * other)
#         else:
#             return NotImplemented
#
#     @staticmethod
#     def volume(box):
#         return box.x * box.y * box.z
#
#     def __eq__(self, other):
#         if isinstance(other, Box):
#             return self.volume(self) == self.volume(other)
#         return NotImplemented
#
#     def __gt__(self, other):
#         if isinstance(other, Box):
#             return self.volume(self) > self.volume(other)
#         return NotImplemented
#
#     def __lt__(self, other):
#         if isinstance(other, Box):
#             return not self > other
#         return NotImplemented
#
#     def __ge__(self, other):
#         if isinstance(other, Box):
#             return any((self > other, self == other))
#         return NotImplemented
#
#     def __le__(self, other):
#         if isinstance(other, Box):
#             return any((self < other, self == other))
#         return NotImplemented
#
#     def __ne__(self, other):
#         return not self == other
#
# box_a = Box(1, 2, 3)
# box_b = Box(1, 2, 3)
# print(box_a >= box_b)
# box_c = box_a + box_b
# print(box_c >= box_b)
# print(box_a <= box_b)
# print(all([1, 0, True]))
# print(any([1, 0, True]))


# all()  # and
# any()  # or





# len()       __len__









########### Incapsulation #########


# Стандартна реалізація класу
# class Cat:
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
#         # self._color = color
#         # self.__color = color
#
#     @staticmethod
#     def get_voice():
#         return "Meow"
#
#     def encrease_age(self, one):
#         self.age += one
#         # return self.age
#
#     def count_age(self, one):
#         age = self.encrease_age(one) # None
#         return self.age
#
#     def __str__(self):
#         msg = "Cat [ name = {}, age = {}, color ={}]"
#         return msg.format(self.name, self.age, self.color)
# # #
# cat = Cat('Barsik', 3, 'black')
# print(cat.get_voice())
# # print(cat._color)
# print(cat._Cat__color)
#
# cat._Cat__color = "white"
# print(cat._Cat__color)




# def adding(num_1, num_2):
#     _res = num_1 + num_2
#     return _res





# print(cat.color)
# cat.color = "green"
# print(cat.color)

# print(cat._color)
# cat._color = "green"
# print(cat._color)

# print(cat._Cat__color)
# cat._Cat__color = "green"
# print(cat._Cat__color)














# # Можна без особливих зусиль змінити значення поля
# cat.color = 'white'
# print(cat.color)


# def adding(num_1, num_2):
#     _res = num_1 + num_2
#     return _res



# barsik_dict = cat.__dict__
# print(barsik_dict)
# print(barsik_dict["name"])

















# __dict__
# __slots__















# class Cat:
#     __slots__ = ("name", "age", "color")
#
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
#
#     def __str__(self):
#         msg = "Cat [ name = {}, age = {}, color = {}]"
#         return msg.format(self.name, self.age, self.color)
#
# #
# # cat_str = "Cat [ name = Barsic, age = 3, color = black]"
# # #
# cat = Cat('Barsik', 3, 'black')
# print(cat)
# # print(cat_str)
# # cat.type = "Simple cat"
# # print(cat.type)
# cat.name = "Tom"
# print(cat)


# len()







# Робота з методами __getattribute__, __getattr__, __setattr__ та __delattr__

# __getattribute__ - викликається автоматично при спробі набути значення певного або невизначеного (відсутнього) поля класу.
# __getattr__ - викликається автоматично при спробі отримати значення невизначеного поля класу.
# __setattr__ - викликається при спробі надати значення будь-якому полю класу (певного та невизначеного)
# __delattr__ – викликається при видаленні поля.






# class Cat:
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
#
#     def __str__(self):
#         msg = "Cat [ name = {}, age = {}, color ={}]"
#         return msg.format(self.name, self.age, self.color)
#
#
# cat = Cat('Barsik', 3, 'black')
# print(cat.name)
# print(cat.type) # Звернення до поля, якого немає


# class Cat:
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
#
#     def __str__(self):
#         msg = "Cat [ name = {}, age = {}, color ={}]"
#         return msg.format(self.name, self.age, self.color)
#
#     def __getattr__(self, atr_name):
#         print(atr_name)
#         # if atr_name in self.__dict__.keys()
#         return None # pass
#
#
# cat = Cat('Barsik', 3, 'black')
# print(cat.type) # Звернення до поля, якого немає
# print(cat.name)


# print(getattr(cat, 'age')) # 3
# print(getattr(cat, 'type')) # None
# print(getattr(cat, 'x'))  # None










# import math





# #
# PI = getattr(math, 'pi')
# print(PI)  # 3.141592653589793
# pow_math = getattr(math, 'pow')
# print(pow_math)
# print(pow_math(4, 2))
#
#
#
# fields = ['age', 'name', 'color']
#
# print(cat.age)
# print(cat.name)
# print(cat.color)
#
# for field in fields:
#     print(getattr(cat, field))




# from module import add_one

# import module
#
# module.add_one()


