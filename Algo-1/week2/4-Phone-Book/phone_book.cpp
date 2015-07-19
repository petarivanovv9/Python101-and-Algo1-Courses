#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

//using namespace std;

std::vector<std::string> lookUpNames(std::vector<std::pair<int, std::string> > phoneBook, std::vector<int> numbers) {

	std::vector<std::string> names;

	std::sort(phoneBook.begin(), phoneBook.end());

	for (size_t i = 0; i < numbers.size(); i++) {

		int left = 0;
		int right = phoneBook.size() - 1;
		int mid;
		bool isNumberFound = false;

		while (left <= right) {

			mid = left + (right - left) / 2;

			if (phoneBook[mid].first == numbers[i]) {
				isNumberFound = true;
				break;
			}
			else if (phoneBook[mid].first < numbers[i]) {
				left = mid + 1;
			}
			else {
				right = mid - 1;
			}
		}

		if (isNumberFound) {
			//std::cout << "here" << std::endl;
			names.push_back(phoneBook[mid].second);
			//std::cout << names[0] << std::endl;
		}

	}

	return names;
}

int main() {

	int n;
	std::cin >> n;

	int m;
	std::cin >> m;

	int number;
	std::string name;

	std::vector<std::pair<int, std::string> > phoneBook(n);

	for (int i = 0; i < n; i++) {
		std::cin >> number;
		//std::cin >> name;
		std::getline(std::cin, name);
		phoneBook.push_back(std::make_pair(number, name));
		std::cout << "+++ " << name << std::endl;
		std::cout << "--- " << phoneBook[i].first << std::endl;
		std::cout << "--- " << phoneBook[i].second << std::endl;
	}

	std::vector<int> numbers(m);

	for (int i = 0; i < m; i++) {
		std::cin >> number;
		numbers.push_back(number);
	}

	std::vector<std::string> result = lookUpNames(phoneBook, numbers);

	for (int i = 0; i < m; i++) {
		//cout << "?/?" << endl;
		std::cout << result[i] << std::endl;
	}

	return 0;
}