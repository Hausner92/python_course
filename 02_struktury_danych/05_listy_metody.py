# -*- coding: utf-8 -*-

techs = []
print(techs)

# %% metoda append dodaje do listy elementy
techs.append('python')
print(techs)

# %%
techs.append('java')

# %% wstawienie zagnieżdżonej listy
# metoda append wstawia nam elementy na koniec obecnej listy
techs.append(['hadoop', 'spark'])
print(techs)

# %% rozszerzy nam listę o nowe elementy i ich nie zagnieźdźi jak powyżej
techs.extend(['sql', 'sas'])
print(techs)

# %% insert pozwala nam w dowolnym miejscu wstawiać wartosci do listy
techs.insert(0, 'go')
print(techs)

# %%
techs.insert(2, 'r')
print(techs)

# %% metoda pop pozwala nam zwrócić ostatni element listy do konsoli i usuwa go z listy

print(techs)
print(techs.pop())
print(techs)

# %% metoda pop przyjmuje argumenty np. nr indexu który chcemy wyrzucić
techs = ['python', 'java', 'sql', 'php']
print(techs.pop(0))
print(techs)

# %% metoda index zwróci nam index przekazanej wartosci
techs = ['python', 'java', 'sql', 'php']

techs.index('java')
# techs.index('jav')

# %% metoda count przyjmuje wartosc elementu ktory chcemy policzyc w naszej liscie
techs = ['python', 'java', 'sql', 'php', 'python']
techs.count('python')
techs.count('jav')

# %% metoda sort pozwoli nam sortować naszą listę alfabetycznie
# parametr "reverse=True" odwróci nam kolejnosc sortowania  
techs = ['python', 'java', 'sql', 'php', 'r', 'angular']
techs.sort(reverse=True)
print(techs)

# %% metoda reverse odwróci nam kolejnosc listy
techs = ['python', 'java', 'sql', 'php', 'r', 'angular']
# techs[::-1] # przy pomocy wycinania
techs.reverse()
print(techs)

# %% dzieki metodzie wycinania mozemy zmieniac wartosci
techs[1] = 'c++'
print(techs)
