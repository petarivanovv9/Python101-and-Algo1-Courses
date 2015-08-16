#include <iostream>
#include <vector>
#include <queue>
#include <set>

using namespace std;

int n, startingPoint;

class Node {
public:
	bool visited;
	bool isCoffeeStore;
	int BFSLevel;
	vector<Node*> connections;

	Node() {
		this->visited = false;
		this->isCoffeeStore = false;
		this->BFSLevel = 0;
	}
};

void readGraph(vector<Node> &graph) {
	int temp;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> temp;
			if (temp == true) {
				graph[i].connections.push_back(&graph[j]);
			}
		}
	}

	cin >> startingPoint;

	for (int i = 0; i < n; i++) {
		cin >> graph[i].isCoffeeStore;
	}

}

queue<Node*> BFSQueue;

int getClosestCoffeeStore(Node* node) {
	node->visited = true;

	if (node->isCoffeeStore) {
		return 0;
	}

	BFSQueue.push(node);

	while (!BFSQueue.empty()) {
		for (unsigned int i = 0; i < node->connections.size(); i++) {
			if (node->connections[i]->isCoffeeStore == true) {
				return node->BFSLevel + 1;
			}
			if (node->connections[i]->visited == false) {
				node->connections[i]->BFSLevel = node->BFSLevel + 1;
				node->connections[i]->visited = true;
				BFSQueue.push(node->connections[i]);
			}
		}

		BFSQueue.pop();
		node = BFSQueue.front();
	}

	return -1;
}

int main() {

	cin.sync_with_stdio(false);
	cin.tie(0);

	cin >> n;
	vector<Node> graph(n);

	readGraph(graph);

	cout << getClosestCoffeeStore(&graph[startingPoint]) << endl;

	return 0;
}