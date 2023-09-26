# -*- coding: utf-8 -*-

# %% teksty w pythonie sa obiektami iterowalnymi, zwracaja pojedyncze elementy ciagu znakow
for i in 'python':
    print(i)
    
# %%
name = 'python'
index = 0

for character in name :
    print(index, character)
    index = index + 1
    
# %% funkcja range zwraca nam obiekt iterowalny 
for index in range(10):
    print(index)

# %%
for index in range(len(name)):
    print('Nr indeksu: ', index, 'Litera:', name[index])
    
# %% funkcja enumerate dzieli nasz tekst zwraca nr indexu i pierwszy element jaka taką tuple
for i in enumerate(name):
    print(i)

# %% rekomendowany sposob do iterowania po obiektach iterowalnych
for indeks, character in enumerate(name):
    print(indeks, character)
    
# %% listy są obiektami iterowalnymi
for i in [4, 5, 6, 8, 6]:
    print(i)
    
# %%
for i, value in enumerate([4, 5, 6, 8, 6]):
    print(i, value)
    
# %% funkcja range buduje nam iterator po ktorym mozemy iterowac
for i in range(10, -1, -1):
    print(i)

# %%
for i in range(10, 100, 10):
    print(i)
    
# %%
techs = 'java'
for i in range(len(techs)):
    print(i, techs[i])
    
# %%
string = 'Python Course'
for char in string:
    print (char)

# %%
string = 'Python Course'
for char in string[:6]:
    print (char)

# %%
string = 'Python Course'
for char in string[::2]:
    print (char)
    
# %% 
string = 'Python Course'
for char in string[::-1]:
    print (char)
    
# %%
hashtags = '#sport#gym#fitness'
for char in hashtags:
    print(char)

# %%
hashtags = '#sport#gym#fitness'
for char in hashtags:
    if char not in '#': # jesli 'char' nie jest rowny '#' to go wyprintuj
        print(char)

# %% funkcja zip laczy dwa elementy w tuple, mozna latwo iterowac po dwoch elementach
for char, number in zip ('abcde', '12345'):
    print(char, number)

# %% jesli mamy rozna dlugosc elementow funkcja zip nam je obetnie do dlugosci najkrotszego elementu ktory zipuje
for char, number in zip ('abcde', 'python'):
    print(char, number)
    
# %%
hashtags = '#sport#gym#fitness'

result = ''
for char in hashtags:
    if char not in '#':
        result = result + char
    else:
        print(result)
        result = ''
        
# %%
hashtags = '#sport#gym#fitness#'

result = ''
for char in hashtags:
    if char not in '#':
        result = result + char
    else:
        print(result)
        result = ''





