#include <iostream>

// Utilizado para forzar utilizar 2 espacios decimales al imprimir doubles
#include <iomanip>

using namespace std;


int main() {
  const int meses = 12;            // Constante de cantidad de meses a ser evaluados
  int mes;                        // Variable de iteración
  double ventas[meses];           // Almacenará los precios de venta durante el año
  double sumatoria_ventas = 0;    // Acumulador para luego calcular promedio de ventas
  double promedio_ventas;         // Contendrá promedio de ventas
  double venta_mayor = -1;        // Venta mayor. -1 (un valor imposible) es valor defecto para prevenir econtrar problemas luego
  double venta_menor = -1;        // Venta menor. -1 (un valor imposible) es valor defecto para prevenir econtrar problemas luego

  // ENTRADA DE DATOS

  // Iterar por los 12 meses
  for(mes = 0; mes < meses; mes++){
    
    // Recibir entrada
    cout << "Entre las ventas del mes " << mes + 1 << ": $";
    cin >> ventas[mes];
    // cout << "\n";

    // Validar valor de entrada
    while(ventas[mes] < 0){
      cout << "Ventas invalidas. Re-entre valor no negativo: $";
      cin >> ventas[mes];
    }

    sumatoria_ventas += ventas[mes];

    // Actualizar valores de ventas mayores y menores si lo merita
    if(venta_mayor == -1 || venta_mayor < ventas[mes]){
      venta_mayor = ventas[mes];
    }

    if(venta_menor == -1 || venta_menor > ventas[mes]){
      venta_menor = ventas[mes];
    }

  }

  // Calcular promedio de ventas
  promedio_ventas = sumatoria_ventas / meses;

  // GENERAR REPORTE

  cout << "\n";
  // Separador
  for(int i = 0; i < 30; i++)
    cout << "=";

  // Encabezado
  cout << "\nREPORTE DE VENTAS DEL AÑO\n";

  // Separador
  for(int i = 0; i < 30; i++)
    cout << "=";

  cout << "\nMes\t\t\t\t\tVentas\n";

  cout << fixed << setprecision(2);
  // Imprimir valores de ventas para cada mes del año
  for(int mes = 0; mes < meses; mes++){
    cout << mes + 1 << "\t\t\t\t\t\t\t$" << ventas[mes] << "\n";
  }
  cout << "\t\t\t\t\t\t\t__________\n";
  cout << "TOTAL DEL AÑO\t\t\t\t$" << sumatoria_ventas << "\n";

  cout << "PROMEDIO MENSUAL\t\t\t$" << promedio_ventas << "\n\n";

  cout << "VENTA MENSUAL MAYOR:\t\t$" << venta_mayor << "\n";
  cout << "VENTA MENSUAL MENOR:\t\t$" << venta_menor << "\n\n";

  return 0;
}