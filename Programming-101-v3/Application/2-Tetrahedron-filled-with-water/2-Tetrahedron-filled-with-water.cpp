#include <iostream>
#include <cmath>

double fill_tetrahedron(int len);
int tetrahedron_filled(int *tetrahedrons, int water, int n);
void selectionSort(int *tetrahedrons, size_t n);

using namespace std;

int main() {

	int n = 0; //size of the array
	cout << "How many tetrahedrons you want to enter: ";
	cin >> n;

	int *tetrahedrons = new (nothrow) int[n]; //create a dynamic int array

	for (int i = 0; i < n; i++) {
		cout << "Enter tetrahedron[" << i << "] = ";
		cin >> tetrahedrons[i];
	}

	int water = 0;
	cout << "Enter the amount of water in litters: ";
	cin >> water;

	cout << "You can fill only " << tetrahedron_filled(tetrahedrons, water, n) << " of this Regular tetrahedrons with " << water << " liters of water." << '\n';

	delete[] tetrahedrons; //delete the memory

	return 0;
}

double fill_tetrahedron(int num) {

	double lenDec = num / 10; //convert the edge length into decimeters
	double volume = 0;

	volume = (sqrt(2.0) * lenDec * lenDec * lenDec) / 12;

	return volume;
}

int tetrahedron_filled(int *tetrahedrons, int water, int n) {

	selectionSort(tetrahedrons, n);

	double sumVolume = 0;
	int counter = 0;

	for (int i = 0; i < n; i++) {
		if ( ( fill_tetrahedron(tetrahedrons[i]) + sumVolume ) < water ) {
			counter++;
			sumVolume += fill_tetrahedron(tetrahedrons[i]);
		}
	}

	return counter;
}

void selectionSort(int *tetrahedrons, size_t n) {
	size_t min;

	for (size_t i = 0; i < n; i++) {
		min = i;
		for (size_t j = i + 1; j < n; j++) {
			if (tetrahedrons[j] < tetrahedrons[min]) {
				min = j;
			}
		}
		if (min != i) {
			int temp = 0;
			temp = tetrahedrons[i];
			tetrahedrons[i] = tetrahedrons[min];
			tetrahedrons[min] = temp;
		}
	}
}