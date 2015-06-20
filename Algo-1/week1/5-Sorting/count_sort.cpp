#include "CountSort.h"


CountSort::CountSort()
{
}


CountSort::~CountSort()
{
}

void CountSort::sort(int* pArr, size_t sizeArr) {
	countingSort(pArr, sizeArr);
}

void CountSort::countingSort(int* pArr, size_t sizeArr) {
	if (!pArr || sizeArr == 0) {
		return;
	}

	int maxN = 0;

	for (size_t i = 0; i < sizeArr; i++) {
		if (maxN < pArr[i]) {
			maxN = pArr[i];
		}
	}

	size_t* pArrHistogram = new size_t[maxN + 1];

	for (size_t i = 0; i <= maxN; i++) {
		pArrHistogram[i] = 0;
	}

	for (size_t i = 0; i < sizeArr; i++) {
		pArrHistogram[pArr[i]]++;
	}

	size_t pos = 0;

	for (int i = 0; i <= maxN; i++) {

		while (pArrHistogram[i] > 0) {
			pArr[pos] = i;
			pArrHistogram[i]--;
			pos++;
		}
	}

	delete[] pArrHistogram;
}