# -*- coding: utf-8 -*-
# funkcja set tworzy nam zbiór
# zbiór jest elementem nie uporządkowanym, kolejnosc w zbiorze nie jest istotna
# istotny jest to czy w danym zbiorze jest dana wartosc czy też nie
empty_set = set ()
print(empty_set)
print (type(empty_set))

# %% zbiór definijuemy po przez użycie {}
techs = {'python', 'java', 'c++', 'sql'}
print(techs)
print(type(techs))
print(len(techs)) # funkcja len zwróci nam długosc zbioru

# %% zbiór zawiera wartosci unikalne
set('python')
set('aaaaaaale')

# %% dzięki operatowi in możemy sprawdzać czy dane wartosci znajduja sie w zbiorze
'python' in techs
'go' in techs

# %% 
print(dir(set))

# %% metoda add dodaje wartosci do zbioru
techs.add('sas')

# %%
print(techs)

# %% metoda remove usuwa wskazane wartosci ze zbioru
techs.remove('sas')

# %% metoda pop wyrzuca dowolną wartosc i usuwa ją ze zbioru 
techs.pop()

# %% metoda clear czysci nasz zbiór
techs.clear()

# %%
A = {1, 2, 3, 4, 5, 6, 7}
B = {5, 6, 7, 8, 9}
C = {5, 6}

C.issubset(A) # sprawdza nam czy zbior C jest podzbiorem zbioru A
C.issubset({5, 7})
A.issuperset(C) # sprawdza nam czy A jest nadzbiorem zbioru C
A.union(B) # zwroci nam sume zbiorow
A.intersection(B) # przeciecie zwroci nam wartosci ktore sa w zbiorze A i B 
A.symmetric_difference(B) # roznica symetryczna zwraca wartosci które nie wystepują w obydwu zbiorach

D = A.copy() # kopiuje nam podany zbior i przypisuje do nowej zmiennej