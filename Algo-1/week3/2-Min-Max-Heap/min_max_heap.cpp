#include <iostream>
#include <vector>

using namespace std;

int n;

class Node {
public:
	int value;
	Node* left;
	Node* right;

	Node(int value, Node* left, Node* right) {
		this->value = value;
		this->left = left;
		this->right = right;
	}
};

class MinMaxHeap {
public:

	// Checks if a binary tree is a min/max heap.
	bool isMinMax(Node* root) {
		
		bool isLeftPartOK = true;
		bool isRightPartOK = true;
		static int level = 1;
		bool isOdd = level % 2;

		if (root->left != NULL) {
			if ((isOdd && (root->left)->value > root->value) || (!isOdd && (root->left)->value < root->value)) {
				level++;
				isLeftPartOK = isMinMax(root->left);
			}
			else {
				level--;
				return false;
			}
		}
		
		if (root->right != NULL) {
			if ( (isOdd && (root->right)->value > root->value) || (!isOdd && (root->right)->value < root->value)) {
				level++;
				isRightPartOK = isMinMax(root->right);
			}
			else {
				level--;
				return false;
			}
		}

		level--;
		
		return isLeftPartOK && isRightPartOK;
	}
};

int main() {

	MinMaxHeap test;

	cin >> n;

	if (n <= 0) {
		return 0;
	}
	else if (n == 1) {
		cout << "YES" << '\n';
		return 0;
	}

	int current;
	cin >> current;

	Node* Root = new Node(current, NULL, NULL);
	Node** Arr = new Node*[n];
	Arr[0] = Root;
	int currentIndex = 0;
	Node* CurrentParent = Arr[currentIndex++];

	for (int i = 1; i < n; i++) {
		cin >> current;

		Arr[i] = new Node(current, NULL, NULL);

		if (CurrentParent->left == NULL) {
			CurrentParent->left = Arr[i];
		}
		else if (CurrentParent->right == NULL) {
			CurrentParent->right = Arr[i];
		}
		else {
			CurrentParent = Arr[currentIndex++];
			CurrentParent->left = Arr[i];
		}

	}

	if (test.isMinMax(Root)) {
		cout << "YES" << '\n';
	}
	else {
		cout << "NO" << '\n';
	}

	delete[] Arr;

	return 0;
}



//int main() {
//
//	Node node1(1, NULL, NULL);
//	Node node2(1, NULL, NULL);
//	Node node3(1, NULL, NULL);
//	Node node4(1, NULL, NULL);
//	Node node5(9, &node1, &node2);
//	Node node6(9, &node3, &node4);
//	Node node7(6, &node5, &node6);
//	
//	MinMaxHeap test;
//
//	if (test.isMinMax(&node7)) {
//		std::cout << "Yes" << std::endl;
//	}
//	else {
//		std::cout << "No" << std::endl;
//	}
//
//	return 0;
//}