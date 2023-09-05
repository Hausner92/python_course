#-*- coding: utf-8 -*-

print ('Cześć, świecie')

imie = 'Jan'
print(imie)

imie = 'Jan'
wiek =30
print(imie, wiek)

print('Cześć, ', end='')
print ('świecie')

print('Cześć', 'świecie!', sep='+')

with open ('plik.txt', 'w') as f:
    print('Cześć, świecie!', file=f)

# %%    
print(2 + 2)

# %%
print(3 * 3)

# %%
print(3 + 2 * 2)
print(4 - 2 * 2)

# %%
10 / 3
4 / 2 

# %%
10 // 3
7 // 6

# %%
2 ** 5 

# %%
10 % 3
12 % 5
11 % 2

# %%
(10 - 2 ** 3) * 10

# %%
a = 10
b = 20

c = a * b 
print(c)

# %%
print('love python')
"love python"

# %%
print("It's the best!")

# %%
print('It\'s the best!')

# %%
print('Python3.7')

# %%
print('Python\n3.7')

# %%
print("""Python
3.7""")

# %%
print('\tPython')
print('\t\t\tPython')


# %%
print('C:\path\to\something\new')
print('C:\path\\to\something\\new')
print(r'C:\path\to\something\new')
print('C:\\path\\to\\something\\new')

# %%
import os
os.getcwd()

# %%
print("""
Instrukcja uruchamiania pliku przyklad.py:

    --file [nazwa pliku]
        zapisuje output do pliku
        
    --quiet
        wycisza logi w konsoli
        
Koniec.""")

# %%
text = 'I love Python. '
print(text)
print(text * 7)
print('hau...' * 8)

# %%
'Python'
'Py' 'thon'
print('Py' 'thon')

# %%
name = 'Python'
print(name + ' 3.7')
print(name, '3.7')

# %%
age = 31
imie = 'Mateusz'

print(imie + ' ' + str(age))
print(imie, age)
print('{} ma {} lat'.format(imie, age))

# %%

