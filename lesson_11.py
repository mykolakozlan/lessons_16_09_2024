#  pip install jupyter
# jupyter notebook




# text = "When I was One I had just begun When I was Two I was nearly new"
# words = ['i', 'was', 'three', 'near']
#
#
# def popular_words(txt, wrds):
#     text_words = txt.lower().split()
#
#     popular_dict_words = {word: text_words.count(word) for word in wrds}
#     # popular_dict_words = {word: 0 for word in words}
#     # popular_dict_words = {}
#     #
#     # # #
#     # # # # for word in text_words:
#     # for word in words:
#     #     # if word in words:
#     #     # popular_dict_words[word] = text_words.count(word)
#     #     popular_dict_words.update({word: text_words.count(word)})
#     #
#     return popular_dict_words
#
#     # return {word: text.lower().split().count(word) for word in words}
#
#
# assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
# print('OK')





# def difference(*numb_args):
#     if not numb_args:
#         result = 0
#     else:
#         result = max(numb_args) - min(numb_args)
#         result = round(result, 2)
#
#     return result


# def difference(*numb_args):
#     if not numb_args:
#         return 0
#
#     result = max(numb_args) - min(numb_args)
#     return round(result, 2)
#
#
# assert difference(1, 2, 3) == 2, 'Test1'
# assert difference(5, -5) == 10, 'Test2'
# assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
# assert difference() == 0, 'Test4'
# print('OK')



############### Files #####################

# write
# writelines

# filename = "test.txt"
#
# my_file = open(filename, "w")    # "w", "r", "a"
#
# my_file.write("Hello World")
# my_file.write("Hello World")
# my_file.write("Hello World")
# my_file.write("Hello World")
#
# my_file.close()


filename = "test.txt"
#
#
# with open(filename, "w") as my_file:
#     my_file.write("Hello World1\n")


# value_list = ["red", "green", "apple", "hello"]

# my_file = open(filename, "w")    # "w", "r", "a"
# # for i in value_list:
# #   my_file.writelines(i + "\n")
# my_file.writelines(value_list)
#
# my_file.close()

# with open(filename, "w") as my_file:
#     my_file.writelines(value_list)


#read, readlines, readline

# with open(filename, "r") as my_file:
#     data = my_file.read()
#
# print(data, type(data))


# with open(filename, "r") as my_file:
#     data = my_file.readlines()
#
# print(data, type(data))

# with open(filename, "r") as my_file:
#     print(my_file.readline())
#     print(my_file.readline())
#     print(my_file.readline())
#     print(my_file.readline())
#     print(my_file.readline())


# with open(filename, "a") as my_file:
#     data = my_file.write("Nikolas")


# with open(filename, "a+") as my_file:
#     data = my_file.write("\nhello")
#     my_file.seek(4)
#     context = my_file.read()
#     print(context)

# value_list = ["red", "green", "apple", "hello"]
#
#
# with open(filename, "wb") as my_file:    # t -text(default), b - binary(ex sound, video, image)
#     my_file.writelines(value_list)

# value_list = ["red", "green", "apple", "hello"]
#
#
# with open(filename, "w", encoding="UTF-8") as my_file:
#     my_file.writelines(value_list)


############# OOP ###############


# class MyCar(object):
#     pass


# class MyCar:
#     color = "red"
#     engine = "2000"                 # атрибути класу



#
#
# car_1 = MyCar()                 # екземпляр класу
# car_2 = MyCar()                 # екземпляр класу
#
# print(car_1)
# car_1.color = "green"
# car_1.body = "sedan"                    # атрибут екземпляру класу
#
#
# print(car_1.color)
# print(car_1.engine)
# print(car_1.body)
#
# print(car_2)
# print(car_2.color)
# print(car_2.engine)



# value_str = "hello"
# print(type(value_str))
# value_str.title()
#
# str





















