#include <iostream>


class Node {
public:
	int value;
	Node* left;
	Node* right;
};

class BST {
public:

	// Checks if a binary tree is a binary search tree.
	bool isBST(Node* root) {
		
		if (root->value > (root->left)->value && root->value < (root->right)->value && root->right != 0 && root->left != 0) {
			return (isBST(root->left) && isBST(root->right));
		}
		else if (root->left == 0 && root->value < (root->right)->value) {
			return isBST(root->right);
		}
		else if (root->right == 0 && root->value > (root->left)->value) {
			return isBST(root->left);
		}
		else if (root->left == 0 && root->right == 0) {
			return true;
		}
		else {
			return false;
		}

	}
};

//int main() {
//
//
//	return 0;
//}