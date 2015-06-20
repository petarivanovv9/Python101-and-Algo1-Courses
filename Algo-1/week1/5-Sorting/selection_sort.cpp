#include "SelectionSort.h"


SelectionSort::SelectionSort() 
{
}


SelectionSort::~SelectionSort() 
{
}

void SelectionSort::sort(int* pArr, size_t sizeArr) {
	selectionSort(pArr, sizeArr);
}

void SelectionSort::selectionSort(int* pArr, size_t sizeArr) {
	if (!pArr || sizeArr == 0) {
		return;
	}

	for (size_t i = 0; i < sizeArr - 1; i++) {
		size_t min = i;

		for (size_t j = i + 1; j < sizeArr; j++) {
			if (pArr[j] < pArr[min]) {
				min = j;
			}
		}

		swapIf(pArr[i], pArr[min]);
	}
}

void SelectionSort::swapIf(int& a, int& b) {
	if (b < a) {
		int temp = a;
		a = b;
		b = temp;
	}
}