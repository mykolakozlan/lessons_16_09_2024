

# first_symbol = float(input("1st num:  "))
# my_operator = input("operator (+, -, /, *):  ")
# second_symbol = float(input("2nd num:  "))
#
# result = None
#
# # if operator != "+" or operator != "-" or operator != "/" or operator != "*":
# # if operator not in "+-*/" or len(operator) != 1:
# # if operator not in ["+", "-", "*", "/"]:
# if my_operator not in ("+", "-", "*", "/"):
#     result = "ERROR - wrong operator"
#
#
# if my_operator == "+":
#     result = first_symbol + second_symbol
# elif my_operator == "-":
#     result = first_symbol - second_symbol
# elif my_operator == "*":
#     result = first_symbol * second_symbol
# elif my_operator == "/":
#     if second_symbol != 0:
#         result = first_symbol / second_symbol
#     else:
#         result = "ERROR - can't divide by zero"
# # else:
# #     result = "ERROR - wrong operator"
#
#
# print(result)








# original_list =  [12]
#
# # last_element = original_list[-1]
# # original_list.pop()
# #
# # original_list.insert(0, last_element)
#
# # if original_list:
# if len(original_list) > 1:
#     original_list.insert(0, original_list.pop())
#
# print(original_list)





# my_list = [1, 2, 3, 9, 4, 5, 6]
#
# separator = len(my_list) - len(my_list) // 2
# new_list = [my_list[:separator], my_list[separator:]]
#
# print(new_list)



############################ String #########################

# value_str = "hello"
# print(value_str, id(value_str))
# value_str = "hello!"
# print(value_str, id(value_str))

# print(value_str[0])
# print(value_str[1:4])
# print(value_str[14])
# print(value_str[14:18], type(value_str[14:18]))
# print(value_str[::2])
# print(value_str[::-1])

# value_str = "email@gmail.com"

# "Email@gmail.com"

# first_name = "Nick Dev"

# is_confirmed = True


# value_lower_case = value_str.lower()
# value_upper_case = value_str.upper()
# value_capital = first_name.capitalize()
# value_title = first_name.title()

# value_swapcase = first_name.swapcase()


# print(first_name)
# print(value_swapcase)


# value_str = "Nick Dev"
# # print(value_str.isalpha())
# print(value_str.isspace())


# if not value_str.isalpha():
#     value_float = float(value_str)
#     print(value_float)
#
#
# print("end")
#
# value_str = "hello"
#
# result = ""
#
# # for letter in value_str:
# #     if letter.isdigit():
# #         result += letter
#
# # print(result)
#
# # enumerate()
#
# for index, letter in enumerate(value_str):
#     print(index, letter)

# value_str = "hellool"

# some_method = value_str.find("loo")
# some_method_2 = value_str.rfind("loo")
# print(some_method)
# print(some_method_2)

# if value_str.startswith("h"):
#     print(True)
# value_str.endswith()

# count()

# value_str = "hellool"
# print(value_str.count("l"))

# split/join



# some_file = "C/My Computer/SomeFolder/12by345_6.png"

# split_method = some_file.split("/", 2)
# split_method = some_file.split()
# split_method = some_file.rsplit(".", 1)
# print(split_method)
#
# split_method[1] = "jpeg"
# print(split_method)
#
# join_method = ".".join(split_method)
#
# print(join_method)



# strip()


# first_name = "______Nick_________"
# value_strip = first_name.strip("_")
# value_rstrip = first_name.rstrip("_")
# value_lstrip = first_name.lstrip("_")
#
# print(first_name)
# print(value_strip)
# print(value_rstrip)
# print(value_lstrip)


# find()
# index()

# first_name = "______Nick_________"
# print(first_name.find("T"))
# print(first_name.index("T"))



############ ASCII ######################


# value_str = "hello"
# value_str_2 = "hеllo"


# value_letter = "А"
# print(ord(value_letter))
# print(chr(104))

# alphabet = ""
#
# for letter in range(ord("a"), ord("z") + 1):
#     # print(chr(letter), letter)
#     alphabet += chr(letter)
#
# print(alphabet)

# import this
#
# print(this)






































