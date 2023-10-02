# -*- coding: utf-8 -*-

# instrukcja contiune pozwala pominąć jedną wybraną iterację i przechodzi do
# następnego elementu

# %%
for i in range(10):
    if i == 6:
        print(i)

# %%
for i in range(10):
    if i == 6:
        continue
    print(i)
    
# %% wyprinotowanie wszystkich liczb nie parzysztych
for i in range(20):
    if i % 2 == 0:
        continue
    print(i)
    
# %% wyprinotowanie wszystkich liczb parzysztych
for i in range(20):
    if i % 2 == 1:
        continue
    print(i)
    
# %% iterowanie po znakach w przykladowym tekscie
sample = 'Python Course'
for char in sample:
    if char == ' ':
        continue
    print(char)
    
# %%
hashtags = '#summer#holiday#free'
result = ''
for char in hashtags:
    if char == '#':
        print(result)
        result = ''
        continue
    result = result + char
print(result)
    