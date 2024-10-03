# tuple
# змінна "_"
# поняття dict
# основні методи dict(update(), get(), pop(), keys(), values(), items())


# 1
# value_list = [1, 0, 3, 0]
#
# for zero in range(len(value_list) - 1, -1, -1):
#     if value_list[zero] == 0:
#         value_list.append(value_list.pop(zero))
#
# print(value_list)
#
# # # 2
# my_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
# second_list = []
# zero = my_list.count(0)
#
# for index in range(len(my_list)):
#     if my_list[index] != 0:
#         second_list.append(my_list[index])
#
# second_list.extend([0] * zero)
# print(second_list)
#
# # 3
# my_list = [0, 9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
# zero = my_list.count(0)
#
# # for index in range(len(my_list)):
# for index in range(zero):
#     # if my_list[index] == 0:
#     my_list.remove(0)
#     my_list.append(0)
#
# print(my_list)
#
#
# # 4
# # import operator
#
#
# my_list = [0, 9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
#
# my_list.sort(reverse=True, key=bool)
# # my_list.sort(key=operator.not_)
#
# print(my_list)
#
# # # 5
# my_list = [0, 3, 5, 0, 4, 0, 7, 9]
#
# index = 0
#
# for i in range(len(my_list)):
#     if my_list[i] != 0:
#         my_list[i], my_list[index] = my_list[index], my_list[i]
#         index += 1
# print(my_list)


# 1
# my_list = [0, 1, 7, 2, 4, 8]
#
# result = 0
#
# for i in range(0, len(my_list), 2):
#     result += my_list[i]
#
# if my_list:
#     result = result * my_list[-1]

# sum(2, 3, 4)
# sum([2, 3, 4])
# sum((2, 3, 4))

# 2
# if my_list:
#     result = sum(my_list[::2]) * my_list[-1]
#
# print(result)


# from random import randint
#
# my_list = [randint(0, 30) for _ in range(randint(3, 10))]
# print(my_list)
# print([my_list[0], my_list[2], my_list[-2]])


# my_list = [
#     1,
#     2,
#     3,
#     4,
#     9,
#     10,
#     11,
# ]

# my_list = []
#
# for value in range(5):
#     my_list.append(value)

# my_list = [value ** 2 for value in range(5)]
#
# print(my_list)

# my_list = []
#
# for value in range(10):
#     if value % 2:
#         my_list.append(value ** 2)

# my_list = [value ** 2 for value in range(10) if value % 2]
#
# print(my_list)


# tuple
# змінна "_"
# поняття dict
# основні методи dict(update(), get(), pop(), keys(), values(), items())

######### Tuple ############

# value_list = [1, 2, 3]
#
# value_tuple = (1, 2, 3)
# value_tuple = tuple()
# value_tuple = ("1",)

# print(value_tuple, type(value_tuple))

# value_tuple = (1, 2, 3)

# value_tuple[9]
# value_tuple[1:3]
# value_tuple[::2]
# value_tuple[::-1]

# print(value_tuple[10:22])


# value_tuple = (1, 2, 3, True, "apple", [1, 2, 3])
# print(value_tuple)
#
# value_tuple[-1].append("hello")
# print(value_tuple)
# value_list = list(value_tuple)
# print(value_list)


################# _ ################

# value_tuple = (1, 2)
#
# # width, length, *tmp = value_tuple
# width, _, *tmp = value_tuple
#
# for _ in range(10):
#     print("hello")


########### Dict #############


# my_dict = {
#     "John": 26,
#     "Tom": 20,
#     1: 20,
#     1.2: 20,
#     True: 20,
#     None: 20,
#     (1, 2, 3, 4): 20,
#     [1, 2, 3, 4]: 20,
# }
#
# print(my_dict)

# print(hash("John"))
# print(hash(100))
# print(hash(1.5))

# my_dict = {
#     "John": [3, 4, 5],
#     "Tom": 20,
#     1: "red",
#     1.2: 20,
#     True: False,
#     None: 20,
#     (1, 2, 3, 4): {"12": 5},
# }
#
# print(my_dict)

# my_dict = dict(name="John", age=24, country="Ukraine")
#
# my_dict = {
#     "name": "John",
#     "age": 24,
#     "country": "Ukraine",
#     "grade": 4,
# }


# print(my_dict)
# print(my_dict["name"])

# my_dict["name"] = "Tom"
#
# print(my_dict["name"])

# my_dict["last_name"] = "Smith"

# print(my_dict["last_name"])

# email = my_dict.get("email", None)
#
# if not email:
#     print("ERROR: email is a mandatory field")
#
# print(email)


# my_dict = {
#     "name": "John",
#     "age": 24,
#     "country": "Ukraine",
#     "grade": 4,
# }

# print(my_dict.keys())

# for i in my_dict:
#     print(i)

# for key in my_dict.keys():
#     print(key)

# for value in my_dict.values():
#     print(value)

# for key, value in my_dict.items():
#     print(key, value)


# fromkeys()

# default_dict = dict.fromkeys(('name', 'age', 'country'), None)
# print(default_dict)


# default_dict = dict.fromkeys(('name', 'age', 'country'), [1, 2, 3])
#
# print(default_dict)
# default_dict['name'].append("Hello")
# print(default_dict)


# pop()

# my_dict = {
#     "name": "John",
#     "age": 24,
#     "country": "Ukraine",
#     "grade": 4,
#     "color": "red",
# }

# print(my_dict)

# del_value = my_dict.pop("name")
# print(my_dict)
#
# print(del_value)

# .update()
# print(my_dict)

# my_dict["color"] = "red"
# my_dict.update({"color": "yellow"})
#
# new_dict = {
#     "color": "red",
#     "size": 2
# }
#
# my_dict.update(new_dict)
#
# print(my_dict)


############## Dict comprehension #########

# my_list = []
#
# for value in range(5):
#     my_list.append(value)

# my_list = [value ** 2 for value in range(5)]
#
# print(my_list)

# my_dict = {}
#
# for value in range(5):
#     my_dict.update({value: f"This is {value}"})


# my_dict = {value: f"This is {value}" for value in range(5)}
#
# print(my_dict)


################## Set #################

# command + option + l (Mac) ctrl + alt + l

# value_list = [1, 2, "apple", "red", 3, 4, 5, 4, 2, 1, 1, 1]
# print(value_list)
# print(set(value_list))
