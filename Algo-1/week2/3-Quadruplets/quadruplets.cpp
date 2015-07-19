#include <iostream>
#include <algorithm>
#include <vector>


class Quadruplets {
public:
	// Returns the number of quadruplets that sum to zero
	int zeroQuadrupletsCount(std::vector<int>& a, std::vector<int>& b, std::vector<int>& c, std::vector<int>& d) {
		
		int counter = 0;

		std::vector<int> AandBpermutation;

		for (int i = 0; i < a.size(); i++) {
			for (int j = 0; j < b.size(); j++) {
				AandBpermutation.push_back(a[i] + b[j]);
			}
		}

		std::sort(AandBpermutation.begin(), AandBpermutation.end());

		for (int i = 0; i < c.size(); i++) {
			for (int j = 0; j < d.size(); j++) {
				int sum = -(c[i] + d[j]);
				counter += std::upper_bound(AandBpermutation.begin(), AandBpermutation.end(), sum) - std::lower_bound(AandBpermutation.begin(), AandBpermutation.end(), sum);
			}
		}

		return counter;
	}
};

int main() {

	int n, temp;
	std::cin >> n;
	std::vector<int> a, b, c, d;
	
	Quadruplets test;

	for (int i = 0; i < n; i++) {
		std::cin >> temp;
		a.push_back(temp);
	}

	for (int i = 0; i < n; i++) {
		std::cin >> temp;
		b.push_back(temp);
	}

	for (int i = 0; i < n; i++) {
		std::cin >> temp;
		c.push_back(temp);
	}

	for (int i = 0; i < n; i++) {
		std::cin >> temp;
		d.push_back(temp);
	}
	std::cout << test.zeroQuadrupletsCount(a, b, c, d) << std::endl;
	
	return 0;
}