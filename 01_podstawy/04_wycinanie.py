# -*- coding: utf-8 -*-

name = 'Python'

# %% wycinanie pojedynczych elementów
# print(name[0])
print(name[-2])

# %%
name[1:4] # name[start:stop]
name[:4]  # name [:stop]
name[2:]  # name [start:]
name[:]   # cały string

# %%
name[-3:]
name[-3:-1]

# %%
full = 'Python Programing'
print(full[7:])
print(full[::2]) # name [start:stop:step]

# %%
sample = '#stop#this#flow'
print(sample[::5]) # name [start:stop:step]

# %%
numbers = '8,9,7,4'
print(numbers[::2])

# %%
print(numbers[::-1]) # wycinanie od końca

# %%
name = 'kajak'
print(name[::-2])

# %% operator in testuje czy dany podciąg jest w naszym ciągu(zwraca wartosc logiczną)
name = 'Python'

'Py' in name
'java' in name

