#include <vector>
#include <iostream>
#include <algorithm>


class KMin {
public:
	// Finds the k-th minimum element in an unsorted collection.
	int kthMinimum(std::vector<int> numbers, int k) {

		int* arr = new int[k];
		for (int i = 0; i < k; i++) {
			arr[i] = numbers[i];
		}

		std::make_heap(arr, arr + k);

		int sizeNumbers = numbers.size();
		for (int i = k; i < sizeNumbers; i++) {
			if (numbers[i] < arr[0]) {
				arr[0] = numbers[i];
				std::make_heap(arr, arr + k);
			}
		}

		int result = arr[0];
		
		delete[] arr;

		return result;
	}
};

//int main() {
//
//	std::vector<int> numbers = { 9, 5, 11, 2, 4, 7, 8 };
//	KMin test;
//	
//	int k;
//	std::cout << "k: ";
//	std::cin >> k;
//
//	std::cout << k << "-th smallest: " << test.kthMinimum(numbers, k) << std::endl;
//	
//	return 0;
//}