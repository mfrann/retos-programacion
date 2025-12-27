'''
#TODO:
/*
* Escribe una función que reciba dos palabras (String) y retorne
* verdadero o falso (Bool) según sean o no anagramas.
* - Un Anagrama consiste en formar una palabra reordenando TODAS
*   las letras de otra palabra inicial.
* - NO hace falta comprobar que ambas palabras existan.
* - Dos palabras exactamente iguales no son anagrama.
*/
'''

def isAnagrams(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

print(isAnagrams("Hola", "Aloh")) #True
print(isAnagrams("Roma", "Amor")) #True
print(isAnagrams("Mano", "Pie"))  #False

# *COMPLETADO