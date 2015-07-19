#include <iostream>
#include <algorithm>
#include <vector>
#include <climits>

class BST {
public:
	// Checks if a binary tree is a binary search tree.
	bool isArrBST(int tree[100000], int root, int size, int lower = INT_MIN, int higher = INT_MAX){

		if (root >= size || tree[root] == 0) {
			return true;
		}
		if (tree[root] <= lower || tree[root] >= higher) {
			return false;
		}
		return (isArrBST(tree, root * 2 + 1, size, lower, tree[root]) && isArrBST(tree, root * 2 + 2, size, tree[root], higher));
	
	}
};

int main() {

	int n;
	std::cin >> n;

	int tree[100000];

	int number;

	for (int i = 0; i < n; i++) {
		std::cin >> number;
		tree[i] = number;
	}

	BST test;

	if (test.isArrBST(tree, 0, n)) {
		std::cout << "YES" << std::endl;
	}
	else {
		std::cout << "NO" << std::endl;
	}

	return 0;
}