
# def add_one(some_list):
#     # all_nums = ''
#     # for number in some_list:
#     #     all_nums += str(number)
#
#     all_nums = ''.join(str(number) for number in some_list)
#
#     added_1_int = int(all_nums) + 1
#
#     # result = []
#     # for i in str(added_1_int):
#     #     result.append(int(i))
#
#     # result = [int(i) for i in str(added_1_int)]
#     # return result
#
#     return [int(i) for i in str(added_1_int)]
#
#
# assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
# assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
# assert add_one([0]) == [1], 'Test3'
# assert add_one([9]) == [1, 0], 'Test4'
# print("ОК")












import string
# def is_palindrome(text):
#     temp =  ''.join(filter(str.isalpha and str.isalnum, text)).lower()
#     return temp == temp[::-1]

# def is_palindrome(text):
#     clean_text = []
#
#     # test = clean_text.lower().split()
#
#     for char in text:
#         if char.isalnum():
#             clean_text.append(char.lower())
#
#     clean_text = ''.join(clean_text)
#     reversed_text = clean_text[::-1]
#
#     return clean_text == reversed_text


# assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
# assert is_palindrome('0P') == False, 'Test2'
# assert is_palindrome('a.') == True, 'Test3'
# assert is_palindrome('aurora') == False, 'Test4'
#
# print("ОК")






# def find_unique_value(some_list):
#
#     for value in set(some_list):
#         # unique_value = some_list.count(value)
#         # if unique_value == 1:
#         if some_list.count(value) == 1:
#             return value
#
#
# assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
# assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
# assert find_unique_value([5, 5, 5, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5]) == 0.5, 'Test3'
# print("ОК")



# Generator

# import sys
#
#
# gen = range(1, 5)
#
# print(gen)
# # print(list(gen))
#
# print(sys.getsizeof(gen))



# def add_one(num):
#     return num + 1
#
# def count(start, func):
#     while True:
#         yield start
#         start = func(start)
#
#
# counter = count(0, add_one)
# counter_2 = count(0, add_one)
#
# print(counter)
#
# print(next(counter))
#
# print(next(counter))
#
# print(next(counter_2))
#
# print(next(counter))


# def some_gen():
#     yield 42
#
# gen = some_gen()
# print(list(gen))
# print(list(gen))
# print(next(gen))
# print(next(gen))

# def s_gen():
#     x = 1
#     while x > 0:
#         x = yield 45
#         print(f"Receiving {x}")
#         if x is None:
#             x = 0
#
#
# new_val = s_gen()
# print(next(new_val))
# new_val.send(90)
# print(next(new_val))



# value_list = [i * 2 for i in range(5)]
# print(value_list)

# value_list = (i * 2 for i in range(5))
# print(value_list)
# print(next(value_list))
# print(next(value_list))
# print(next(value_list))
# print(next(value_list))
# print(next(value_list))
# print(next(value_list))




# Gen Speed

import time

# a = []
# start = time.time()
# for i in range(10_000_000):
#     a.append(i**2)
# end = time.time()
# print("for cicle t = ", end-start, " s")
#
# start = time.time()
# b = [i**2 for i in range(10_000_000)]
# end = time.time()
# print("for generator list t = ", end-start, " s")
# #
# start = time.time()
# c = (i**2 for i in range(10_000_000))
# end = time.time()
# print("for generator t = ", end-start, " s")
#
# start = time.time()
# c = list(c)
# end = time.time()
# print("for generator to list t = ", end-start, " s")







# Замикання (closures)

# def add(q, w):
#     return q + w
#
# a = add # Створення синоніму функції
# print(a(2, 3))





# # """Область видимості параметра n належить до зовнішньої (охоплюючій) функції, проте
# # вкладена функція може використовувати його. (LEGB)"""
# #
# def calculate_pow(n): # охоплююча функція
#
#     def calculate(number): # Вкладена функція
#         print(locals())
#
#         return number ** n # змінна з охоплюючої функції
#
#     return calculate # Возврат вложенной функции
#
# f = calculate_pow(3) # Виклик охоплюючої функції
# f_2 = calculate_pow(2) # Виклик охоплюючої функції
#
# print(f) # покажчик на вкладену функцію
# number_one = f(2) # Виклик вкладеної функції
# number_two = f_2(5)
# print(number_one)
# print(number_two)









# LEGB

# Використання модифікатора nonlocal


