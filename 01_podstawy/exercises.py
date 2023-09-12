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

# %% ćwiczenie 7

radius = 5
pi = 3.14159
circumference = 2 * pi * radius
print(f'The circumference of the circle is {circumference}.')

# %% ćwiczenie 8

text = 'Python-is-amazing'
print('First three characters:', text[:3])
print('Last two characters:', text[-2:])

# %% ćwiczenie 9

text= 'Python is amazing!'
print('Reversed text:', text[::-1])

# %% ćwiczenie 10

x = 5
print(type(x))
 
x = 'five'
print(type(x))

# %% ćwiczenie 11

text = '#'.join(['sport', 'python', 'free', 'time'])
print(text)

# albo

words = ['sport', 'python', 'free', 'time']
joined_words = '#'.join(words)
print(joined_words)

# %% ćwiczenie 12

number_string = '123,785,45,5'
print(number_string.split(','))

# albo

number_string = '123,785,45,5'
numbers = number_string.split(',')
print(numbers)

# %% ćwiczenie 13

text = ' Python '
print('Original text:', text)
print('Uppercase text:', text.upper())
print('Lowercase text:', text.lower())
print('Stripped text:', text.lstrip())
print('Replaced text:', text.replace('P', 'C'))

# albo

text = ' Python '
 
uppercase = text.upper()
lowercase = text.lower()
stripped = text.strip()
replaced = text.replace('P', 'C')
 
print('Original text:', text)
print('Uppercase text:', uppercase)
print('Lowercase text:', lowercase)
print('Stripped text:', stripped)
print('Replaced text:', replaced)

# %% ćwiczenie 14

text = 'script.py view.jpg README.md main.py'
extension = text.count('py')

print(f"The extension '.py' appears {extension} times in the text.")

# albo

text = 'script.py view.jpg README.md main.py'
char = '.py'
 
count = text.count(char)
print(f'The extension \'{char}\' appears {count} times in the text.')