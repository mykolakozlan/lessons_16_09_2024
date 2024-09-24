# Bool, None types
# Logic operators
# Зведення типів
# Duck typing
# If statement (programming golf, Тернарний оператор)
# list
# змінні не змінні типи даних різниця
# методи list(append(), pop(), sort(), copy())
# функція sorted()

# незмінні

# float
# int
# complex
# decimal
#
# str
#
# bool
# None
#
# tuple

# Змінні

# list
# dict
# set

############ NoneType ############

# value_none = "hello"
#
# # value_id = id(value_none)
# value_print = print(value_none)
#
# print(value_print)

############ bool ############

# value_bool = True
# is_confirmed = True
# is_true = False


# value_float = 0.000000000000000000001
# print(bool(value_float))


# value_bool = True
# print(value_bool * 10)

# value_int = 400
# print(bool(value_int) * 8)

# value_str = ""
# print(bool(value_str))

############# Logic operators ################### >, <, >=, <=, ==, !=, in, not, is

# value_str = "Hello"
# value_str_2 = "Hello"

# print(value_int_1 > value_int_2)
# print(value_int_1 > value_int_2)
# print(value_str < value_str_2)

# print("He" in "Hello")
# print("He" not in "Hello")


# ===    ->   is
# value_int_1 = 1
# value_int_2 = 1.0
#
# print(value_int_1 == value_int_2)
# print(value_int_1 is value_int_2)


# if якась умова:
#     роби це(виконання)

# and or

# value_int = 11
#
# if value_int > 0 and value_int < 10:
# # if 0 < value_int < 10:
#     print(f"{value_int} is bigger than 0")
# elif value_int > 10: #else if
#     print(f"{value_int} is bigger than 10")
# else:
#     print(f"{value_int} is not bigger than 0")
#
#
#
# print("end")






# If statement (programming golf, Тернарний оператор)


# num_1 = 2
# num_2 = 330
#
#
# if num_1 > num_2:
#     result = "A"
# else:
#     result = "B"
#
#
# result = "A" if num_1 > num_2 else "B"
#
# print(result)



################# list #################

# some_list = list()


# value_str = "Hello"
#
# some_list = [1, 1.5, True, "hello", [1, 2, 3], value_str] # індексований обʼєкт від 0... і далі

# print(some_list)
# print(some_list[1])
# print(some_list[:3]) # від початку(0) до 3(виключно)
# print(some_list[3:]) # від 3-го до кінця
# print(some_list[3:5]) # від 3-го до 5(виключно)
# print(some_list[1:2] + some_list[4:6]) #
# print(some_list[1:8:2]) #



# ############################################

# base_list = [1, 2, 3]
# my_new_list = base_list * 4
# print(my_new_list)
# #
# #
# base_list[0] = 10
# #
# print(f"base_list {base_list}")
# print(f"my_new_list {my_new_list}")

# # # ######################################
#

# from copy import deepcopy
#
# base_list = [1, 2, 3, [True, False]]
# # base_list = [id, id, id, link]
#
# # new_list = [base_list.copy()] * 4
# new_list = [deepcopy(base_list)] * 4
# # new_list = [link, link, link, link]
# print(new_list)
#
# # base_list[0] = 10
# base_list[-1][0] = "hello"
# print(f"base_list {base_list}")
# print(new_list)

# # # ######################################

