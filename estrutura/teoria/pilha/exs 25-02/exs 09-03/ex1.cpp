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
};

void push(stack &p, int x)
{
  p.data[++p.top] = x;
};

int pop(stack &p)
{
  return (p.data[p.top--]);
};

int qty(stack &p)
{
  return (p.top + 1);
};

void print(stack &p)
{
  stack aux;
  start(aux);

  int element, i = 0, quant = qty(p);

  cout
      << endl
      << "Sua pilha tem " << qty(p) << " elementos." << endl
      << "E eles são:" << endl;

  for (i = 0; i < quant; ++i)
  {
    element = pop(p);
    cout << element << endl;
    push(aux, element);
  }

  for (i = 0; i < quant; i++)
  {
    element = pop(aux);
    push(p, element);
  };
};

bool balanced(char exp[])
{
  stack s;
  start(s);
  for (int i = 0; exp[i] != '\0'; i++)
  {
    if (exp[i] == '(' || exp[i] == '[' || exp[i] == '{')
    {
      push(s, exp[i]);
    }
    else if (exp[i] == ')')
    {
      if (empty(s))
      {
        return false;
      }
      else
      {
        char c = pop(s);
        if (c != '(')
        {
          return false;
        }
      }
    }
    else if (exp[i] == ']')
    {
      if (empty(s))
      {
        return false;
      }
      else
      {
        char c = pop(s);
        if (c != '[')
        {
          return false;
        }
      }
    }
    else if (exp[i] == '}')
    {
      if (empty(s))
      {
        return false;
      }
      else
      {
        char c = pop(s);
        if (c != '{')
        {
          return false;
        }
      }
    }
  }
  return empty(s);
};

int main()
{
  char test[MAX] = {'(', ')'};
  cout << "A expressão que será testada é a seguinte: " << endl;
  for (int i = 0; i < MAX; i++)
    cout << test[i] << " ";
  cout << endl
       << (balanced(test) ? "Balanceado" : "Não balanceado") << endl;
  return 0;
};
