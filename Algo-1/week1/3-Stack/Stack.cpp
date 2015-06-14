#include "Stack.h"

#include <iostream>

Stack::Stack() {
	this->arr = NULL;
	this->sizeArr = 0;
	this->capacity = 4000;
}

Stack::~Stack() {
	delete[] this->arr;
	this->sizeArr = 0;
	this->capacity = 0;
}

void Stack::push(int value) {
	int index = this->sizeArr;

	if (this->sizeArr + 1 == this->capacity) {
		this->capacity *= 2;
	}

	int* temp = new (std::nothrow) int[this->capacity];
	if (temp == NULL)
		return;
	for (int i = 0; i < index; i++) {
		temp[i] = this->arr[i];
	}

	temp[index] = value;

	for (int i = index; i < this->sizeArr; i++) {
		temp[i + 1] = arr[i];
	}

	this->sizeArr += 1;
	delete arr;
	this->arr = new (std::nothrow)int[this->capacity];
	for (int i = 0; i < this->sizeArr; i++) {
		this->arr[i] = temp[i];
	}
	delete temp;
}

int Stack::pop() {
	int firstElement = this->arr[this->sizeArr - 1];

	int* temp = new (std::nothrow) int[this->sizeArr - 1];
	//if (temp == NULL)
	//	return;
	for (int i = 0; i < this->sizeArr - 1; i++) {
		temp[i] = this->arr[i];
	}

	this->sizeArr--;
	delete arr;
	this->arr = new (std::nothrow)int[this->capacity];
	for (int i = 0; i < this->sizeArr; i++) {
		this->arr[i] = temp[i];
	}
	delete temp;

	return firstElement;
}

const int Stack::peek() const {
	return this->arr[this->sizeArr - 1];
}

const int Stack::getSize() const {
	return this->sizeArr;
}

void Stack::printQueue() const {
	std::cout << "Stack: ";

	for (int i = 0; i < this->sizeArr; i++) {
		std::cout << this->arr[i] << " ";
	}
	std::cout << std::endl;
}