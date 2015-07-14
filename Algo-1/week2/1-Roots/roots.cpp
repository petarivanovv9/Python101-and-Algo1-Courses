#include <iostream>
#include <cmath>
#include <iomanip>

class Roots {
public:
	double squareRoot(int);
private:
	double binarySearch(double, int);
};

double Roots::binarySearch(double precision, int number) {
	
	double start = 0;
	double end = number / 2.0;

	for (int i = 0; i <= precision + 1; i++) {

		while (abs(start - end) > precision) {
			double middle = start + ((end - start) / 2);
			double middleSquare = middle * middle;

			if (middleSquare > number) {
				end = middle - precision;
			}
			else if (middleSquare < number) {
				//std::cout << "start: " << start << std::endl;
				//std::cout << "middle: " << middle << std::endl;
				start = middle + precision;
			}
		}
	}

	return start;
}

double Roots::squareRoot(int number) {
	return binarySearch(0.000001, number);
}

//int main() {
//
//	int number;
//	std::cin >> number;
//
//	Roots test;
//
//	std::cout << std::fixed;
//	std::cout << std::setprecision(5) << test.squareRoot(number) << std::endl;

//	return 0;

//}