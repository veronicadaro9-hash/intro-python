#realizar un programa muestre segun la opcion + (suma), -(resta), *(Multiplicacion), /(Division)
#de dos numero ingresados por teclado, nos pedira ingresar el primer numero, el segundo,
# y luego ingrese la operación, el programa debe parar solo si al final de la operación escribo la palabra salir
#usar funciones

def calculadora(num1:float,num2:float,operacion:str):

    if operacion =='+':
        print(f"La suma es:{num1+num2}") 
    elif operacion =='-':
        print(f"La resta es:{num1-num2}")
    elif operacion == '*':
        print(f"La multiplicacion es:{num1*num2}")
    elif operacion =='/':
        print(f"La division es:{num1/num2}")
    

continuar=True
while continuar:
    numero1=float( input("Ingrese el primer numero: ") )
    numero2=float( input("Ingrese el segundo numero: ") )
    operacion= input("Ingrese la operación:+,-,*,/:  ") 
    calculadora(numero1,numero2,operacion)


    #logica para parar
    seguir = input("Quieres continuar s/n")
    if seguir =='n':
        continuar=False
  