#include "InsertionSort.h"


InsertionSort::InsertionSort()
{
}


InsertionSort::~InsertionSort()
{
}

void InsertionSort::sort(int* pArr, size_t sizeArr) {
	insertionSort(pArr, sizeArr);
}

void InsertionSort::insertionSort(int* pArr, size_t sizeArr) {
	if (!pArr || sizeArr == 0) {
		return;
	}

	for (size_t i = 1; i < sizeArr; i++) {
		size_t j = i;
		int currentNumber = pArr[j];

		while (pArr[j - 1] > currentNumber) {
			pArr[j] = pArr[j - 1];
			j--;
		}

		pArr[j] = currentNumber;
	}
}