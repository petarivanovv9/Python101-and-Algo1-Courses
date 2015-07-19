#include <iostream>


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