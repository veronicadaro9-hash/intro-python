a = 10
b = 5

print(a<b)#False menor que
print(a>b)#True mayor que
print(a!=b)#True distinto que
print(a==b)#False igual que
#condicional, es una estructura la
#cual ingresa al bloque de codigo muestra su condición sea verdadera
if a > b:
    print("'a' es mayor que 'b")

"""
if a > b:
    print("'a' es mayor que 'b")
else:
    print("a es menor o igual a b")
"""

"""
dia = "Viernes"

if dia == "Martes":
    print("es Martes")
elif dia == "Miércoles":
    print("es Miércoles")
elif dia == "Jueves":
    print("es Jueves")
elif dia == "Viernes":
    print("es Viernes")
else:
    print("no se sabe que día")
"""

usuario = None
password = None

usuario = input("Ingrese su usuario")
password = input("Ingrese su password")

# rolando@gmail.com y rolando1234 credenciales correctas

# operadores de union and or not

if usuario == "rolando@gmail.com" and password == "rolando1234":
    print("Bienvenido al sistema")
else:
    print("Credenciales no válidas")



