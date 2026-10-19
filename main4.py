print("Condicionales")
print("Ej1")

grade = float(input("Introduce la nota: "))
if grade >= 9:
    print("Sobresaliente")
elif grade >= 7:
    print("Notable")
elif grade >= 5:
    print("Suficiente")
else:
    print("Insuficiente")

print("Ej2")

n1 = float(input("1er numero: "))
operacion = (input("Operación: "))
n2 = float(input("2do numero: "))

if operacion == '+':
    print(n1 + n2)
elif operacion == '-':
    print(n1 - n2)
elif operacion == '*':
    print(n1 * n2)
elif operacion == '/':
    print(n1 / n2)
else:
    print('No existe')

print('Ej3')

n1 = float(input("1er numero: "))
n2 = float(input("2do numero: "))
n3 = float(input("3er numero: "))

if n1 > n2 and n1 > n3:
    print(f'El numero mas alto e{n1}')
elif n2 > n1 and n2 > n3:
    print(f'El numero mas alto es {n2}')
elif n3 > n1 and n3 > n2:
    print(f'El numero mas alto es {n3}')
else:
    print('Son iguales')

print('Ej4')

lado1 = int(input('Lado 1:'))
lado2 = int(input('Lado 2:'))
lado3 = int(input('Lado 3:'))

if lado1 == lado2 and lado2 == lado3:
    print('Equilatero')
elif lado1 == lado2 or lado1 == lado3  or lado2 == lado3:
    print('Isosceles')
else:
    print('Escaleno')

print('Ej5')

numero = int(input('Introduce un numero: '))

if numero >= 100 and numero <= 200:
    print('Muy bien')
else:
    print('Muy mal')

print('Ej6')

num = float(input('Introduce un valor en metros: '))
ud = (input('Introduce una unidad'))

if ud == 'km':
    print(num / 100, 'km')
elif ud == 'cm':
    print(num * 100, 'cm')
elif ud == 'mm':
    print(num * 1000, 'mm')
else:
    ('No valido')

print('Ej7')

edad = int(input('Introduce edad: '))
finde = (input('Es fin de semana: ')) == 'si'

if edad < 12:
    precio = 5
elif edad >= 12 and edad <= 17:
    precio = 7
else:
    precio = 10

if finde:
    precio = precio + 2

print(f'El coste de la entrada es de {precio}€')

print('Ej8')

num = int(input('Introduce un número: '))

if num == 1:
    print('Enero')
elif num == 2:
    print('Febrero')
elif num == 3:
    print('Marzo')
elif num == 4:
    print('Abril')
elif num == 5:
    print('Mayo')
elif num == 6:
    print('Junio')
elif num == 7:
    print('Julio')
elif num == 8:
    print('Agosto')
elif num == 9:
    print('Septiembre')
elif num == 10:
    print('Octubre')
elif num == 11:
    print('Noviembre')
elif num == 12:
    print('Diciembre')
else:
    ('Numero invalido')

print('Ej9')

num = int(input('Introduce un numero: '))

if num % 3 == 0:
    print('Es multiplo de 3')
elif num % 5 == 0:
    print('Es multiplo de 5')
elif num % 7 == 0:
    print('Es multiplo de 7')
else:
    ('No es multiplo de 3, 5 ni 7')

print('Ej10')

num = int(input('Introduce un numero'))

if num < 10:
    print('Hace frio')
elif num >= 10 and num < 30:
    print('Es templada')
else:
    print('Hace calor')

    