print("Ej1")
a = 5
b = 7

print(f"Suma entre {a} y {b} es = {a+b}")
print(f"Resta entre {a} y {b} es = {a-b}")
print(f"Multiplicacion entre {a} y {b} es = {a*b}")
print(f"Division entre {a} y {b} es = {a/b}")

print("Ej2")
cel = 9

fahrenheit = (cel * 9/5) + 32

print(f"{cel} celsius son {fahrenheit}")

km = 5

ft = km * 3281
millas = km * 0.621371
print(f"{km}km son {ft}ft y {millas} millas")

eur = 250
libra = eur * 0.847
usd = eur * 1.120
print(f"{eur}€ son {libra}GBP y {usd}$")

print("Ej3")
nota1 = 4
nota2 = 5
nota3 = 6
nota4 = 6.5

media = (nota1 + nota2 + nota3 + nota4) / 4
aprobado = media >= 5 
print(f"Nota media: {media} Has aprobado? {aprobado}")

print("Ej4")
num = 1024
esPar = num % 2 == 0
print(f"El numero {num} es par: {esPar}")

print("Ej5")
a = 1
b = 10
num = 5
enRango = a <= num <=b
print (f"El numero {num} esta entre el {a} y {b}: {enRango}")

print("Ej6")
numero = 30
print(f"El numero {numero} es multiplo de 3: {numero % 3 == 0}")
print(f"El numero {numero} es multiplo de 5: {numero % 5 == 0}")
print(f"El numero {numero} es multiplo de 7: {numero % 7 == 0}")