# match/case
# list
# while
# break and continue
# while - else
# for
# for - else
# range()

# command + /(Mac) cntrl + /(Win) - comment all raws(lines)
# coomand + d(Mac) cntrl + d(Win) - дублювання

# numbers_from_input = int(input("Type sum num: "))
#
# thousands = numbers_from_input // 1000
# hundreds = numbers_from_input // 100 % 10
# tenth = numbers_from_input // 10 % 10
# ones = numbers_from_input % 10
#
# # print(f"{thousands}\n{hundreds}\n{tenth}\n{ones}")
# print(thousands, hundreds, tenth, ones, sep="\n")

# print(thousands)
# print(thousands)
# print(hundreds)
# print(tenth)
# print(ones)



# my_input = int(input("please add 4 digits: "))
#
# thousands, left_1 = divmod(my_input, 1000)
# hundreds, left_2 = divmod(left_1, 100)
# tenth, ones = divmod(left_2, 10)
#
# # print(f"{thousands}\n{hundreds}\n{tenth}\n{ones}")
# print(thousands, hundreds, tenth, ones, sep="\n")
# print(thousands)
# print(hundreds)
# print(tens)
# print(ones)
# result = (1, 3)

# my_list = [1, 2, 3, 4, 5, 6, 7]
#
# num_1, num_2, *tmp = my_list

# print(num_1)
# print(num_2)
# print(tmp)


# num_1, num_2 = 10, 100
#
# print(num_1)
# print(num_2)
#
# num_1, num_2 = num_2, num_1
#
# print(num_1)
# print(num_2)


# value_str = "hello"
#
# if (value_str == "hello") or (value_str == "bye"):
#     print("!!!!!!!!!!!!")
# else:
#     print("#############")
#



# weather = "hjghhuukhku"
#
# match weather:
#     case "cold":
#         print("it's cold")
#     case "hot":
#         print("it's hot")
#     case "rainy":
#         print("it's rainy")
#     case _:
#         print("Error")





############### List ###############


# value_list = [1, 2, 3]
# value_list.append("hello")
# value_list.append("hello1")
# value_list.append("hello2")
#
# print(value_list)


# value_list = [1, 2, 3] #88 byte
# value_list.append(1) #88 byte
# value_list.append(2) #88 byte
# value_list.append(3) #132 byte
# value_list.append(3) #132 byte


# value_list = [1, 2, 3]
# value_pop = value_list.pop()
#
# print(value_list)
# print(value_pop)


# value_list = [1, 2, 3]
# # value_list.insert(0, "hello")
# value_list.insert(4, "hello")
# value_list.insert(4, "hello1")
# value_list.insert(4, "hello2")
# value_list.insert(4, "hello3")
# print(value_list)

# value_list = [1, 2, 3, 5, 3, 1, 7]
# print(id(value_list))

# value_list_2 = value_list[::-1]
# print(value_list_2, id(value_list_2))
#
# value_list.reverse()
# print(value_list, id(value_list))

# value_list = [1, 2, 3, 5, 3, 1, -7]

# print(len(value_list))
# value_list = ["red", "yellow", "", "", "blue", "bblue"]

# value_list.sort(reverse=False, key=abs) # по модулю
# value_list.sort(reverse=False, key=len)
# value_list.sort(reverse=False, key=bool)
# value_list.sort(reverse=False)
# print(value_list)


# some_list = value_list.copy()
# some_list.sort()

# some_list = sorted(value_list, reverse=False, key=bool)
# print(some_list)


################# Loop ###############

# for, while
# break, continue, else

value_int = 0
is_true = True

# while True:
#     value_int += 1
#     print(value_int)
#     if value_int >= 10:
#         break
# else:
#     print(111111)

# while value_int < 10:
#     value_int += 1
#     print(value_int)

# count = 0
#
# while is_true:
#     value_int += 1
#     if value_int == 5:
#         continue
#     print(value_int)
#
#     if value_int >= 10:
#         is_true = False
# else:
#     print(111111)
#
#
# print("end")


# for, for - else, range()

# value_str = "hello"
# # value_list = [1, 2, 3]
# #
# # index = 0
# # while index < len(value_str):
# #     print(value_str[index])
# #     index += 1
#
#
# for letter in value_str:
#     print(letter)
#     # if letter == "o":
#     #     break
# else:
#     print("llllll")


# range()
# range(5)  від 0 до 5(виключно)
# range(2, 5)  від 2 до 5(виключно)
# range(2, 5, 2)  від 2 до 5(виключно) з кроком в 2

# for i in range(2, 5, 2):
#     print(i)


















# value_input = int(input("some number: "))
#
#
# thousands = value_input // 10000
# hundreds = value_input // 1000 % 10
# tenth = value_input // 100 % 10
# ones = value_input // 10 % 10
# one = value_input  % 10
#
# # print(f"{thousands}{hundreds}{tenth}{ones}{one}")
# print(f"{one}{ones}{tenth}{hundreds}{thousands}")
# # print(thousands, hundreds, tenth, ones, sep="\n")


# value_input = int("12345")
#
# num_1, left_1 = divmod(value_input, 10000)
# num_2, left_2 = divmod(left_1, 1000)
# num_3, left_3 = divmod(left_2, 100)
# num_4, left_4 = divmod(left_3, 10)
#
# result = left_4 * 10000 + num_4 * 1000 + num_3 * 100 + num_2 * 10 + num_1
# print(result)
# print(num_1,num_2,num_3,num_4,left_4, sep='')





























