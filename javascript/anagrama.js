/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */

//DOS PALABRAS IGUALES NO SON ANAGRAMAS
//NO COMPROBAR QUE EXISTAN LAS PALABRAS
//ANAGRAMA --> FORMAR PALABRA REODERNANDO LETRAS DE OTRA PALABRA

//RECIBIR DOS PALABRAS Y RETORNAR V O F SI ES ANAGRAMA

function Anagrama(palabraUno, palabraDos) {
  //PRIMERO ORDENAR LAS PALABRAS, PASANDO A MINUSCULAS Y QUITANDO ESPACIOS
  //COMPROBAR SI SON IGUALES AL ESTAR ORDENADAS
  //IMPRIMIR V O F
  const ordenar = (str) => str.toLowerCase().split("").sort().join("");

  if (ordenar(palabraUno) === ordenar(palabraDos)) {
    return true;
  } else {
    return false;
  }
}

console.log(Anagrama("hola", "aloh")); //true
console.log(Anagrama("amor", "mora")); //true
console.log(Anagrama("casa", "saca")); //true
console.log(Anagrama("radio", "odio")); //false
