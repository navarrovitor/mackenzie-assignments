#include <iostream>

using namespace std;

struct aluno
{
  string nome;
  string curso;
  int matricula;
};

void ordenar(aluno vet[], int n)
{
  int i, j, aux_mat;
  string aux_curso, aux_nome;
  for (i = 1; i < n; i++)
  {
    aux_mat = vet[i].matricula;
    aux_curso = vet[i].curso;
    aux_nome = vet[i].nome;
    j = i - 1;
    while (j >= 0 && vet[j].matricula > aux_mat)
    {
      vet[j + 1].matricula = vet[j].matricula;
      vet[j + 1].curso = vet[j].curso;
      vet[j + 1].nome = vet[j].nome;
      j = j - 1;
    };
    vet[j + 1].matricula = aux_mat;
    vet[j + 1].curso = aux_curso;
    vet[j + 1].nome = aux_nome;
  };
};

int exec = 1;

int busca_binaria(aluno vet[], int esquerda, int direita, int x)
{
  if (direita >= esquerda)
  {
    int meio = esquerda + (direita - esquerda) / 2;
    if (vet[meio].matricula == x)
    {
      cout << "Nome do aluno buscado:" << vet[meio].nome << endl;
      cout << "Curso do aluno buscado:" << vet[meio].curso << endl;
      cout << "Número de execuções do programa:" << exec << endl;
    }
    exec++;
    if (vet[meio].matricula > x)
      return busca_binaria(vet, esquerda, meio - 1, x);
    return busca_binaria(vet, meio + 1, direita, x);
  };
  // cout << "Matrícula não encontrada." << endl;
  return -1;
};

int main()
{
  int n_alunos = 7;
  int i, mat_desejada;
  aluno alunos[n_alunos];

  for (i = 0; i < n_alunos; i++)
  {
    cout << "Estudante número:" << i + 1 << endl;
    cout << "Digite o seu nome:" << endl;
    cin >> alunos[i].nome;
    cout << "Digite o seu curso:" << endl;
    cin >> alunos[i].curso;
    cout << "Digite a sua matricula:" << endl;
    cin >> alunos[i].matricula;
  };

  cout << "Digite a matricula desejada:" << endl;
  cin >> mat_desejada;

  cout << "Busca sequencial:" << endl;
  for (i = 0; i < n_alunos; i++)
  {
    if (alunos[i].matricula == mat_desejada)
    {
      cout << "Nome do aluno buscado:" << alunos[i].nome << endl;
      cout << "Curso do aluno buscado:" << alunos[i].curso << endl;
      cout << "Número de execuções do programa:" << exec << endl;
    }
    // else if (i == n_alunos - 1 and alunos[i].matricula != mat_desejada)
    // {
    //   cout << "Matrícula não encontrada." << endl;
    // }
    exec++;
  };
  exec = 1;
  cout << "Busca binária:" << endl;
  ordenar(alunos, n_alunos);
  busca_binaria(alunos, 0, n_alunos - 1, mat_desejada);
};