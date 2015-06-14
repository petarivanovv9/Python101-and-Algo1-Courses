#include "Vector.h"

#include <iostream>

Vector::Vector() {
	this->arr = NULL;
	this->sizeArr = 0;
	this->capacity = 4000;
}

Vector::~Vector() {
	delete[] this->arr;
	this->sizeArr = 0;
	this->capacity = 0;
}

void Vector::insert(int index, int value) {

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

void Vector::add(int value) {
	if (this->sizeArr == 0) {
		insert(0, value);
	}
	else {
		insert(this->sizeArr, value);
	}
}

const int Vector::get(int index) const {
	return this->arr[index];
}

void Vector::remove(int index) {
	for (int i = index; i < this->sizeArr - 1; i++) {
		this->arr[i] = this->arr[i + 1];
	}
	this->arr[sizeArr - 1] = NULL;
	this->sizeArr -= 1;
}

const int Vector::getSize() const {
	return this->sizeArr;
}

const int Vector::getCapacity() const {
	return this->capacity;
}

void Vector::printVector() const {
	std::cout << "Vector: ";

	for (int i = 0; i < this->sizeArr; i++) {
		std::cout << this->arr[i] << " ";
	}
	std::cout << std::endl;
}

void Vector::pop() {
	remove(this->sizeArr - 1);
}