# def fibonacci():
#     first_number = 0
#     second_number = 1
#     def get_next():
#
#         nonlocal second_number #оголошуємо змінну не локальною
#         nonlocal first_number
#
#         next_number = second_number + first_number
#         first_number = second_number
#         second_number = next_number
#         return next_number
#     return get_next


















# Decorators

# my_function = []
#
# def add_function(func):
#     """
#     Функція приймає на вхід будь-який об'єкт (функцію), додає його до
#     списку my_function і повертає цей об'єкт.
#      """
#     my_function.append(func)
#     return func
#
# @add_function # Застосування створеної функції як декоратор
# def summ(x, y): # Декорована функція
#     return x + y
#
# @add_function
# def mul(x, y): # Декорована функція
#     return x * y
#
# print(my_function) # Список функцій, які ми задекорували
# print(mul(4, 5)) # функція працює так, як і було задумано
#
# # # Створимо ще одну функцію і застосуємо до неї декоратор
# def div(q, w):
#     return q / w
#
# div = add_function(div)
#
# # @add_function
# # def div(q, w):
# #     return q / w
#
# print(my_function)

# print(div(5, 6))






# Передача параметрів для функції, що декорується.


# def to_str(func):
#     #конструкція *args, **kwargs дозволяє приймати будь-які аргументи (позиційні та/або іменовані) та в будь-якій кількості
#     def get_str(*args, **kwargs): # Функція, яка приймає аргументи для функції, що декорується
#         """from any type to string"""
#         return str(func(*args, **kwargs))
#
#     return get_str # Як результат повертається інша функція
#
#
# @to_str
# def suma(x, y):
#     return x + y
#
#
# # print("Summa = " + suma(3, 4)) #хоча функція suma повертає число, але тут помилка не виникне
# print(suma(3, 4), type(suma(3, 4))) #хоча функція suma повертає число, але тут помилка не виникне
#
# # suma = to_str(suma)
# # suma = get_str(*args, **kwargs) -> str(func(*args, **kwargs))
#
# print(suma) # бачимо вказівник на функцію get_str





# def trace(func):
#     """Декоратор trace виводить на екран повідомлення з
#          інформацією про виклик функції, що декорується"""
#     def inner(*args, **kwargs):
#         """Inner doc"""
#         print(f'name: {func.__name__}, args: {args}, kwargs: {kwargs}')
#         return func(*args, **kwargs)
#     return inner
#
#
# @trace # identity = trace(identity)
# def identity(x):
#     """I do nothing useful."""
#     return x


# print(identity(50))

# print(identity) # вказівник на функцію inner
# help(identity) # Help on function inner
#
# print(identity.__name__, identity.__doc__) ##інформація з оригінальної функції









# # встановимо "правильні" значення в атрибути функції, що декорується:
# def trace(func):
#     """Декоратор trace виводить на екран повідомлення з
#          інформацією про виклик функції, що декорується"""
#     def inner(*args, **kwargs):
#         """Inner doc"""
#         print(f'name: {func.__name__}, args: {args}, kwargs: {kwargs}')
#         return func(*args, **kwargs)
#     # Встановлюємо для функції inner значення, які були у декорованої функції
#     inner.__module__ = func.__module__
#     inner.__name__ = func.__name__
#     inner.__doc__ = func.__doc__
#     return inner
#
# @trace
# def identity(x):
#     """I do nothing useful."""
#     return x
#
# print(identity.__name__, identity.__doc__) ##інформація з оригінальної функції



















import functools
#
# def trace(func):
#     """Декоратор trace виводить на екран повідомлення з
#          інформацією про виклик функції, що декорується"""
#     def inner(*args, **kwargs):
#         """Inner doc"""
#         print(f'name: {func.__name__}, args: {args}, kwargs: {kwargs}')
#         return func(*args, **kwargs)
#     functools.update_wrapper(inner, func)
#     return inner
#
# @trace
# def identity(x):
#     """I do nothing useful."""
#     return x
#
# print(identity.__name__, identity.__doc__)










# same with @wraps

# def trace(func):
#     """Декоратор trace виводить на екран повідомлення з
#          інформацією про виклик функції, що декорується"""
#
#     @functools.wraps(func)
#     def inner(*args, **kwargs):
#         """Inner doc"""
#         print(f'name: {func.__name__}, args: {args}, kwargs: {kwargs}')
#         return func(*args, **kwargs)
#     return inner
#
#
# @trace
# def identity(x):
#     """I do nothing useful."""
#     return x
#
#
# print(identity.__name__, identity.__doc__)
# print(identity(34))


