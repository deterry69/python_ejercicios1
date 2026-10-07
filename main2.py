import math

print("Ej 1 y 2")
def greet():
    print("Hello world")

def greet(name = "world"):
    print(f"Hello {name}")

greet()
greet("Daniel")
greet("Brandom")

print("Ej3")
def pow(a, b):
    return a ** b
a = 2
b = 3
resultado = pow(a, b)
print(resultado)

print("Ej4")
def celsius_to_fahrenheit(temperature):
    return (cel * 9 / 5) + 32
cel = 5
resultado = celsius_to_fahrenheit(cel)
print(resultado)

print("Ej5")
def area_circle(radius):
    return math.pi * (radius ** 2)
radius = 5
resultado = math.pi * (radius ** 2)
print(resultado)

print("Ej6")
def avg(a, b, c):
    return (a + b + c) / 3
a = 2
b = 3
c = 4
resultado = (a + b + c) / 3
print(resultado);

print("Ej7")
def concat(a, b, c):
    return f"{a} {b} {c} "
resultado = concat("Hola", "buenas", "tardes")
print(resultado)

print("Ej8")
def full_name(name, surname1, surname2):
    return f"{name} {surname1} {surname2}"
resultado = full_name("Alfonso", "de Terry", "Perez")
print(resultado)

print("Ej9")
def current_age(birth_year):
    return 2026 - birth_year
birth_year = 2006
resultado = 2026 - birth_year
print(resultado)

print("Ej10")
def introduccion(name, surname1, surname2, birth_year):
    nombre_completo = full_name(name, surname1, surname2)
    edad = current_age(birth_year)
    print(f"Hola soy {nombre_completo} y tengo {edad} años")
introduccion("Alfonso", "de Terry", "Perez", 2006)

print("Ej 11 y 12")
def welcome(name):
    print(f"Hello {name}, welcome to this Python lesson")
welcome("Alfonso")

print("Ej13")
def double(number):
    return number * 2
number = 9
resultado = number * 2
print(resultado)

print("Ej14")
def price_with_tax(price):
    return price * 1.21
price = 50
resultado = price * 1.21
print(resultado)

print("Ej15")
def precio_with_tax(price, tax):
    return price + (price * (tax / 100))
total = precio_with_tax(50, 21)
print(resultado)

print("Ej16")
def volume_cube(side):
    return side ** 3
side = 5
resultado = side ** 3
print(resultado)

print("Ej17")
def time_to_seconds(hours, minutes, seconds):
    return (hours * 3600) + (minutes * 60) + seconds
total = time_to_seconds(1, 60, 3600)
print(total)

print("Ej18")
def pretty_text(text):
    return "=== {text} ==="
text = "Que tal?"
print(f"=== {text} ===")

print("Ej19")
def format_name(name, surnames):
    return surnames, name
surnames = "de Terry Perez"
name = "Alfonso"
print(surnames, name)

print("Ej20")
def passed(grade1, grade2, grade3):
    return (grade1 + grade2 + grade3) / 3
grade1 = 5
grade2 = 5.5
grade3 = 3.5
total = (grade1 + grade2 + grade3) / 3
aprobado = total >=5
print(total, aprobado)

print("Ej21")
def student_passed(name, surnames, grade1, grade2, grade3):
    nombre_formateado = format_name(name, surnames)
    aprobado = passed(grade1, grade2, grade3)
    print(nombre_formateado, aprobado)
student_passed("Alfonso", "de Terry Perez", 9, 8, 10)   