#include <iostream>
#include <algorithm>

//
// If b < a, the function swap their values
//
void swapIf(int&, int&);

//
// Selection sort
//
void selectionSort(int*, size_t);

//
// Insertion sort
//
void insertionSort(int*, size_t);


int main() {

	int arr[] = { 2, 3, 5, 6, 3, 3, 9, 55, 1020, 555, 312, 1, 3412, 11, 23, 55 };
	int sizeArr = (sizeof(arr) / sizeof(*arr));
	
	std::cout << "sizeOfArray: " << sizeArr << std::endl;

	std::cout << "-----------------------------------" << std::endl;

	std::cout << "Selection sort: " << std::endl;
	selectionSort(arr, sizeArr);

	for (size_t i = 0; i < sizeArr; i++) {
		std::cout << arr[i] << " ";
	}
	std::cout << std::endl;

	std::cout << "-----------------------------------" << std::endl;

	std::cout << "Insertion sort: " << std::endl;
	insertionSort(arr, sizeArr);

	for (size_t i = 0; i < sizeArr; i++) {
		std::cout << arr[i] << " ";
	}
	std::cout << std::endl;

	std::cout << "-----------------------------------" << std::endl;


	return 0;
}

//
// Selection sort
//
void selectionSort(int* pArr, size_t sizeArr) {
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

		//if (min != i)
		//	std::swap(pArr[i], pArr[min]);

		swapIf(pArr[i], pArr[min]);
	}
}

//
// If b < a, the function swap their values
//
void swapIf(int& a, int& b) {
	if (b < a) {
		int temp = a;
		a = b;
		b = temp;
	}
}

//
// Insertion sort
//
void insertionSort(int* pArr, size_t sizeArr) {
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