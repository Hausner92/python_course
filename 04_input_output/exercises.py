# -*- coding: utf-8 -*-

# %% ćwiczenie 1

with open ('data.txt', 'r') as file:
    for line in file:
        print(line, end='')
        
# %% ćwiczenie 2

with open('data.txt', 'r') as file:
    data = file.readlines()
    print(data)
    
# $$ ćwiczenie 3

with open('products.txt', 'r') as file:
    lines = file.readlines()
    
lines = lines[1:]

products = []
for line in lines:
    cols = line.strip().split(';')
    products.append(cols)
    
for product in products:
    print(product)
    
# %% ćwiczenie 4

products = []
 
with open('products.txt', 'r') as file:
    for line in file:
        name, price, quantity = line.strip().split(',')
        products.append({
            'name': name,
            'price': float(price),
            'quantity': int(quantity)
        })
 
for product in products:
    print(product)
    
# %% ćwiczenie 5

with open('data.txt', 'r') as file:
    data = file.read()
 
lines = data.split('\n')
total_power = 0
 
for line in lines:
    if line:
        power = float(line.split(',')[1])
        total_power += power
 
print(f'Total power generated: {total_power:.2f} MW')

# %% ćwiczenie 6

with open('data.csv', 'r') as file:
    rows = file.readlines()
 
total_energy = 0
counter = 0
for row in rows[1:]:
    values = row.strip().split(',')
    energy = float(values[2])
    total_energy += energy
    counter += 1
 
avg_energy = total_energy / counter
print(f'Average energy generated: {avg_energy:.2f} kWh')

    
    