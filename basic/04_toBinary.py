'''
#TODO:
/*
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
*/
'''

#Crear una funcion que reciba un numero decimal como parametro, lo que hara sera transformarlo a binario 0 y 1.Sin funciones del lenguaje.

# ? Dividir / 2 el decimal repetidamente
# ? Guardar el resto 0 o 1
# ? Cociente nuevo numero y repetir hasta que sea 0

def toBinary(num):
    if num == 0:
        return "0"
    
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2
    
    return binary

print(toBinary(23)) #10111
print(toBinary(77)) #1001101
print(toBinary(92)) #1011100

