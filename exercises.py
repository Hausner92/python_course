# -*- coding: utf-8 -*-

# ćwiczenie 1

sentence = 'I love Python!'
print(sentence)

# %% ćwiczenie 2

name = 'Python'
print('Cześć,', name)

# %% ćwiczenie 3

name = 'John'
age = 25
height = 180.5

print(f'My name is {name} and I\'m {age} years old.'
      f'\nMy height is {height} cm.')

# %% albo z dwoma printami

print(f'My name is {name} and I\'m {age} years old.')
print(f'My height is {height} cm.')

# %% ćwiczenie 4

name = 'Alice'
age = 30
height = 165.5

print(f'{name}|{age}|{height}')

# %% albo

print(name, age, height, sep='|')

# %% ćwiczenie 5

initial_amount = 1000
interest_rate = 5
duration = 2
wartosc_koncowa = initial_amount * (1 + interest_rate / 100) ** duration

print(wartosc_koncowa)

# %% ćwiczenie 6

result = (5 + 3) * 2 / 4
print(f'The result is {result}.')

# %% ćwiczenie 6

radius = 5
pi = 3.14159
circumference = 2 * pi * radius
print(f'The circumference of the circle is {circumference}.')
