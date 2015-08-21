#include <iostream>
#include <vector>
#include <algorithm>

#define INF 2147483647

using namespace std;

class Node {
public:
	int value;
	Node* next;

	Node(int val = 0, Node* nxt = NULL)
		: value(val), next(nxt) {
	};
};


class KLists {
public:
	void makeHeap(Node** sequence, int size) {
		for (int i = size / 2 - 1; i >= 0; i--) {
			heapify(sequence, size, i);
		}
	}

	void heapify(Node** sequence, int size, int i) {
		int a;
		int b;

		while (i * 2 + 1 < size) {
			
			if (i * 2 + 1 < size) {
				a = sequence[i * 2 + 1]->value;
			}
			if (i * 2 + 2 < size) {
				b = sequence[i * 2 + 2]->value;
			}
			else {
				b = INF;
			}

			int minIndx = a < b ? i * 2 + 1 : i * 2 + 2;

			if (sequence[minIndx]->value < sequence[i]->value) {
				swap(sequence[minIndx], sequence[i]);
				i = minIndx;
			}
			else {
				return;
			}

		}
	}

	// Merge K sorted lists
	Node merge(vector<Node>& lists) {
		Node** heap = new Node*[lists.size()];
		Node* begin;
		Node* currentNode;

		for (int i = 0; i < lists.size(); i++) {
			heap[i] = &lists[i];
		}

		makeHeap(heap, lists.size());
		currentNode = begin = heap[0];

		int hasMore = lists.size();

		if (heap[0]->next != NULL) {
			heap[0] = heap[0]->next;
		}
		else {
			hasMore--;
			swap(heap[0], heap[hasMore]);
		}
		
		while (hasMore) {
			heapify(heap, hasMore, 0);
			currentNode->next = heap[0];
			currentNode = heap[0];
			
			if (heap[0]->next != NULL) {
				heap[0] = heap[0]->next;
			}
			else {
				hasMore--;
				swap(heap[0], heap[hasMore]);
			}
		}
		
		currentNode->next = NULL;
		
		return *begin;

	}

};


int main() {

	cin.sync_with_stdio(false);
	cin.tie(0);

	int k;
	cin >> k;

	vector<Node> lists;

	for (int i = 0; i < k; i++) {
		int temp = 0;

		Node* previous;
		
		cin >> temp;

		Node beginning(temp, NULL);
		previous = &beginning;

		Node current;

		while (cin >> temp && temp != -1) {
			Node* current = new Node(temp, NULL);
			previous->next = current;
			previous = current;
		}

		lists.push_back(beginning);
	}
	
	KLists test;
	Node node = test.merge(lists);
	Node* n = &node;

	while (n != NULL) {
		cout << n->value << " ";
		n = n->next;
	}

	return 0;
}