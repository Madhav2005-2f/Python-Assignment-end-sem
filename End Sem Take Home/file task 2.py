filename = 'yourfile.txt'

with open(filename, 'r') as file:
    content = file.read()

number = ''
numbers = []

for char in content:
    if char.isdigit():
        number += char
    else:
        if number:
            numbers.append(number)
            number = ''

if number:
    numbers.append(number)


for num in numbers:
    print(num)
