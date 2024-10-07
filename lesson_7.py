# import keyword
# import string
#
# name_var = input("Please enter a name of variable: ")
# result = ""
#
# if name_var:
#     result = "True"
#
#     if name_var[0].isdigit():
#         result = "False"
#     elif keyword.iskeyword(name_var):
#         result = "False"
#     else:
#         for symbol_str in range(len(name_var)):
#         # for symbol_str in name_var:
#             if name_var[symbol_str].isupper():
#                 result = "False"
#             elif name_var[symbol_str].isspace():
#                 result = "False"
#             elif name_var[symbol_str] in string.punctuation and name_var[symbol_str] != "_":
#                 result = "False"
#             elif name_var[symbol_str] == "_":
#                 if symbol_str > 0 and name_var[symbol_str] == name_var[symbol_str-1]:
#                     result = "False"
#
# else:
#     result = "empty string"
#
# print(f'Name of variable "{name_var}" is {result}')




# my_string = input("Please enter your variable: ")
# result = False
#
# if my_string.isidentifier():
#     if my_string == "_" or my_string.islower():
#         result = True
#
# print(result)
















# import string
#
# input_string = 'Python Community'
# # input_string = 'i like python community!'
# # input_string = 'Should, I. subscribe? Yes!'
# # input_string = input("Write some string: ")
#
# words = ''.join(char for char in input_string if char not in string.punctuation).split()
#
# hashtag = '#' + ''.join(word.capitalize() for word in words)
#
# if len(hashtag) > 140:
#     hashtag = hashtag[:140]
#
# print(hashtag)





# some_val = "12wjjijiiljllk;111"
# result = ""
# for num in some_val:
#     if num.isdigit():
#         result += num
#
# print(result)



# Modified calculator
#
# while True:
#     number_1 = input('Enter the first number: ')
#
#     if not number_1.isdigit():
#         print('Undefined number! Try again.')
#         continue
#     number_1 = float(number_1)
#
#     action = input('Enter the operator: ')
#     if action not in ('+', '-', '/', '*'):
#         print('Undefined action! Try again.')
#         continue
#
#     number_2 = input('Enter the second number: ')
#     if not number_2.isdigit():
#         print('Undefined number! Try again.')
#         continue
#     number_2 = float(number_2)
#
#     result = 0
#
#     if action == '+':
#         result = number_1 + number_2
#     elif action == '-':
#         result = number_1 - number_2
#     elif action == '*':
#         result = number_1 * number_2
#     elif action == '/' and number_2 == 0:
#         result = str('Ділення на нуль неможливе!')
#     else:
#         result = number_1 / number_2
#
#     print(result)
#
#     var_cont = input('Do you want to continue? Y/N? ')
#     if var_cont.lower() != 'y':
#         print('Good bye!')
#         break



# collections OrderedDict (popitem, move_to_end)
# from collections import defaultdict

from collections import OrderedDict, defaultdict

# my_dict = {
#     "name": "John",
#     "age": 24,
#     "country": "Ukraine",
#     "grade": 4,
#     "color": "red",
# }
# print(my_dict)
#
# my_order_dict = OrderedDict(my_dict)    #[('name', 'John'), ('age', 24), ('country', 'Ukraine')]
# print(my_order_dict)

# my_dict = dict.fromkeys(["name", "age", "country"], False)
#
# print(my_dict)
# my_dict["name"].append("Nick")
# print(my_dict)

# my_dict = defaultdict(list)
#
# print(my_dict)
#
# for i in range(5):
#     my_dict[i].append(i * 5)
#
# print(my_dict)



# from collections import namedtuple
#
# val_tuple = (1, 2, 3)
# # val_list = [1, 2, 3]
#
#
# fields = (
#     "color",
#     "engine",
# )
#
# car = namedtuple("Car", fields)
# car_1 = car("red", 2.0)
#
# print(car_1)
# print(car_1.color)
# print(car_1.engine)



################ Set #############


# my_set_1  = {1, 2, 3}
# my_set_2  = {"apple", "red", "hi", "yes"}
# print(my_set_2)
#
# # print(my_set_1.union(my_set_2)) # обʼєднання
# # print(my_set_1.difference(my_set_2)) # видає унікальні елементи першого сету
# # print(my_set_1.intersection(my_set_2)) # перетин(ті значення які є в обох сетах)
#
# new_set = frozenset(my_set_2)
# print(new_set)







############################ Functions #############################

#
#
# def my_calc(number_1, number_2, operator):
#     result = 0
#
#     if operator == "+":
#         result = add_two_numbers(number_1, number_2)
#     elif operator == "-":
#         result = add_two_numbers(number_1, number_2)
#
#     # return None
#     return result
#
#
#
#
# def add_two_numbers(num_1, num_2):
#     """This func is doing something useful"""
#
#     result = num_1 + num_2
#
#     return result
#
#
# print(my_calc(2, 3, "+"))
#
#





def say_hi(name, age):
    pass


assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('ОК')

