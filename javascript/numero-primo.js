/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */

//NUMERO PRIMO --> ES DIVISIBLE ENTRE 1 Y MISMO NUMERO

function esPrimo(num) {
  //COMPROBAR QUE EL NUMERO 2 ES EL UNICO PAR PRIMO
  if (num <= 1) return false;
  if (num === 2) return true;
  if (num % 2 === 0) return false;

  const limite = Math.sqrt(num); //RAIZ DEL NUMERO

  for (let i = 3; i < limite; i += 2) {
    if (num % i === 0) return false;
  }

  return true;
}

console.log("============= Numeros primos entre 1 y 100 =============");

const primos = [];

for (let i = 1; i <= 100; i++) {
  if (esPrimo(i)) {
    primos.push(i); //AGREGAR ELEMENTO AL ARRAY
  }
}

console.log(primos);
