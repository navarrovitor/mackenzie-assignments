#include "queue.h"
#include "methods.cpp"

// using namespace std;

int main()
{
     Queue fluxOne = createQueue(), fluxTwo = createQueue(), fluxThree = createQueue();
     cout << "These are the three fluxes created:\n";
     cout << "Flux one:\n";
     fluxOne.print();
     cout << endl;
     cout << "Flux two:\n";
     fluxTwo.print();
     cout << endl;
     cout << "Flux three:\n";
     fluxThree.print();
     cout << endl;
     // multiplex(fluxOne, fluxTwo, fluxThree);
     // Queue multiplexedFluxes = multiplex(fluxOne, fluxTwo, fluxThree);
     // multiplexedFluxes.print();
}

// int main()
// {
//   cout << "\n----------------------------------------------";
//   cout << "\n PROGRAMA PARA APRENDIZADO DO TAD FILA (VETOR)";
//   cout << "\n----------------------------------------------";

//   int tamVet;
//   cout << "\n\nInforme o tamanho do vetor para uso da fila: ";
//   cin >> tamVet;

//   Queue fila(tamVet);

//   while (true)
//   {

//     cout << "\n0 - sair ";
//     cout << "\n1 - inserir na fila ";
//     cout << "\n2 - extrair da fila ";
//     cout << "\n3 - imprimir a fila ";
//     cout << "\n4 - verificar se o item está na fila (retorna a posição na fila)";
//     cout << "\n5 - tamanho da fila ";

//     int opc = 0;
//     cout << "\n\nForneca sua opção: ";
//     cin >> opc;

//     if (opc == 0)
//     {
//       break;
//     }
//     else if (opc == 1)
//     {
//       int dado = -1;
//       cout << "\nInforme o valor do novo elemento: ";
//       cin >> dado;
//       int x = fila.enqueue(dado);
//       if (x == -1)
//       {
//         cout << "\nERRO: A fila está lotada.";
//       }
//       else if (x == -2)
//       {
//         cout << "\nERRO: Este elemento já está na fila.";
//       }
//       else
//       {
//         cout << "\n Incluido com sucesso na posição " << x;
//       }
//     }
//     else if (opc == 2)
//     {
//       break;
//     }
//     else if (opc == 3)
//     {
//       fila.print();
//     }
//     else if (opc == 4)
//     {
//       break;
//     }
//     else if (opc == 5)
//     {
//       break;
//     }

//     cout << "\n\n";
//     cout << "\n----------------------------------------------";
//     cout << "\n PROGRAMA PARA APRENDIZADO DO TAD FILA (VETOR)";
//     cout << "\n----------------------------------------------";
//   }

//   cout << "\n\n--- Obrigado e até a proxima ---\n";
//   return 0;
// }
