num1 = float(input("Escribe el primer número: "))
num2 = float(input("Escribe el segundo número: "))
num3 = float(input("Escribe el tercer número: "))

mayor = max(num1, num2, num3)

print("El número más alto es:", mayor)

## segundo ejercicio
numero = input("Escribe un número entero: ")

suma = 0
for digito in numero:
    suma += int(digito)

print("La suma de los dígitos es:", suma)
## tercer ejecircio
frase = input("Escribe una frase: ")

palabras = frase.split()

cantidad = len(palabras)

print("Número de palabras:", cantidad)
## cuarto ejercicio
numeros = list(range(10, 0, -1))  

numeros_invertidos = numeros[::-1]  

print(numeros_invertidos)

##quinto ejercicio
import random

numeros = [random.randint(1, 20) for _ in range(5)]

print("Números aleatorios:", numeros)
##sexto ejercicio
import random

numero_secreto = random.randint(1, 10)

intento = 0

print("Adivina el número del 1 al 10")

while True:
    intento = int(input("Escribe tu número: "))
    
    if intento < numero_secreto:
        print("El número es MAYOR.")
    elif intento > numero_secreto:
        print("El número es MENOR.")
    else:
        print("Adivinaste el número.")
        break
##sexto ejercicio 
multiplos_de_3 = [num for num in range(1, 31) if num % 3 == 0]
print(multiplos_de_3)


