'''
/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */
'''

def callArea(shape, base, altura):
    if shape == 1 or shape == 'Triangulo':
        area = int((base * altura)/2)
    elif shape == 2 or shape == 'Cuadrado':
        base = altura
        area = base**2
    elif shape == 3 or shape == 'Rectangulo':
        area = base * altura
    else:
        print("ERROR")

    return area
print(callArea(1, 20, 34)) #TRIANGULO
print(callArea(2, 20, 34)) #CUADRADO
print(callArea(3, 20, 34)) #RECTANGULO

#*COMPLETADO