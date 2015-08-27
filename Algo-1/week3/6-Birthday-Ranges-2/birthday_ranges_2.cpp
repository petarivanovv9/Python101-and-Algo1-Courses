#include <iostream>
#include <vector>
#include <string>

using namespace std;

int tree[1024] = { 0 };


class BirthdayRanges {
public:
	
	// adds people who are born on a specific day
	void add(int day, int numberOfPeople) {
		int index = 512 + day;

		while (index) {
			tree[index] += numberOfPeople;
			index /= 2;
		}
	}

	// removes people who are born on a specific day
	void remove(int day, int numberOfPeople) {
		int index = 512 + day;
		int removeCount = (tree[index] >= numberOfPeople ? numberOfPeople : tree[index]);

		while (index) {
			tree[index] -= removeCount;
			index /= 2;
		}
	}

	// return the number of people born in a range
	int count(int startDay, int endDay) {
		startDay += 512;
		endDay += 513;

		int startSum = 0;
		int endSum = 0;

		while (startDay > 1) {
			if (startDay % 2) {
				startSum += tree[--startDay];
			}
			startDay /= 2;
		}

		while (endDay > 1) {
			if (endDay % 2) {
				endSum += tree[--endDay];
			}
			endDay /= 2;
		}

		return endSum - startSum;
	}

};


int main() {

	cin.sync_with_stdio(false);
	cin.tie(0);

	BirthdayRanges Test;

	int n, m;
	cin >> n >> m;

	for (int i = 0; i < n; i++) {
		int temp;
		cin >> temp;
		Test.add(temp, 1);
	}

	for (int i = 0; i < m; i++) {
		string command;
		cin >> command;

		int a, b;
		cin >> a >> b;

		if (command == "count") {
			cout << Test.count(a, b) << endl;
		}
		else if (command == "remove") {
			Test.remove(a, b);
		}
		else if (command == "add") {
			Test.add(a, b);
		}
	}


	return 0;
}