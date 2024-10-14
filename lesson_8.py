# Глобальні та локальні змінні.
# Передача аргументів.
# Правило доступу до змінних LEGB
# Використання іменованих параметрів.
# аргументи за замовчуванням
# Використання змінної кількості аргументів
# Використання змінної кількості іменованих аргументів
# Тонкощі використання аргументів
# Розпакування кортежу в низку фактичних параметрів
# Розпакування словника в низку фактичних параметрів
# Особливості використання функцій






# import string
#
# input_str = input('Enter two letters hyphenated: ').split('-')  # z-a -> ["a", "c"]
#
#
# beginning = string.ascii_letters.find(input_str[0])
# ending = string.ascii_letters.find(input_str[-1])
#
# if beginning == -1 or ending == -1:
#     print("error")
# else:
#     print(string.ascii_letters[beginning:ending + 1])



# import string
#
# input_str = input('Enter two letters hyphenated: ').split('-')  # a-c -> ["a", "c"]
#
# beginning = string.ascii_letters.find(input_str[0])
# ending = string.ascii_letters.find(input_str[-1])
#
# if beginning == -1 or ending == -1:
#     print("error")
# else:
#     if beginning <= ending:
#         print(string.ascii_letters[beginning:ending + 1])
#     else:
#         print(string.ascii_letters[ending:beginning + 1][::-1]) # z-a   a-z










# total_seconds = int(input("Введіть кількість секунд (від 0 до 8639999): "))
#
# if 0 <= total_seconds < 8640000:
#
#     days, seconds_left = divmod(total_seconds, 86400)
#     hours, seconds_left = divmod(seconds_left, 3600)
#     minutes, seconds = divmod(seconds_left, 60)
#
#     if days % 10 == 1 and days % 100 != 11:
#         day_word = "день"
#     elif (2 <= days % 10 <= 4) and (days % 100 < 10 or days % 100 >= 20):
#     # elif 2 <= days % 10 <= 4:
#     #     if days % 100 < 10 or days % 100 >= 20:
#             day_word = "дні"
#     else:
#         day_word = "днів"
#
#     print(f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
#
# else:
#     print("Введене число повинно бути від 0 до 8639999.")







# number = int(input("Enter number: "))  #999
#
# result = 1
#
# while number > 9:
#     for digit in str(number):
#         result *= int(digit)
#     number = result  # після першого кроку 729
#     result = 1
#
# print(number)




# eval("1*2*2")

# number = int(input("Enter number: ")) or 1
#
# while number > 9:
#     number = eval('*'.join(str(number)))  #"9*9*9"
#
# print(number)


# Глобальні та локальні змінні.
# Передача аргументів.
# Правило доступу до змінних LEGB
# Використання іменованих параметрів.
# аргументи за замовчуванням
# Використання змінної кількості аргументів
# Використання змінної кількості іменованих аргументів
# Тонкощі використання аргументів
# Розпакування кортежу в низку фактичних параметрів
# Розпакування словника в низку фактичних параметрів
# Особливості використання функцій



# def adding_numbers(num_1, num_2):
#     if num_1 == 0:
#         return None
#     else:
#         result = num_1 + num_2
#         return result
# #
#
# print(adding_numbers(0, 4))


# LEGB - local, enclosing, global, built-in

# from math import pi

# pi = "global"
#
# def outer():
#     pi = "enclosing"
#
#     def inner():
#         pi = "local"
#         # global pi
#
#         # pi += "!!!!!"
#
#         print(pi)
#
#     inner()
#
# outer()
# # print(pi)


# value_int = 10
# value_int += 1


# def adding_numbers(num_1, num_2):
#     result = 0
#     if num_1 != 0:
#         result = num_1 + num_2
#     print(locals())
#
#     return result
#
# print(adding_numbers(9, 3))


# import operator
#
# actions = {
#     "+": operator.add,
#     "-": operator.sub,
#     "*": operator.mul,
#     "/": operator.truediv,
# }
#
# num_1 = float(input("num_1 "))
# action = input("action ")
# num_2 = float(input("num_2 "))
#
# # my_func = actions[action]
# my_func = actions.get(action)
# if my_func:
#     print(my_func(num_1, num_2))
# else:
#     print("Error")


# drukui = print
#
# drukui("Heello")



# def adding_numbers(num_1, num_2, num_3):
#
#     return num_1 + num_2 + num_3
#
#
# print(adding_numbers(1, 2, 3))

# IS_SEND_PENDING_EMAIL = True
#
# def print_line(fill, width, is_email=False):
#     for i in range(width):
#         print(fill, end="")
#
#     if is_email:
#         print("send email")
#
#
# # print_line("*", 6) # виклик в порядку черги
# # print_line(width=6, fill="*")  # іменований виклик
# # print_line("*", width=6, is_email=False)  # важлива черговість
# print_line("*", width=6, is_email=IS_SEND_PENDING_EMAIL)
# print_line("*", width=6)



# print(1, 3, 4)

# def print_line(fill, width):
#     for i in range(width):
#         print(fill, end="")
#
#
# print(print_line("*", 8, 9))


# *args

# def print_line(*args):
#     return args
#
# print(print_line(1, 2, 3, 4))


# value_list = [1, 2, 3]
# val_1, *tmp = value_list
#
# print(val_1)
# print(tmp)

#
# def print_line(*args):
#     return args
#
# print(print_line(1, 2, 3, 4))

# kwargs

# def say_hi(name):
#     print(f"Hi {name}")
#
# def say_age(age):
#     print(f"{age}")
#
#
# def print_line(fill, width, **kwargs):
# # def print_line(fill, width, name, age, name, age, name, age, name, age, name, age, name, age, name, age, name, age):
#     for i in range(width):
#         print(fill, end="")
#
#     print(kwargs)
#
#     say_hi(kwargs.get("name", "John"))
#
#     if kwargs.get("age"):
#         say_age(kwargs.pop("age"))
#
#
# print_line("*", 6, name_1="Nick", age=19, age_1=19, age_2=19, age_3=19, )


# def create_group(*args):
#     group_dict = {"teacher": "Nick", "group": list(args)}
#
#     # for i in args:
#     #     group_dict["group"].append(i)
#
#     return group_dict
#
# print(create_group("Nick", "Alex", "Dmytro", "Sergiy"))

# def adding_numbers(num_1: int, num_2: int) -> int:
#     """This func is doing something useful"""
#     return num_1 + num_2
#
# print(adding_numbers(8, 9))



# def my_func():
#     return 10
#
# # print(my_func())
#
#
# if __name__ == "__main__":
#     print(my_func.__doc__)
#     print(my_func.__name__)
#     print(my_func.__module__)

