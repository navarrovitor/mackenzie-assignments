#include <iostream>

using namespace std;

#define MAX 10

typedef struct
{
  int top;
  int data[MAX];
} stack;

void start(stack &p)
{
  p.top = -1;
};

bool empty(stack &p)
{
  return (p.top < 0);
};

bool full(stack &p)
{
  if (p.top == MAX - 1)
    return true;
  else
    return false;
}

void push(stack &p, int x)
{
  p.data[++p.top] = x;
  cout << endl
       << "top: " << p.top << endl
       << x << " empilhado" << endl;
}

int pop(stack &p)
{
  return (p.data[p.top--]);
}

int qty(stack &p)
{
  return (p.top + 1);
}

void print(stack &p)
{
  // for (int i = 0; i < MAX; i++)
  // {
  //   cout << p.data[i] << ", ";
  // };
  cout << endl
       << "Sua pilha tem " << qty(p) << " elementos." << endl;
}

int main()
{
  stack pile;
  start(pile);

  if (empty(pile))
    cout << "A pilha esta inicialmente vazia." << endl;
  else
    cout << "A pilha foi criada e nao esta vazia." << endl;

  push(pile, 10);
  push(pile, 3);
  push(pile, 5);
  push(pile, 19);

  print(pile);

  if (full(pile))
    cout << "A pilha esta cheia." << endl;
  else
    cout << endl
         << "Ainda cabem elementos na pilha."
         << endl;

  cout << endl
       << "Item desempilhado: " << pop(pile) << endl
       << endl
       << "Item desempilhado: " << pop(pile) << endl;
  print(pile);

  return 0;
};