# -*- coding: utf-8 -*-
# ćwiczenie 1

string = 'Programowanie w języku Python - od A do Z'
string = string.lower()
string = string.replace('-', ' ')
string = string.replace(' ', '')
string = string.replace('ę', 'e')
set('programowaniewjezykupythonodadoz')

string = set('programowaniewjezykupythonodadoz')
print(len(string))

# %% albo 

string = 'Programowanie w języku Python - od A do Z'
string = string.lower()
string = string.replace('-', ' ')
string = string.replace(' ', '')
string = string.replace('ę', 'e')

unique_characters_count = len(set(string))
print(unique_characters_count)

# %% albo

string = 'Programowanie w języku Python - od A do Z'
string = string.lower().replace('ę', 'e').replace(' ', '').replace('-', '')
 
unique_characters_count = len(set(string))
print(unique_characters_count)

# %% ćwiczenie 2

set1 = set([1, 2, 3, 4, 5])
set2 = set([4, 5, 6, 7, 8])

union_set = set1.union(set2)
intersection = set1.intersection(set2)
difference = set1.difference(set2)
symmetric_difference = set1.symmetric_difference(set2)

print(f'Union set: {union_set}')
print(f'Intersection set: {intersection}')
print(f'Difference set: {difference}')
print(f'Symmetric difference set: {symmetric_difference}')

# %% ćwiczenie 3

list1 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
unique_set = set(list1)
unique_list = list(unique_set)


print('List with duplicates:', list1)
print('List without duplicates:', unique_list)

# %% ćwiczenie 4

set1 = set([1, 2, 3, 4, 5])
set2 = set([4, 5, 6, 7, 8])

union_set = set1.union(set2)
print('Union set without duplicates:', union_set)

# %% ćwiczenie 5

language = 'Python'
version = '3.10'

language_version = (language, version) 
print(language_version)

# %% ćwiczenie 6

tuple1 = (1, 2, 3)
tuple2 = ('apple', 'banana', 'cherry')
combined_tuple = tuple1 + tuple2

print('Tuple 1:', tuple1)
print('Tuple 2:', tuple2)
print('Combined tuple:', combined_tuple)

# %% ćwiczenie 7

fruits = ('apple', 'banana', 'cherry', 'banana', 'banana')
number_of_bananas = fruits.count('banana')

print('Number of bananas:', number_of_bananas)

# %% ćwiczenie 8

fruits = ('apple', 'banana', 'cherry')
fruit_1, fruit_2, fruit_3 = fruits

print('Tuple:', fruits)
print('Fruit 1:', fruit_1)
print('Fruit 2:', fruit_2)
print('Fruit 3:', fruit_3)

# %% ćwiczenie 9

numbers = [1, 4, 2, 5]
letters = ['d', 's', 't']
unionlist = numbers + letters

print(unionlist)

# %% ćwiczenie 10

fruits = [['apple', 'banana'], ['cherry', 'orange'], ['kiwi', 'melon']]

print('Nested list:', fruits)
print('First item of second nested list:', fruits[1][0]) 
# wydrukuje pierwszy element drugiej zagnieżdżonej listy.

# %% ćwiczenie 11

fruits = ['apple', 'banana', 'cherry', 'orange', 'kiwi']

print('List:', fruits)
print('Slice 1:', fruits[1:3])
print('Slice 2:', fruits[:3])
print('Slice 3:', fruits[3:])
print('Slice 4:', fruits[1:5:2])

# %% ćwiczenie 12

fruits = [
    ['apple', 'banana', 'cherry'],
    ['orange', 'kiwi', 'melon'],
    ['grape', 'pear', 'plum'],
]

print('Last item of first nested list:', fruits[0][2])
print('First two items of second nested list:', fruits[1][:2])
print('Last two items of third nested list:', fruits [2][1:])
