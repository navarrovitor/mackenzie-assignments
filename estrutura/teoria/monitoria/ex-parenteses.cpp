#include <iostream>
#define tamanho 100
using namespace std;

typedef struct
{
  int topo;
  char item[tamanho];
} STACK;

void iniciaPilha(STACK &p)
{
  p.topo = -1;
}

bool pilhaVazia(STACK &p)
{
  if (p.topo == -1)
    return true;
  else
    return false;
}

bool pilhaCheia(STACK &p)
{
  if (p.topo == tamanho - 1)
    return true;
  else
    return false;
}

void empilha(STACK &p, char x)
{
  p.item[++p.topo] = x;
}

int desempilha(STACK &p)
{
  return (p.item[p.topo--]);
}

bool checar(char p[])
{
  STACK s;
  iniciaPilha(s);

  for (int i = 0; p[i] != '\0'; ++i)
  {
    // se o item que esta sendo analisado corresponde a ABERTURA. Devemos empilhar
    if (p[i] == '(' || p[i] == '[')
    {
      empilha(s, p[i]);
    }
    // se o item que esta sendo analisado corresponde a FECHAMENTO.
    else if (p[i] == ')')
    {
      // verificamos se ja houve algum item de ABERTURA, ou seja se algum item ja foi empilhado, então a pilha não pode estar vazia
      if (pilhaVazia(s))
      {
        // se estiver vazia quer dizer que não houve abertura, então a sequencia esta errada
        return 0;
      }
      else
      {
        // se não estiver vazia vamos desempilhar
        char c;
        c = desempilha(s);
        // o item desempilhado deve ser correspondente ao seu item de abertura, se ele não for correspondente a sequencia esta errada. ex: ([))
        if (c != '(')
        {
          return 0;
        }
      }
    }
    // o mesmo procedimento ocorre para o outro simbolo
    else if (p[i] == ']')
    {
      if (pilhaVazia(s))
      {
        return 0;
      }
      else
      {
        char c;
        c = desempilha(s);
        if (c != '[')
        {
          return 0;
        }
      }
    }
  }
  // ao final devemos ter a mesma quantidade de itens empilhados e de itens desempilhados, ou seja pilha deve estar vazia, se estiver vazia irá retornar True, validando então a sequencia
  return pilhaVazia(s);
}

// int validate (char s[])
// {
//     startStack ();
//     for (int i = 0; s[i] != '\0'; ++i) {
//         char c;
//         switch (s[i]) {
//             case ')':
//                 if (isEmpty ())
//                     return 0;
//                 c = pop ();
//                 if (c != '(')
//                     return 0;
//                 break;
//             case ']':
//                 if (isEmpty ())
//                     return 0;
//                 c = pop ();
//                 if (c != '[')
//                     return 0;
//                 break;
//             default:  push (s[i]);
//         }
//     }
//     return isEmpty ();
// }

int main()
{
  char palavra[tamanho] = {'(', '(', ')', ')'};

  if (checar(palavra))
  {
    cout << "Balanceado";
  }
  else
  {
    cout << "Não balanceado";
  }

  return 0;
}