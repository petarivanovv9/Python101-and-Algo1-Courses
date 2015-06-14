#pragma once

class Stack {
public:
	Stack();
	~Stack();
public:
	void push(int);
	int pop();
	const int peek() const;

	const int getSize() const;

	void printQueue() const;
private:
	int* arr;
	int sizeArr;
	int capacity;
};