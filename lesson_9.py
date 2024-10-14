# def say_hi(name, age):
#     # return " ".join(["Hi. My name is", name, "and I'm", str(age), "years old"])
#     return f"Hi. My name is {name} and I'm {age} years old"
#     # return "Hi. My name is " + name + " and I'm " + str(age) + " years old"
#     # return "Hi. My name is {} and I'm {} years old".format(name, age)
#
#
# assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'say_hi error: text is not correct'
# assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
# print("OK")


# def correct_sentence(text):
#     text = text.strip()
#
#     if text[0].islower():
#         text = text[0].upper() + text[1:]
#         # text = text.capitalize()
#
#     # if text[-1] != '.':
#     if not text.endswith("."):
#         text += "."
#
#     return text
#
# assert correct_sentence("Greetings, friends") == "Greetings, friends.", 'correct_sentence error: check for dot'
# assert correct_sentence("hello.") == "Hello.", 'correct_sentence error: check for capital letter'
# assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
# assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
# assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
# print('ОК')


# def second_index(text: str, some_str: str) -> str:
#     first_index = text.find(some_str)
#
#     if first_index == -1:
#         return None
#
#     seconds_index = text.find(some_str, first_index + len(some_str))
#
#     if seconds_index == -1:
#         return None
#
#     return seconds_index
#
#
# assert second_index("sims", "s") == 3, 'Test1'
# assert second_index("find the river", "e") == 12, 'Test2'
# assert second_index("hi", "h") is None, 'Test3'
# assert second_index("Hello, hello", "lo") == 10, 'Test4'
# print('ОК')


# def common_elements():
#     # multiples_of_3 = [num for num in range(100) if num % 3 == 0]
#     # multiples_of_5 = [num for num in range(100) if num % 5 == 0]
#
#     multiples_of_3 = {num for num in range(0, 100, 3)}
#     multiples_of_5 = {num for num in range(0, 100, 5)}
#
#     # return multiples_of_3 & multiples_of_5
#     return multiples_of_3.intersection(multiples_of_5)
#
#
#
# assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
# print('ОК')


# Функції частина 3:
#
# Функція як параметр для іншої функції
# Документування функцій
# Анотування типів у функціях
# Рекурсія
# Анонімні функції lambda
# map, filter, zip
# Функції генератори yield


# args kwargs


# def draw_rectagle(w, h, fill):
#     for i in range(w):
#         for j in range(h):
#             print(fill, end="")
#
#     return None


# draw_rectagle(7, 5, "*")

# my_args = 7, 5, "*"
# my_args = [7, 5, "*"]
# my_args = (7, 5, "*")
# my_args = "7 5 *"

# draw_rectagle(*my_args)


# def my_add(num_1, num_2):
#     return num_1 + num_2
#
#
# def my_mul(num_1, num_2):
#     return num_1 * num_2
#
#
# # adding_numbers = my_add
#
# # drukuy = print
#
# calc_list = [my_add, my_mul]
#
# for my_func in calc_list:
#     print(my_func(2, 3))


# def my_add(num_1):
#     return num_1 + 2
#
#
# def my_mul(num_1):
#     return num_1 * 2
#
#
# def my_calc(num_list, func):
#     """
#     This func is doing something
#     IMPORTANT:  func has only one arg
#     """
#
#     for num in num_list:
#         print(func(num))
#
#
# # print(str.__doc__)
#
#
# my_calc([1, 2, 3, 4], my_mul)


# choice = 0
#
# if choice == 1:
#     def my_func(n):
#         if n > 0:
#             return True
#         else:
#             return False
# else:
#     def my_func(n):
#         if n < 0:
#             return True
#         else:
#             return False
#
#
# print(my_func(100))

# def my_func(n):
#     if n < 0:
#         return True
#     else:
#         return False
#


#
# print(my_func(100))


# from lesson_8 import my_func
#
# print(my_func())
# def my_func():
#     return 10


# if __name__ == "__main__":
#     print(my_func.__doc__)
#     print(my_func.__name__)
#     print(my_func.__module__)



# Рекурсія


# def fibo(n):
#     a = 0
#     b = 1
#
#     for i in range(2, n + 1):
#         a, b = b, a + b
#
#     return b

# 0, 1, 1, 2, ...

# def fibo(n):
#     print(n)
#     if n in (1, 2):
#         return 1
#
#     return fibo(n - 1) + fibo(n - 2)
#
#
# print(fibo(10))


# def my_filter(seq, predicate):
#     result = []
#
#     for el in seq:
#         if predicate(el):
#             result.append(el)
#
#     return result


# def greater_than_zero(x):
#     return x > 0


# sequence = [0, 9, 8, -4, 2]
#
# greater_than_zero = lambda x: x > 0

# print(my_filter(sequence, greater_than_zero))
# print(my_filter(sequence, lambda x: x > 0))
# print(my_filter(sequence, greater_than_zero))



########### map(), filter(), zip() ##################

# map()


# sequence = "1234"

# def to_int(func, seq):
#     result = []
#     for i in seq:
#         result.append(func(i))
#
#     return result


# new_seq = map(int, sequence)
# print(new_seq)
# print(list(new_seq))
# print(tuple(new_seq))



# sequence = [0, 9, 8, -4, 2]
#
# new_seq = map(lambda x: x ** 2, sequence)
#
# print(list(new_seq))


# filter()

# sequence = [0, 9, 8, -4, 2]
#
# # greater_than_zero = lambda x: x > 0
# # filter_nums = filter(None, sequence)
# filter_nums = filter(lambda x: x > 0, sequence)
#
# print(list(filter_nums))


# zip()

# sequence_3 = [0, 9, 8, -4, 2]
# sequence_2 = ["apple", "red", "gold", "good"]
# sequence_1 = [True, False, None]
#
# for element in zip(sequence_1, sequence_2, sequence_3):
#     print(element)






