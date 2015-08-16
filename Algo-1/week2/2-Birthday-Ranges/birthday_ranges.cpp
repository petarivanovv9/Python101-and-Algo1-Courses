#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int birthdaysCounter[366] = { 0 };
int n;
int m;

void getBirthdaysCount() {
	cin >> n;
	cin >> m;

	vector<int> birthdays(n);

	for (int i = 0; i < n; i++) {
		cin >> birthdays[i];
	}
	sort(birthdays.begin(), birthdays.end());

	int counter = 0;
	int index = 0;

	for (int i = 0; i < 366; i++) {
		birthdaysCounter[i] = counter;

		while (index < n && birthdays[index] == i) {
			birthdaysCounter[i]++;
			index++;
			counter++;
		}

	}

	int leftRange;
	int rightRange;

	for (int i = 0; i < m; i++) {
		cin >> leftRange;
		cin >> rightRange;
		
		int result = birthdaysCounter[rightRange] - (leftRange > 0 ? birthdaysCounter[leftRange - 1] : 0);
		cout << result << '\n';
	}
}

int main() {

	getBirthdaysCount();

	return 0;
}