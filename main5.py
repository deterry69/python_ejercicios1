import random

print('While')

print('Ej1')
i = 1
while i <= 10:
    print(i)
    i = i + 1

print('Ej2')
i = 10
while i >= 1:
    print(i)
    i = i - 1

print('For')

print('Ej1')
for numero in range(1, 11):
    print(numero)

print('Ej2')
for numero in range(10, 0, -1):
    print(numero)

print('Ej3')
acc = 0
for numero in range(1, 11):
    acc += numero
    print(acc)

print('Ej4')
for numero in range(1, 21, 2):
    print(numero)

print('Ej5')


print('Ej6')
for numero in range(1, 11):
    print(f'7 * {numero} = {numero * 7}')

print('Ej7')
for numero in range(1,51):
    if numero % 2 == 0:
        print(numero)

print('Ej8')
for numero in range(6):
    print(random.randint(1, 6))

print('Ej9')
list = ['texto1', 'texto2', 'texto3', 'texto4', 'texto5']
for i in list:
    print(i)

print('Ej10')
list = [2, 4, 6, 8, 10]
acc = 0
for i in list:
    acc += i
print(acc)

print('Ej11')
list = [2.5, 6.4, 9.4, 4.5, 5.0]
acc = 0
for i in list:
    acc += i
print(acc / len(list))

print('Ej12')
list = [2, 4, 7, 8, 10]

even = 0
odd = 0
for i in list:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'even: {even} y odd: {odd}')

print('Ej13')
list = ['Paco', 'Mateo', 'Marta', 'Daniel', 'Antonio']

name = input('Introduce un nombre: ')
found = False
for names in list:
    if names == name:
        found = True
print('Existe') if found == True else print('No existe')

print('Ej14')
list['Pokemon', 'Naruto', 'Attack on Titan', 'Guardianes de la noche', 'HunterXHunter']

for i in range(0, len(list)) : 
    print(f'Cadena {i} : {list(i)}')

print('Ej15')
list['Pokemon', 'Naruto', 'Attack on Titan', 'Guardianes de la noche', 'HunterXHunter']

for i in set:
    if len(i) >= acc:
        acc = len(i)
        result = i
print(result)

print('Ej16')
lista = {
    'Paco': 4.9,
    'Antonio': 7.2,
    'Manolo': 3.4,
    'Daniel': 4.9,
    'Pablo': 6.7
}

max = 0
min = 10
namemin = ''
namemax = ''
for i in lista:
    if lista[i] >= max:
        max = lista[i]
        namemax = i

    if lista[i] <= min:
        min = lista[i]
        namemin = i
print(f'{namemin} : {min}')
print(f'{namemax} : {max}')
print(sum(lista.values()) / len(lista))

print('Ej17')

dict = {
    'Iphone 18': 1600,
    '5090': 3000,
    'Motorola 3': 4,
    'Pase de batalla': 9,
    'Ocarina of Time': 70
}

for i in dict:
    print(f'{i} : {dict[i] * 1.21}€')

    print('Ej18')

dict = {
    'Julian': 2001,
    'Manuel': 2015,
    'Daniel': 1993,
    'Roberto': 2000,
    'Alfonso': 2006
}

acc_adult = 0
acc_underage = 0
    
for name in dict:
    if 2026 - dict[name] >= 18:
        acc_adult += 1
    else:
        acc_underage += 1
print(f'Adultos: {acc_adult}')
print(f'Undereage: {acc_underage}')