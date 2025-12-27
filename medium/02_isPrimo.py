'''
#TODO:
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */
'''
#Numero primo es divisible entre 1 y el mismo numero

def esPrimo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(esPrimo(5)) #True

#TODO: LISTA DE PRIMOS HASTA N

def primosHasta(n):
    primos = [] # Creamos una lista para almacenar los primos

    for num in range(2, n+1): #Iteramos desde 2 hasta n+1
        es_primo = True #variable bool
        for i in range(2, int(num**0.5) + 1): #Iteramos desde 2 hasta raiz cuadrada + 1
            if num % i == 0: #Si el numero dividido entre i, el residuo es 0 --> no es primo
                es_primo = False
                break
        if es_primo:
            primos.append(num) #Por cada vez que sea primo, agregamos a la lista
    return primos #Termina todo y muestra la lista

print(primosHasta(100))


#*COMPLETADO