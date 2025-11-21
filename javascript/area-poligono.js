/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */

function Poligono(shape, base, altura) {
  if (shape === 1 || shape === "Triangulo") {
    area = (base * altura) / 2;
    console.log(area);
  } else if (shape === 2 || shape === "Cuadrado") {
    area = base * altura;
    console.log(area);
  } else if (shape === 3 || shape === "Rectangulo") {
    area = base * altura;
    console.log(area);
  } else {
    console.log("ERROR");
  }
  return true;
}

console.log("FUNCION PARA CALCULAR EL AREA DE UN POLIGONO");

console.log(Poligono(1, 25, 2)); //TRIANGULO
console.log(Poligono(2, 100, 100)); //CUADRADO
console.log(Poligono(3, 20, 4)); //RECTANGULO
