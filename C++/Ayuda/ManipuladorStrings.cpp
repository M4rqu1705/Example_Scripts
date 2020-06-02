#include <iostream>

using namespace std;

int cantidad_vocales(char*);
int cantidad_palabras(char*);
char* convertir_mayuscula(char*);


int main() {
  const char LISTADO_OPCIONES[6][60] = {
    "MENU\n",
    "1. Contar el número de vocales en un string.\n",
    "2. Contar el número de palabras en un string.\n",
    "3. Convertir en mayúscula todas las letras de un string.\n",
    "4. Fin\n",
    "Entre el número de la opción deseada: "
  };

  char opcion = '0';    // Contendrá la opción del usuario. Originalmente es 0
  char string[200];     // Contendrá el string del usuario

  while(opcion != '4'){

    // Imprimir menú
    for(int linea = 0; linea < 6; linea++)
      cout << LISTADO_OPCIONES[linea];
    
    // Recibir opción del usuario
    cin >> opcion;

    cout << "==== ==== ==== ==== ==== ====\n\n";

    if(opcion == '1'){
      // Recibir entrada
      cout << "Seleccionó la opción 1: Contar el número de vocales en un string.\n\n";

      cout << "Entre el string y presione 'enter': ";
      cin.get();    // Deseamos ignorar el 'enter' de la entrada previa
      cin.getline(string, 199, '\n');


      // Llamar funcion mientras se imprime la salida
      cout << "'" << string << "' tiene " << cantidad_vocales(string) << " vocales.\n\n";

      cout << "==== ==== ==== ==== ==== ====\n\n";

    } else
      if(opcion == '2'){
        cout << "Seleccionó la opción 2: Contar el número de palabras en un string.\n\n";
        
        // Recibir entrada
        cout << "Entre el string y presione 'enter': ";
        cin.get();    // Deseamos ignorar el 'enter' de la entrada previa
        cin.getline(string, 199, '\n');

        // Llamar funcion mientras se imprime la salida
        cout << "'" << string << "' tiene " << cantidad_palabras(string) << " palabras.\n\n";

        cout << "==== ==== ==== ==== ==== ====\n\n";

      } else
        if(opcion == '3'){
          cout << "Seleccionó la opción 3: Convertir en mayúscula todas las letras de un string.\n\n";
          
          // Recibir entrada
          cout << "Entre el string y presione 'enter': ";
          cin.get();    // Deseamos ignorar el 'enter' de la entrada previa
          cin.getline(string, 199, '\n');

          // Llamar funcion mientras se imprime la salida
          cout << "\t'" << string << "'\nse convierte en:\n\t'" << convertir_mayuscula(string) << "'.\n\n";

          cout << "==== ==== ==== ==== ==== ====\n\n";

        }

      
  }

    cout << "Adiós!!\n";


  return 0;
}



int cantidad_vocales(char* string){
  int vocales = 0;    // Contador de vocales

  // Iterando por cada caracter del string
  for(int i = 0; string[i] != '\0'; i++){
    if (string[i] == 'A' || string[i] == 'E' || string[i] == 'I' || string[i] == 'O' || string[i] == 'U' || string[i] == 'a' || string[i] == 'e' || string[i] == 'i' || string[i] == 'o' || string[i] == 'u'){
      // Aumentar contador si se encontró una vocal (mayúscula o minúscula)
      vocales++;
    }
  }

  return vocales;
}

int cantidad_palabras(char* string){
  int espacios = 0;   // Contador de espacios
  int palabras;       // Contador de palabras

  // Iterando por cada caracter del string
  for(int i = 0; string[i] != '\0'; i++){
    if(string[i] == ' '){
      // Aumentar contador de espacios
      espacios++;
    }
  }

  // Se asume que la última palabra no tiene espacio en blanco luego, asi que para contar esta última palabra se le debe añadir 1
  palabras = espacios + 1;

  return palabras;
}

char* convertir_mayuscula(char* string){
  // Iterando por cada caracter del string
  for(int i = 0; string[i] != '\0'; i++){
    // Si el caracter está en el rango de las minúsculas ...
    if(97 <= string[i] && string[i] <= 122){
      // Convertir en mayúscula tomando como referencia que:
      // `a` = 97 y `A`= 65
      // lo que señala que hay un offset de -32 entre mayúsculas y minúsculas
      string[i] -= 32;
    }
  }

  return string;
}