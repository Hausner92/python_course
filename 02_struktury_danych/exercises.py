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
