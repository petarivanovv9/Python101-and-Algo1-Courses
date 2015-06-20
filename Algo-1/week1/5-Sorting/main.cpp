#include <iostream>

#include "SelectionSort.h"
#include "InsertionSort.h"
#include "CountSort.h"


int main() {

	int arr[] = { 2, 3, 5, 6, 3, 3, 9, 55, 1020, 555, 312, 1, 3412, 11, 23, 55 };
	int sizeArr = (sizeof(arr) / sizeof(*arr));
	
	std::cout << "sizeOfArray: " << sizeArr << std::endl;

	std::cout << "------------------------------------------------------" << std::endl;

	int arr_2[] = { 1, 3, 3, 5, 8, 6, 4, 4, 8, 3, 1, 0 };
	int sizeArr_2 = (sizeof(arr_2) / sizeof(*arr_2));

	std::cout << "sizeOfArray: " << sizeArr_2 << std::endl;

	std::cout << "------------------------------------------------------" << std::endl;


	return 0;
}