#ifndef QUEUE_H
#define QUEUE_H

#include <string>
#include <iostream>

using namespace std;

class Queue
{
private:
  int *queue;
  int size;
  int capacity;
  int front;
  int rear;

public:
  Queue();
  Queue(int c);
  ~Queue();
  int noOfElements();
  int maxCapacity();
  int queueFront();
  int queueRear();
  bool full();
  bool empty();
  int dequeue();
  int enqueue(int e);
  int enqueueTuple(int pos, int e);
  int elementIndex(int e);
  void print();
};

#endif