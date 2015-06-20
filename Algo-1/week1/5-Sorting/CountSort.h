#pragma once

class CountSort {
public:
	CountSort();
	~CountSort();
public:
	void sort(int*, size_t);
private:
	void countingSort(int*, size_t);
};