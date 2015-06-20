#pragma once

class InsertionSort {
public:
	InsertionSort();
	~InsertionSort();
public:
	void sort(int*, size_t);
private:
	void insertionSort(int* pArr, size_t sizeArr);
};

