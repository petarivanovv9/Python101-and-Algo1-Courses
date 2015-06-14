#pragma once

class Vector {
public:
	Vector();
	~Vector();
public:
	void insert(int, int);
	void add(int);
	const int get(int) const;
	void remove(int);
	void pop();
	const int getSize() const;
	const int getCapacity() const;

	void printVector() const;
private:
	int* arr;
	int sizeArr;
	int capacity;
};