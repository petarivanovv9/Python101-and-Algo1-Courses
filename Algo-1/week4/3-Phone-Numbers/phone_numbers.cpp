#include <iostream>

#define MAXX 1001

using namespace std;

int graph[MAXX][MAXX] = {};
int visited[MAXX] = {};
int n;

void readGraph() {
	cin >> n;
	int* numbers = new int[n];

	for (int i = 0; i < n; i++) {
		cin >> numbers[i];
		visited[numbers[i]] = 1;
	}
	
	for (int i = 0; i < n; i++) {
		cin >> graph[numbers[i]][0];
		for (int j = 1; j <= graph[numbers[i]][0]; j++) {
			cin >> graph[numbers[i]][j];
		}
	}

	delete[] numbers;
}

void DFS(int i) {
	visited[i] = 5;
	
	for (int j = 1; j <= graph[i][0]; j++) {
		if (visited[graph[i][j]] == 1) {
			DFS(graph[i][j]);
		}
	}
}

int main() {

	readGraph();
	
	int k = 0;

	for (int i = 0; i < MAXX; i++) {
		if (visited[i] == 1) {
			k++;
			DFS(i);
		}
	}

	cout << k << '\n';

	return 0;
}