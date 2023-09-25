# -*- coding: utf-8 -*-

# prosty program który pozwala nam się zalogować do systemu
print('Program uruchomiony...')
print(""" Włam się do systemu, zgadując dwucyfrowy pin.
      Numer pin składa się z cyfr: 0, 1, 2.""")
pin = input('Wprowadź numer pin: ')

if pin == '21':
    print('Brawo! Złamałes system.')
elif pin == '20':
    print('Byłes blisko!')
else:
    print('Nie zgadłes.')
    
# %%
print('Program uruchomiony...')
print(""" Włam się do systemu, zgadując dwucyfrowy pin.
      Numer pin składa się z cyfr: 0, 1, 2.""")
pin = int(input('Wprowadź numer pin: '))

if pin == 21:
    print('Brawo! Złamałes system.')
elif pin == 20:
    print('Byłes blisko!')
else:
    print('Nie zgadłes.')

# %%
bool('')

# %%
string = ''

if string:
    print('Niepusty ciąg znaków')
else:
    print ('Pusty ciąg znaków')
    
# %%
number = 12

if number:
    print('Liczba niezerowa!')
else:
    print('Zerrrro!!')
    
# %%
default_flag = True

if default_flag:
    print('Doszło do defaultu.')
else:
    print('Nie doszło')
    
# %%
default_flag = False

if not default_flag:
    print('Nie doszło')
else:
    print('Doszło do defaultu.')
    
# %% sprawdzenie z dwoma warunkami 
saldo = 10000
klient_zweryfikowany = True

if saldo > 0 and klient_zweryfikowany: # koniunkcja, wszystkie elementy muszą być True 
    print('Możesz wypłacić gotówkę')
else:
    print('Nie możesz wypłacić gotówki.')
    
# %%
saldo = 10000
klient_zweryfikowany = True
amount = int(input('Ile chcesz wypłacić gotówki: '))

if saldo > 0 and klient_zweryfikowany and saldo >= amount:
    print('Możesz wypłacić gotówkę')
else:
    print('Nie możesz wypłacić gotówki.'
          'Brak wystarczającej kwoty {}'.format(abs(saldo - amount))) 
    #funkcja abs zwraca nam wartosc bezwzględną czyli wartosc absolut
    
# %%
name = 'python'

if 'p' in name:
    print('Znaleziono p')
else:
    print('Nie znaleziono p')

# %%
tech = 'python'

if tech == 'python':
    flag = 'Dobry wybór'
else:
    flag = 'Poszukaj czegos lepszego'
    
# %% składnia warunków w jednej lini
# x if [warunek] else y
tech = 'python'
flag = 'Dobry wybór' if tech == 'python' else 'Poszuakj czegos lepszego'
