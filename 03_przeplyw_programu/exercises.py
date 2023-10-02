# -*- coding: utf-8 -*-
# %% ćwiczenie 1

print(bool(' '))
print(bool(''))
print(bool('1'))
print(bool(['', '']))

# %% ćwiczenie 2

x = 3
y = 5
z = 0

print(bool(x > y and z < y))
print(bool(x > y or z < y))

# albo

result = (x > y) and (z < y)
print(result)
 
result = (x > y) or (z < y)
print(result)

# %% ćwiczenie 3

a = 5
b = 10

print(bool(a < b and b > 0))
print(bool(a == b or b != 0))
print(bool(not(a >= b)))

# albo

c = a < b and b > 0
d = a == b or b != 0
e = not (a >= b)
 
print(c)
print(d)
print(e)

# %% ćwiczenie 4

number = 10

if number > 0:
    print('The number is greater than zero.')

# %% ćwiczenie 5

number = 5

if number > 0:
    print(f'The number {number} is positive.')
elif number < 0:
    print(f'The number {number} is negative.')
elif number == 0:
    print(f'The number {number} is equal to zero.')
    
# %% ćwiczenie 6

number = 7

if number % 2 == 0:
    print('The number', number, 'is even')
else:
    print('The number', number, 'is odd.')
    
# %% ćwiczenie 7

year = 2024
# Jeśli rok jest podzielny przez 4 i nie jest podzielny przez 100, lub jest podzielny przez 400, to jest to rok przestępny.
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('The year', year, 'is a leap year.')
else:
    print('The year', year, 'is not a leap year.')

# %% ćwiczenie 8

category = 'electronics'
price = 2000

if category == 'electronics':
    if price > 1000:
        VAT = price * 0.23
    else:
        VAT = price * 0.08
elif category == 'clothing':
    VAT = price * 0.23
else:
    VAT = price * 0.21
    
print('The VAT for a product is', VAT, 'PLN.')

# %% ćwiczenie 9

velocity = 55

if velocity > 50:
    print('Slow down!')
else:
    print('Keep it up!')
    
# %% ćwiczenie 10

category = 'crime'
quantity = 5
book_price = 100

if category == 'crime':
    if quantity >= 5:
        book_price = book_price - (book_price * 0.20)
    elif quantity >= 3:
        book_price = book_price - (book_price * 0.10)
    else:
        book_price
elif category == 'fantasy':
    if quantity >= 10:
        book_price = book_price - (book_price * 0.25)
    elif quantity >= 5:
        book_price = book_price - (book_price * 0.15)
    else:
        book_price
else:
    if quantity >= 20:
        book_price = book_price - (book_price * 0.10)
    elif quantity >= 10:
        book_price = book_price - (book_price * 0.05)
    else:
            book_price

    
print('The total price after the discount is', book_price, "PLN.")

# albo

category = 'crime'
quantity = 5
book_price = 100

if category == 'crime':
    if quantity >= 5:
        discount = 0.2
    elif quantity >= 3:
        discount = 0.1
    else:
        discount = 0
elif category == 'fantasy':
    if quantity >= 10:
        discount = 0.25
    elif quantity >= 5:
        discount = 0.15
    else:
        discount = 0
else:
    if quantity >= 20:
        discount = 0.1
    elif quantity >= 10:
        discount = 0.05
    else:
        discount = 0
 
final_price = book_price * (1 - discount)
print(f'The total price after the discount is {final_price} PLN.')

# %% ćwiczenie 11

fact = 'Python is easy and enjoyable'
unique_characters = set(fact)
number_of_unique_characters = len(unique_characters)

if number_of_unique_characters < 20:
    print('There are less than 20 unique characters.')
else:
    print('The number of unique characters is greater than or equal to 20.')
    
# %% ćwiczenie 12

text = 'sfdvjklncdnskjccbnksjdnckjsdsnckjnsdkjnckjsnkjlcnqdlknwsx'

if 'q' in text:
    print('The text contains the letter "q".')
else:
    print('The text does not contain the letter "q".')
    
# %% ćwiczenie 13

height = 1.85
weight = 85

BMI = weight / (height ** 2)
print(f'The patient\'s BMI is: {BMI:.2f}') # zaokraglenie BMI do dwoch miejsc po przecinku

if BMI < 18.5:
    print('Underweight')
elif BMI >= 18.5 and BMI < 25:
    print('Normal weight')
elif BMI >= 25 and BMI < 30:
    print('Overweight')
elif BMI >= 30:
    print('Obese')

# %% ćwiczenie 14

password = 'my_password_123'

if len(password) < 8:
    print('The password is too short.')
elif not any(char.isdigit() for char in password):
    print('The password must contain at least one digit.')
elif not any(char.isupper() for char in password):
    print('The password must contain at least one uppercase letter.')
elif not any(char.islower() for char in password):
    print('The password must contain at least one lowercase letter.')
else:
    print('The password is complex enough.')
    
