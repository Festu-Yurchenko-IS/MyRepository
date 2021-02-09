hello = "Hello, World!"
print(type(hello))  # str
print("x=" + str(hello))
x = 1 + 2 + 3 + 4
print(type(x))  # int
print("x=" + str(x))
y = 6
print(type(y))  # int
print("y=" + str(y))
x, y = y, x
print(type(x))  # int
print(f"x={x}")
print(type(y))  # int
print(f"y={y}")
print("2**3**2=" + str(2**3**2))
print("2**9=" + str(2**9))
print(f"8**2={8**2}")
print(f"16/3={16/3}")
print(f"16//3={16//3}")
print(f"16%3={16%3}")
print()

x = ['1', 'rer', 1]
print(f'{x}\n{type(x[0])}\n{type(x[1])}\n{type(x[2])}')
del x[1]
print(x)
y = x.pop()
print(y)
x.append(y)
del y
print(x)
x.insert(0, 'new')
print(x)
x.remove('1')
print(x)

y = x.pop(0)
print(x)
del y

x.append(5)
x.append(-2)
x.append(4)
# x.append(0.1)

print(f'дополняем x: {x}')
print(f'sorted(x): {sorted(x)}')
print(f'x: {x}')
x.sort()
print(f'x.sort: {x}')
print(f'x: {x}')
print(f'list(reversed(x)): {list(reversed(x))}')
print(f'x: {x}')
x.reverse()
print(f'x.reverse: {x}')
print(f'x: {x}')
print(f'len(x): {len(x)}')
print(f'x[-2]: {x[-2]}')

for elem in x:
    print(f'elem: {elem}')

y = 'hello'
print(f'y: {y}')
print(f'y.upper(): {y.upper()}')
print(f'y.lower(): {y.lower()}')
print(f'y.title(): {y.title()}')
print(f'y.title(): {y.title()}\n')

t = []
for value in range(1, 10, 3):
    print(value)
    t.append(value)
print(f't: {t}\n')

b = [value**2 for value in range(1, 11)]
print(f'b = [value**2 for value in range(1, 11)]: {b}')
print(f'b[2:4]: {b[2:4]}')
print(f'b[2:4]: {b[-5:]}')
a = b[:]
print(f'a = b[:], a: {a}')
a[1] = 99
print(f'a[1]=99, a: {a}, b: {b} => срез создаёт список и заполняет значениями')

print()
a = (3, 5)
print(f'Кортеж - неизменяемый список a=(3, 5): {a}')


if len(a) > 2:
    print(f'длина списка а>2: {a}')
elif len(a) == 2:
    print(f'длина списка а=2: {a}')
else:
    print(f'длина списка a<2: {a}')

print(f'2!=3: {2!=3}')
print(f'2 in range(1,5): {2 in range(1,5)}')
print(f'"k" not in ["m","o","p"]: {"k" not in ["m","o","p"]}')

a = {"black": "#000000", "white": "#ffffff"}
print(f'a={{"black":"000000","white":"ffffff"}}, a["black"]=: {a["black"]}')

a["red"] = "#ff0000"
print(f'a["red"] = "#ff0000": a["red"] = {a["red"]}')

print(f'"red" in a: {"red" in a}')
del a["red"]
print(f'del a["red"]\t "red" in a: \
    {"red" in a}')

print()
for key, value in a.items():
    print(f'key: {key}, value: {value}')

z = [1, 2, 3, 4, 2, 5, 2, 6, 2, 7]
print(f'\n{z}\nудаление двоек из списка с помощью цикла')
while 2 in z:
    z.remove(2)
print(z)

responses = {}
while False:
    key = input(f'Введите ключ:')
    value = input(f'Введите значение:')
    responses[key] = value
    inp = input('Продолжить ввод? [введите no или q для остановки]: ').lower()
    if inp == 'no' or inp == 'q':
        break

print(responses)


def greet_user(username="user",):
    """Выводит простое приветствие"""
    print(f"Hello, {username.title()}!")


greet_user('Andrey')
greet_user()
greet_user(username='Android')


def formatted_name(first_name, second_name, last_name, middle_name='', *other):
    """Возвращает отформатированное представление ФИО"""
    if middle_name == '':
        full_name = last_name + ' ' + first_name + ' ' + second_name
    else:
        full_name = last_name + ' ' + first_name + ' '  \
            + middle_name + ' ' + second_name
    for string in other:
        full_name += ' ' + string.title()
    return full_name.title()


print(formatted_name('андрей', "СЕРГЕЕВИЧ", 'Юрченко'))
print(formatted_name('андрей', "СЕРГЕЕВИЧ", 'Юрченко', 'де'))
print(formatted_name('андрей', "СЕРГЕЕВИЧ", 'Юрченко', 'де', 'ла', "фирэ"))

y = x = 4
print(f'y = x = 4\nx == y: {x == y}, x is y: {x is y}')
del x
print(y)
print()

a, b, *rest = 1, 2, 3, 4, 5, 6, 7
print(f'a: {a}, b: {b}, rest: {rest}')
*rest, a, b = 1, 2, 3, 4, 5, 6, 7
print(f'rest: {rest}, a: {a}, b: {b}')
print('*rest: ', end='')
print(*rest)
print('*rest: ', end='')
print(*rest, sep="\t", end=".\n")


def hello_n(name: str,
            n: int):
    '''Печатает имя (name) указанное количество (n) раз'''
    for i in range(n):
        print(name, ', привет!')


hello_n('Вася', 5)
v = 'Женя', 3
hello_n(*v)

a = range(1, 100, 2)
print(a, end="\t")
print(type(a))
print(*a)
print(dir(a))


c = [-1, -2, -3]
print("список - последовательность ссылок на объекты")
b = [1, (2, 20), 3, 4]
print(type(b) == list)
b[0] = b
b[3] = c
print('b:', end=" ")
print(*b)
print()
print('*b:', end=" ")
print(*b)

print('\nпечать элементов массива b вручную')
for i in range(len(b)):
    print(f'b[{i}] = {b[i]}', end=", ")

print('\n\nпечать элементов массива b вручную (через enumerate)')
for i, x in enumerate(b):
    print(f'#{i}: {x}')

print('\nМножества:')
s = {1, 2, 5, 6, 2, 4, 1, 3, 5, 2, 6, 1, 5, 2, 2}
print(type(s))
print(s)
print(*s)
for el in s:
    print(el)
print('быстро обрабатывают проверки на принадлежность')

print('\nСловари:')
d = {1: 2, 5: 6, 2: 4, 1: 3, 5: 2, 6: 1}
print(type(d))
print(d)
print(*d)
for key, item in d.items():
    print(key, ':', item, ' ', end=' ', sep='')
print()
for key in d:
    print(key, ':', d[key], ' ', end=' ', sep='')
print()


# 1.py
