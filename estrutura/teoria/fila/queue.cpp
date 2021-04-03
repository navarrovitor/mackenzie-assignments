#include "queue.h"

/*
DESTROY THE QUEUE FROM MEMORY
*/
Queue::~Queue()
{
  delete this->queue;
}

/*
CREATE NEW QUEUE WITH 0 INFO
*/
Queue::Queue()
{
}

/*
CREATE NEW QUEUE WITH THE CAPACITY ARGUMENT
*/
Queue::Queue(int c)
{
  this->queue = new int(c);
  this->size = 0;
  this->capacity = c;
  this->front = -1;
  this->rear = -1;
}

//--------------------QUEUE PARTICULARS METHODS--------------------//

/*
RETURN THE NUMBER OF ELEMENTS INSIDE A QUEUE
*/
int Queue::noOfElements()
{
  return this->size;
}

/*
RETURN THE CAPACITY OF A QUEUE
*/
int Queue::maxCapacity()
{
  return this->capacity;
}

/*
RETURN THE FRONT OF A QUEUE
*/
int Queue::queueFront()
{
  return this->front;
}

/*
RETURN THE REAR OF A QUEUE
*/
int Queue::queueRear()
{
  return this->rear;
}

/*
RETURN TRUE IF QUEUE IF FULL
*/
bool Queue::full()
{
  return this->size == this->capacity;
}

/*
RETURN TRUE IF QUEUE IS EMPTY
*/
bool Queue::empty()
{
  return this->size == 0;
}

//--------------------QUEUE CHANGING METHODS-----------------------//
//--------------------QUEUE CHANGING METHODS-----------------------//

/*
DEQUEUE THE FIRST ELEMENT THAT ENTERED THE QUEUE
(FIRST IN FIRST OUT)
RETURNS THE ELEMENT DEQUEUED
RETURNS -1 IF QUEUE IS EMPTY
*/
int Queue::dequeue()
{
  if (empty())
  {
    this->front, this->rear = -1;
    return -1;
  }
  else
  {
    int e = this->front;
    this->front = (this->front + 1) % this->capacity;
    this->size--;
    return e;
  }
}

/*
ENQUEUE THE GIVEN ELEMENT INTO THE QUEUE
RETURNS THE QUEUE SIZE
RETURNS -1 IF QUEUE IS FULL
*/
int Queue::enqueue(int e)
{
  if (full())
  {
    return -1;
  }
  this->rear = (this->rear + 1) % this->capacity;
  if (this->front == -1)
  {
    this->front = 0;
  }
  this->queue[this->rear] = e;
  this->size++;
  return this->size;
}

/*
ENQUEUE THE GIVEN ELEMENT INTO THE QUEUE IN A TUPLE FORMAT
RETURNS THE QUEUE SIZE
RETURNS -1 IF QUEUE IS FULL
*/
int Queue::enqueueTuple(int pos, int e)
{
  if (full())
  {
    return -1;
  }
  this->rear = (this->rear + 1) % this->capacity;
  if (this->front == -1)
  {
    this->front = 0;
  }
  this->queue[this->rear] = (pos, e);
  this->size++;
  return this->size;
}

//--------------------QUEUE INFORMATION METHODS--------------------//

/*
RETURN THE INDEX OF GIVEN ELEMENT INSIDE QUEUE
RETURN -1 IF QUEUE IS EMPTY
*/
int Queue::elementIndex(int e)
{
  if (empty())
  {
    return -1;
  }
  else
  {
    if (this->front <= this->rear)
    {
      for (int i = front; i <= this->rear; i++)
      {
        if (this->queue[i] == e)
        {
          return (i - this->front);
          // return (i - this->front) + 1;
        }
      }
    }
    else
    {
      for (int i = this->front; i < this->capacity; i++)
      {
        if (this->queue[i] == e)
          return (i - this->front);
        // return (i - this->front) + 1;
      }
      for (int i = 0; i < this->rear + 1; i++)
      {
        if (this->queue[i] == e)
          return this->size - this->rear + i;
      }
    }
  }
  return -1;
}

/*
PRINT ALL THE VALUES IN THE CURRENT QUEUE
*/
void Queue::print()
{
  if (empty())
  {
    cout << "The queue is empty.\n";
  }
  else
  {
    if (this->front <= this->rear)
    {
      for (int i = this->front; i <= this->rear; i++)
      {
        cout << this->queue[i] << ' ';
      }
    }
    else
    {
      int i = this->front;
      while (i < this->size)
      {
        cout << this->queue[i] << ' ';
        i++;
      }
      i = 0;
      while (i <= this->rear)
      {
        cout << this->queue[i] << ' ';
        i++;
      }
    }
  }
}