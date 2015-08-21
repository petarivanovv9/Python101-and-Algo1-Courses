#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

class Contact {
public:
	string name;
	int number;
	
	Contact(int number, string name) {
		this->name = name;
		this->number = number;
	}
};

class Node {
public:
	Contact contact;
	Node* left;
	Node* right;

	Node(Contact c, Node* l, Node* r) :
		contact(c), left(l), right(r) {
	};
};

class PhoneBook {
private:
	Node* beginning;
public:
	PhoneBook() : beginning(NULL) {
	};

	//inserts a new contact
	void insert(Contact contact) {
		Node* currentNode = beginning;
		Node* parent = NULL;

		while (currentNode != NULL) {
			if (currentNode->contact.name == contact.name) {
				currentNode->contact.number = contact.number;
				return;
			}
			else if (currentNode->contact.name > contact.name) {
				parent = currentNode;
				currentNode = currentNode->left;
			}
			else if (currentNode->contact.name < contact.name) {
				parent = currentNode;
				currentNode = currentNode->right;
			}
		}

		if (beginning != NULL) {
			if (contact.name < parent->contact.name) {
				parent->left = new Node(contact, NULL, NULL);
			}
			else {
				parent->right = new Node(contact, NULL, NULL);
			}
		}
		else {
			beginning = new Node(contact, NULL, NULL);
		}

	}

	//lookup a name and print its phone number
	void lookup(std::string name){
		Node* currentNode = beginning;

		if (currentNode == NULL) {
			cout << "NOT FOUND!" << "\n";
			return;
		}

		while (currentNode->contact.name != name) {
			if (name > currentNode->contact.name) {
				if (currentNode->right == NULL) {
					cout << "NOT FOUND!" << "\n";
					return;
				}
				currentNode = currentNode->right;
			}
			else {
				if (currentNode->left == NULL) {
					cout << "NOT FOUND!" << "\n";
					return;
				}
				currentNode = currentNode->left;
			}
		}

		cout << currentNode->contact.number << "\n";
	}

	//list all records in an alphabetical order
	void list() {
		showContacts(beginning);
	}

	void showContacts(Node* node) {
		if (node == NULL) {
			return;
		}
		showContacts(node->left);
		cout << node->contact.name << " " << node->contact.number << "\n";
		showContacts(node->right);
	}


	//remove a record for a given name
	void remove(std::string name) {
		if (beginning == NULL) {
			return;
		}

		Node* toRemove = beginning;
		Node* parent = NULL;

		while (toRemove->contact.name != name) {
			parent = toRemove;

			if (name > toRemove->contact.name) {
				if (toRemove->right == NULL) {
					return;
				}
				toRemove = toRemove->right;
			}
			else {
				if (toRemove->left == NULL) {
					return;
				}
				toRemove = toRemove->left;
			}
		}

		if (toRemove->right != NULL) {
			parent = toRemove;
			Node* leftMost = toRemove->right;

			while (leftMost->left != NULL) {
				parent = leftMost;
				leftMost = leftMost->left;
			}

			toRemove->contact = leftMost->contact;

			if (parent->right == leftMost) {
				parent->right = leftMost->right;
			}
			else {
				parent->left = leftMost->right;
			}
		}
		else {
			if (toRemove == beginning) {
				beginning = beginning->left;
				return;
			}
			if (parent->contact.name < toRemove->contact.name) {
				parent->right = toRemove->left;
			}
			else {
				parent->left = toRemove->left;
			}
		}

	}
};


int main() {

	cin.sync_with_stdio(false);
	cin.tie(0);

	int n;
	int number;

	std::string command, name;

	PhoneBook test;

	std::cin >> n;

	while (n--) {

		std::cin >> command;

		if (command == "insert") {
			std::cin >> number;
			std::cin >> name;
			test.insert(Contact(number, name));
		}
		else if (command == "lookup") {
			std::cin >> name;
			test.lookup(name);
		}
		else if (command == "list") {
			test.list();
		}
		else if (command == "remove") {
			std::cin >> name;
			test.remove(name);
		}
	}

	return 0;
}