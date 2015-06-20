#pragma once

class SelectionSort {
public:
	SelectionSort();
	~SelectionSort();
public:
	void sort(int*, size_t);
private:
	void selectionSort(int*, size_t);
	
	// If b < a, the function swap their values
	void swapIf(int&, int&);
};