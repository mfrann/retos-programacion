'''
#TODO: 
/*
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
 */
'''

# paso 1: guardar esta palabra en una lista
# paso 2: recorrer la lista y contar cada palabra
# paso 3: 

'''
EJEMPLO: 

abecedario = [a, b, e, c, e, d, a, r, i, o]

count a = 2
count b = 1
count e = 2
count c = 1
...
'''
def count_word(word):
   
    list = [] #Para guardar cada letra de la palabra
    word = word.lower() #Cada letra a minuscula

    for char in word: #Recorrer y agregar a la lista
        list.append(char)
    
    #Contar cada palabra
    conteo = {} #Guardar cada palabra al contar

    for w in list:
        if w in conteo:
            conteo[w] += 1
        else:
            conteo[w] = 1



    return list, conteo

print(count_word('AbeCedArio'))

#*COMPLETADO