# %% ćwiczenie 15

for number in range(21):
    print(number)
    
# %% ćwiczenie 16

hashtags = '#weekend#good#time#'
result = ''

for char in hashtags:
    if char not in '#':
        result = result + char
    elif result:
        print(result)
        result = ''
        
# %% ćwiczenie 17

sum = 0

for number in range(11):
    sum = sum + number
    
print('The sum of numbers from 1 to 10 is:', sum)

# %% ćwiczenie 18

products = [('T-shirt', 50.00), ('Pants', 100.00), ('Shoes', 150.00)]
total_amount = 0.0

for product, price in products:
    total_amount = total_amount + price
    
print('The total order amount is:', total_amount)

# albo

products = [('T-shirt', 50.00), ('Pants', 100.00), ('Shoes', 150.00)]
 
total = 0.0
 
for product in products:
    total += product[1]
 
print('The total order amount is:', total)

# %% ćwiczenie 19

products = [('T-shirt', 50.00), ('Pants', 100.00), ('Shoes', 150.00)]
total_amount = 0.0

if len(products) > 1:
    discount = 0.1
else:
    discount = 0.0
    
for product, price in products:
    total_amount = total_amount + price

total_amount_after_discount = total_amount - (total_amount * discount)
print(
      'The total order amount after applying the discount is:', total_amount_after_discount
      )

# %% ćwiczenie 20

products = [
    ('T-shirt', 'Clothing', 50.00),
    ('Pants', 'Clothing', 100.00),
    ('Shoes', 'Footwear', 150.00)
]

for product, category, price in products:
    if category == 'Clothing':
        print(product, price)
        
# albo 

products = [
    ('T-shirt', 'Clothing', 50.00),
    ('Pants', 'Clothing', 100.00),
    ('Shoes', 'Footwear', 150.00)
]
 
category = 'Clothing'
 
for product in products:
    if product[1] == category:
        print(product[0], product[2])
        
# %% ćwiczenie 21

products = [
    ('Shoes', 'Footwear', 150.00),
    ('T-shirt', 'Clothing', 50.00),
    ('Pants', 'Clothing', 100.00),
]

category = 'Clothing'

for product in products:
    if product[1] == category:
        print(f'The first product is {product[0]}.')
        break
    
# %% ćwiczenie 22

cars = [
    {'model': 'Tesla', 'mileage': 15000, 'battery_level': 100},
    {'model': 'Nissan', 'mileage': 30000, 'battery_level': 75},
    {'model': 'BMW', 'mileage': 5000, 'battery_level': 100},
    {'model': 'Ford', 'mileage': 20000, 'battery_level': 50}
]

for car in cars:
    if car['battery_level'] == 100:
        print('The first car with a full charge is:', car['model'])
        break

# %% ćwiczenie 23

panels = [
    {'id': 1, 'output_power': 200},
    {'id': 2, 'output_power': 150},
    {'id': 3, 'output_power': 250},
    {'id': 4, 'output_power': 180},
]

minimum_power = 200

for panel in panels:
    if panel['output_power'] > minimum_power:
        print(
            f"The first panel with an output power greater than {minimum_power} is: " 
            f"{panel['id']}"
            )
        break
    
# %% ćwiczenie 24

missions = [
    {
        'name': 'Apollo 11',
        'date': '20.07.1969',
        'status': 'completed',
    },
    {
        'name': 'Mars Pathfinder',
        'date': '04.07.1997',
        'status': 'completed',
    },
    {
        'name': 'Chang\'e 4',
        'date': '03.01.2019',
        'status': 'in progress',
    },
    {
        'name': 'Cassini',
        'date': '15.10.1997',
        'status': 'completed',
    },
]

for mission in missions:
    if mission['status'] == 'in progress':
        continue
    print('Mission', mission['name'], 'took place on', mission['date'])
    
# %% ćwiczenie 25

trainings = [
    {'name': 'Basic marksmanship', 'rank': 'Private'},
    {'name': 'Infantry tactics', 'rank': 'Corporal'},
    {'name': 'Art of war', 'rank': 'Sergeant'},
    {'name': 'Heavy weapons specialist', 'rank': 'Captain'},
    {'name': 'Advanced first aid', 'rank': 'Private'},
    {'name': 'Combat engineering', 'rank': 'Corporal'},
    {'name': 'Field intelligence', 'rank': 'Sergeant'},
    {'name': 'Military law', 'rank': 'Captain'},
    {'name': 'Parachuting', 'rank': 'Private'},
    {'name': 'Amphibious assault', 'rank': 'Corporal'},
    {'name': 'Counterterrorism', 'rank': 'Sergeant'},
    {'name': 'Military diplomacy', 'rank': 'Captain'},
]

military_rank = 'Sergeant'

for training in trainings:
    if training['rank'] != military_rank:
        continue
    print('Training for rank', training['rank'], 'is:', training['name'])
        
    



    
    
    
    
        










