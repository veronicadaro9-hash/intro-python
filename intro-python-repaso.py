#comentario en una sola linea

"""
Comentarios en varias lineas
"""

#salida de infomación
print("Salida de información")

#entrada de información
nombre = input("Ingrese su nombre") #un input captura el dato ingresado por terminal y siempre lo devuelve en formato str
print( "Su nombre es "+nombre+" es un alumno")

#tipos de variables en python
#str "@dljsjwkeje545454)?"
#int 100
#float 1000.5
#bool
variable = 100.5
print(type(variable))

#sensible a mayúsculas y minúsculas
variable1 = "Carlos"
vARiable1 = "Ivan"
Variable1 = "Jose"
print(variable1)
print(vARiable1)
print(Variable1)

nombre=None

def nombrar():
    pass

#las variables de python son flexibles
nombre = "Rolando"
print(nombre)
nombre = True
print(nombre)
nombre = 100
print(nombre)

#reglas de nombres de variables
#nombres de variables y funciones van en minúsuclas
#nombresde clases con la primera letra en mayúscula
#nombre de variables de tipo constante VALOR_PI = 3.1434554
#DECLARACIÓN DE VARIABLES


#NO SE PUEDE
#Número antes de una letra en nombre de variable
#10valor = "Ana"
#espacios entre nombre de variable
#cuenta bancario = 563635262

#SE PUEDE
nombre10="María"
#snake case o camel case
cuenta_bancario_conjunta= 5353636
cuentaCorrienteCerrado = 65362636

#casting o casteo
numero1 = "100"
numero2 = 50
suma = int(numero1)+numero2
print("la suma es",suma)
#se puede hacer el casting o conversion de tipos de todas las variables
#str(aqui el valor), bool(aquie el valor), float(aquí va el valor)



