#include "queue.h"

//-------------------------OTHER METHODS--------------------------//

/*
CREATE A QUEUE
RETURN THAT QUEUE
*/
Queue createQueue()
{
  int queueSize, element;
  cout << "\nWhat will be the capacity of your queue? ";
  cin >> queueSize;
  Queue temp(queueSize);
  for (int i = 0; i < queueSize; i++)
  {
    cout << "\nWhat value do you want to enqueue (choose -1 to end queue)? ";
    cin >> element;
    if (element == -1)
    {
      cout << "\nEnding queue...\n";
      break;
    }
    else
    {
      temp.enqueue(element);
    }
  }
  return temp;
}

/*
MULTIPLEX THREE QUEUES
RETURNS A QUEUE WITH THE SHARED FLUX
*/
Queue multiplex(Queue one, Queue two, Queue three)
{
  int finalSize = one.noOfElements() + two.noOfElements() + three.noOfElements(), i = 1;
  Queue temp(finalSize);
  // while (!one.empty() || !two.empty() || !three.empty())
  // {
  //   if (!one.empty())
  //     temp.enqueue(one.dequeue());
  //   // temp.enqueueTuple(i, one.dequeue());
  //   if (!two.empty())
  //     temp.enqueue(one.dequeue());
  //   // temp.enqueueTuple(i, two.dequeue());
  //   if (!three.empty())
  //     temp.enqueue(one.dequeue());
  //   // temp.enqueueTuple(i, three.dequeue());
  //   i++;
  // }
  return temp;
}