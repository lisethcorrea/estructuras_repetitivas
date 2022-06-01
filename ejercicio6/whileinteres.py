"""Ejercicio 6:
Programa que lea un capital C, y que averigue e imprima en cuantos meses se duplica,
si lo colocamos a un interes compuesto del 5% mensual."""

print("------------------------------------")
print("---------- INTERS MENSUAL ----------")
print("------------------------------------")

# input 
C=int(input("Digite el capital inicial: "))
D=2*C
N=0

#processing
while C<D:
     C=C+0.05*C
     N=N+1
    
    

print( "En " + str (N) + " meses tendra el doble de la capital inicial" )
