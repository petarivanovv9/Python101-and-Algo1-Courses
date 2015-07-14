#include <vector>
#include <iostream>
#include <algorithm>

class Pair {
public:
	int start;
	int end;
};

class BirthdayRanges {
public:

	// Returns a vector with the number of people born in the specific ranges.
	std::vector<int> birthdaysCount(std::vector<int>& birthdays, std::vector<std::pair<int, int> >& ranges) {
		
		int histogram[366] = { 0 };

		std::vector<int> results;
		//std::sort(birthdays.begin(), birthdays.end());

		for (int i = 0; i < 366; i++) {
			histogram[birthdays[i]]++;
		}

		for (int i = 1; i < 366; i++) {
			histogram[i] += histogram[i - 1];
		}

		int r1, r2;

		for (int i = 0; i != ranges.size(); i++) {
			r1 = ranges[i].first;
			r2 = ranges[i].second;

			results[i] = histogram[r2] - histogram[r1];
		}

		return results;
	}
};

int main() {

	int numBirthdays;
	int numRanges;

	std::cout << "number of birthdays: ";
	std::cin >> numBirthdays;

	std::cout << "number of ranges: ";
	std::cin >> numRanges;

	std::vector<int> birthdays(numBirthdays);
	int birthday;
	for (int i = 0; i < numBirthdays; i++) {
		std::cout << "birthday: ";
		std::cin >> birthday;
		birthdays[i] = birthday;
	}

	int first;
	int last;

	std::vector<std::pair<int, int> > ranges(numRanges);
	for (int i = 0; i < numRanges; i++) {
		//std::cout << "------" << std::endl;
		std::cout << "first: ";
		std::cin >> first;
		std::cout << "last: ";
		std::cin >> last;
		ranges[i] = std::make_pair(first, last);
	}

	BirthdayRanges test;

	std::vector<int> result = test.birthdaysCount(birthdays, ranges);
	//for (int i = 0; i < result.size(); i++) {
	//	std::cout << result[i] << std::endl;
	//}


	return 0;
}