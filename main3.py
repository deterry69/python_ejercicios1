print('Colecciones')
print('Ej1')
lista = ['Hola', 'buenas', 'tardes']
print(lista)

print('Ej2')
lista = ['Hola', 'muy', 'buenas', 'noches']
print(lista)
lista[1] = 'amigo'
print(lista)

print('Ej3')
nums = [5, 10, 15]
suma = nums[0] + nums[1] + nums[2]
print(suma)

print('Ej4')
nums = [5, 10, 15]
media = nums[0] + nums[1] + nums[2] / 3
print(media)

print('Ej5')
lista = ['Francia', 'España', 'Inglaterra']
print(max(lista, key=len))

print("Ej6")
lista = ['Naruto', 'Sasuke', 'Sakura', 'Kakashi', 'Itachi']
palabra = input('Introduce palabra: ')
print(palabra in lista)

print("Ej7")
matriz = [[1, 2], [3, 4]]
print(matriz[0][0], matriz[0][1], matriz[1][0], matriz[1][1])

print("Ej8")
matriz = [[1, 2, 3], [4, 5, 6]]
print(matriz[0][0] + matriz[0][1] + matriz[0][2] + matriz[1][0] + matriz[1][1] + matriz[1][2] / 6)

print("Ej9")
lista = ["Shikamaru", "Kiba", "Hinata", "Ino", "Choji"]
print(lista[0], lista[4], len(lista))

print("Ej10")
lista = [4, 3, 5, 8, 3]
if sum(lista) / len(lista) >= 5:
    print('Aprobado')
else:
    print('Suspenso')

print("Ej11")
lista = ['Azul', 'Rojo', 'Amarillo', 'Verde', 'Morado']
palabra = input('Introduce palabra: ')
print(palabra in lista)

print("Ej12")
miset = {'29a', '50b', '12c', '46d', '12c'}
print(len(miset))
print('29a' in miset)

print("Ej13")
miset = {'Tanjiro', 'Nezuko', 'Inosuke', 'Zenitsu', 'Tomioka'}
nombre = input('Introduce nombre:')
if nombre in miset:
    print('Ya existe')
else:
    miset.add(nombre)
    print(miset)

print("Ej14")
miset = {1, 2, 3}
miset2 = {4, 5, 6}
if len(miset) > len(miset2):
    print('set1 es mayor')
elif len(miset2) > len(miset):
    print('set2 es mayor')
else:
    print('son iguales')

print("Ej15")
diccionario = {'Brock': 18, 'Misty': 16, 'Surge': 25, 'Erika': 17, 'Sabrina': 17}
nombre = input('Introduce nombre: ')
if nombre in diccionario:
    print('Edad:', diccionario[nombre])
    print('Mayor de edad:', diccionario[nombre] >= 18)

print("Ej16")
diccionario = {'Pepe': 5, 'Ana': 4, 'Marta': 7, 'Guillermo': 8, 'Manolo': 4}
nombre = input('Introduce nombre: ')
if nombre in diccionario:
    print('Nota:', diccionario[nombre])
    print('Aprobado:', diccionario[nombre] >= 5)

print("Ej17")
diccionario = {'Cyndaquil': 1234, 'Totodile': 5678, 'Chikorita': 9101, 'Hoothoot': 1123, 'Ledyba': 1314}
nombre = input('Introduce nombre: ')
contrasena = input('Introduce la contraseña: ')
if nombre in diccionario and int(contrasena) == diccionario[nombre]:
    print('Login correcto')
else:
    print('Login incorrecto')


