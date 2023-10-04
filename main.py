# функциональное программирование

# ссылки на функции
# map, filter
# lambda expression


from typing import Callable


def do_operation(number1, number2,
                 operation: Callable):  # operation - Это функция которую мы будем передевать как ссылку
    result = operation(number1, number2)
    print(f'{result=}')


def plus(number1, number2):
    return number1 + number2


def minus(num1, num2):
    return num1 - num2


# do_operation(10, 10, plus)
# do_operation(10, 10, minus)


# map - Это класс, принимающий первым аргументов ссылку на функцию
# которая должна выполняться для каждого элемента внутри (списка, строки, кортежа, множества, словаря)


names = [f'name-{i}' for i in range(10)]

names_upper = [name.upper() for name in names]
print(names_upper)


def upper(element):
    return element.upper()


lst = map(upper, names)
# print(lst)
# print(list(lst))

lst2 = []

for i in names:
    print(upper(i))
    lst2.append(upper(i))

print(lst2)

test1 = ['a', 'b', 'c']
test2 = ['d', 'e', 'f']


def plus_letters(letter1, letter2):
    return letter1 + letter2


print(list(map(plus_letters, test1, test2)))

test3 = ['sdfafdsasdfaafsdf', 'asdfd', 'sdafasf', 'sadffdsadfsajkolfjasokjf', 'sadfsdaffd']

print(list(map(len, test3)))
print(list(map(str.upper, test3)))

mixed = [123, 123, '23.234', 234.234234, 'sdffds0', True, 'sfdsfd', [1, 2, 3], {}, 'FDJsdi']


def is_str(element):
    return type(element) is str
    # if type(element) is str:
    #     return True
    # return False


print(list(filter(is_str, mixed)))
print(list(map(is_str, mixed)))