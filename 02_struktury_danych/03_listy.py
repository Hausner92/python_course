# -*- coding: utf-8 -*-
# listy są obiektami które są zmienne 
# lista to uporządkowana struktura elementów, mogą być elementami zduplikowanymi
# które mogą być też zmienne 
# pusta lista

empty_list = list()
print(empty_list)

# %% listy przekazujemy jako nawiasy kwadratowe
techs = ['python', 'java', 'c++', 'go', 'sql']
techs[0] = 'python 3.7'
print(techs)

# %%
numbers = [3, 5, 3, 5, 23]
print(numbers)
print(type(numbers))

# %%
mixed = ['python', 3.7, 4, True]
print(mixed)

# %% listy możemy zagnieżdżać
empty = []
nested = [[1,2, [3, 'sql']], ['python', 'java', 'go'], 3]

# %%
first = ['mleko', 'ziemniaki', 'makaron']
second = ['woda', 'jajka']

bucket = [first, second]

# %% funkcja len pozwoli nam sprawdzić długosc listy
len(bucket)

# %% łączenie list 
techs = ['python', 'java', 'c++', 'go', 'sql']

techs += ['javascript']
print(techs)

# %% pokazanie metod do list
print(dir(list))