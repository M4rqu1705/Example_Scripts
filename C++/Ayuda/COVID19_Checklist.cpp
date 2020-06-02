#include <iostream>

using namespace std;

int main() {

  // Constante que se puede manipular con adición o remoción de preguntas y criterios
  const int CANTIDAD_PREGUNTAS = 12;

  // Matriz de preguntas
  const char PREGUNTAS[CANTIDAD_PREGUNTAS][80] = {
    "Do you have cough?",
    "Do you have colds?",
    "Do you have diarrhea?",
    "Do you have sore throat?",
    "Are you experiencing myalgia or body aches?",
    "Do you have a headache?",
    "Do you have fever (Temperature of 38.7C or above)?",
    "Are you having difficulty breathing?",
    "Are you experiencing fatigue?",
    "Have you traveled recently during the last 14 days?",
    "Do you have a travel history to a COVID-19 infected area?",
    "Do you have direct contact or is taking care of a positive COVID-19 patient?" 
  };

  // Puntuaciones correspondientes que se asignarán a base de un 1 (si) o 2 (no)
  const int PUNTUACIONES[CANTIDAD_PREGUNTAS] {
    1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3
  };

  // Array de respuestas (inicialmente 0)
  int respuestas[CANTIDAD_PREGUNTAS] = {0};
  // Puntuación por defecto
  int puntuacion = 0;

  // Está al final de cada pregunta, asi que para prevenir tener que reemplazar 12 instancias de este sufijo común, se cambiar solo aqui
  const char sufijo[] = "(1=Yes, 2=No) ";


  // Encabezado
  cout << "COVID-19 CHECKLIST\n";
  cout << "Please answer these questions. (Use 1 if you have the symptom. Use 2 if you do not)\n\n";

  // Realizar preguntas
  for(int pregunta = 0; pregunta < CANTIDAD_PREGUNTAS; pregunta++){
    cout << "Question " << pregunta + 1 << "\n";
    cout << PREGUNTAS[pregunta] << sufijo;
    cin >> respuestas[pregunta];

    // Validar respuesta de usuario
    while(respuestas[pregunta] != 1 && respuestas[pregunta] != 2){
      cout << "Invalid answer for Question " << pregunta + 1 << ". Re-enter " << sufijo;
      cin >> respuestas[pregunta];
    }
    cout << "\n";

    // Aplicar puntuación si la respuesta fue 1
    if(respuestas[pregunta] == 1){
      puntuacion += PUNTUACIONES[pregunta];
    }
  }


  // GENERAR RESULTADOS
  cout << "\n";
  // Separador
  for(int i = 0; i < 30; i++)
    cout << "=";

  cout << "\nRESULTS\n";
  cout << "Your Score (Maximum = 24): " << puntuacion << "\n\n";

  cout << "INTERPRETATION:\n";
  // Seleccionar interpretación a base de puntuación
  if(0 <= puntuacion && puntuacion <= 2){
    cout << "May be stress related and observe.\n";
  } else
    if(3 <= puntuacion && puntuacion <= 5){
      cout << "Hydrate properly and proper personal hygiene.\n\tObserve and Re-evaluate after 2 days.\n";
    } else
      if(6 <= puntuacion && puntuacion <= 12){
        cout << "Seek a consultation with Doctor\n";
      } else
        if(12 <= puntuacion && puntuacion <= 24){
          cout << "Call 911!\n";
        }
  
  // Separador
  for(int i = 0; i < 30; i++)
    cout << "=";

  cout << "\n";

}