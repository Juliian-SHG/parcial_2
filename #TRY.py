#TRY

try:
    num1 = float (input ("Por favor, ingresa un numero:"))
    num2 = float (input("Por favor, ingresa un numero:"))

    if num2 == 0:
        raise ZeroDivisionError # Lanza el errror o provoca el error manual
    
        resultado = num1 / num2
        print(f"El resultado de esta division es: {resultado}")

except ValueError:
       print ("¡ERROR! ingresa un nuevo numero")

except ZeroDivisionError:
       print ("¡Error! No se púede dividir por cero.")
  
  
resultado = num1 / num2
print (f"el resultado es: {resultado}")
