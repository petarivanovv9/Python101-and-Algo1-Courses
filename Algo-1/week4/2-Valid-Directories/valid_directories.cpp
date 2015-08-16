#include <iostream>
#include <vector>
#include <queue>

#define MAXX 1001

using namespace std;

int graph[MAXX][MAXX] = {};
int visited[MAXX] = {};
int n;

void readGraph() {
	cin >> n;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> graph[i][j];
		}
	}
}

class ValidDirectories {
public:
	bool DFS(int i, int size) {
		
		if (visited[i] == 2) {
			return false;
		}
		
		visited[i] = 2;
		
		for (int j = 0; j < size; j++) {
			if (graph[i][j] == 1 && visited[j] != 1) {
				if (DFS(j, size) == false) {
					return false;
				}
			}
		}

		visited[i] = 1;
		
		return true;
	}

	bool isValid() {
		return DFS(0, n);
	}
};

int main() {

	ValidDirectories test;
	readGraph();

	if (test.isValid() == true) {
		cout << "true" << endl;
	}
	else {
		cout << "false" << endl;
	}

	return 0;
}