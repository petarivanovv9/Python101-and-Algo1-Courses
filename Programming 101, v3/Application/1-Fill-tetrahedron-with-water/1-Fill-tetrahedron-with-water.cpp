#include <iostream>
#include <cmath>

using namespace std;

double fill_tetrahedron(int len);

int main() {

	int num = 0;

	cout << "Enter the edge length of a Regular tetrahedron in centimeters: ";
	cin >> num;

	cout << "You can fill Regular tetrahedron with edge of " << num << "cm with " << fill_tetrahedron(num) << " liters of water." << '\n';

	return 0;
}

double fill_tetrahedron(int num) {
	
	double lenDec = num / 10; //convert the edge length into decimeters
	double volume = 0;

	volume = (sqrt(2.0) * lenDec * lenDec * lenDec) / 12;

	return volume;
}