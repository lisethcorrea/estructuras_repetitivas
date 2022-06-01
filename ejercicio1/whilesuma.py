"""Ejercicio 1:
Programa para calcular la suma de los N primeros números naturales."""

print("--------------------------------------")
print("---------SUMATORIA DE NUMEROS --------")
print("--------------------------------------")

suma=0
j=1

print("Dame el valor de N.\n")

# input

n=int(input("."))

#processing

while (j<=n):
    suma=suma+j
    j=j+1
    
    
    
#output

print ("La sumatoria total es: " + str (suma))

#FIN

