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

# %% ćwiczenie 13 

fruits = ['apple', 'banana', 'cherry']
print('List:', fruits)
fruits.append('orange')
print("List with 'orange':", fruits)

# %% ćwiczenie 14

list_1 = [4, 5, 3, 3]
list_2 = [9, 7]

list_1.extend(list_2)
print(list_1)

# albo

list_1 += list_2
print(list_1)

# %% ćwiczenie 15

company_name = ['Apple', 'Microsoft', 'Samsung', 'Netflix', 'Uber']
new_companies = ['Amazon', 'Google']
company_name.extend(new_companies)

print(company_name)

# %% ćwiczenie 16

fruits = ['apple', 'banana', 'cherry', 'orange', 'kiwi']

fruits.append('melon')
print('After appending:', fruits)

fruits.pop(3)
print('After removing:', fruits)

fruits.reverse()
print('After reversing:', fruits)

fruits.sort()
print('After sorting:', fruits)

# %% ćwiczenie 17

number_square = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(number_square)

# %% ćwiczenie 18

countries_capitals = {
    'Polska': 'Warszawa',
    'Niemcy': 'Berlin',
    'Czechy': 'Praga',
}

countries_capitals['Włochy'] = 'Rzym'

stolice = list(countries_capitals.values())
stolice.sort()
print(stolice)

# albo

countries_capitals['Włochy'] = 'Rzym'
sorted_capitals = sorted(list(countries_capitals.values()))
 
print(sorted_capitals)

# %% ćwiczenie 19

fruits = {'apple': 2, 'banana': 3, 'cherry': 5, 'orange': 1}

print('Dictionary:', fruits)

fruits['kiwi'] = 4
print('After adding:', fruits)

del fruits['orange']
print('After deleting:', fruits)

print('Keys:', fruits.keys())

print('Values:', fruits.values())

# %% ćwiczenie 20

fruits = {'apple': 2, 'banana': 3}

print('Dictionary before update:', fruits)

fruits.update({'apple':4})
print('Dictionary after update:', fruits)

fruits['kiwi'] = 1
print('Dictionary after adding:', fruits)

fruits2 = {'orange':3, 'peach':2}
fruits.update(fruits2)
print('Dictionary after merging:', fruits)

# %% ćwiczenie 21

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

dict1.update(dict2)
print(dict1)

# %% ćwiczenie 22

people = {'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}

print(people.pop('Bob'))
print(people)

# %% ćwiczenie 23

people = {'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}

people.update({'Emma':20})
print(people['Emma'])
print(people)