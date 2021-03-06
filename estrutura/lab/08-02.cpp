#include <iostream>
using namespace std;
int main()
{
  int vetor[20], i;
  cout << "Quais os valores do seu vetor?\n";
  for (i = 0; i < 20; i++)
  {
    cin >> vetor[i];
    cout << vetor[i] << "\n";
  }
}