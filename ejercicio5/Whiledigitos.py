"""Ejercicio 5:
Programa que dado un número determina cuántos dígitos tiene."""

print("-----------------------------------------")
print("---------- CANTIDAD DE DÍGITOS ----------")
print("-----------------------------------------")

# input 
N=int(input("Digite el valor de N: "))
C=0

#processing
while N>0:
    N=N//10
    C=C+1
    
print("La cantidad de dígitos es:",C)


