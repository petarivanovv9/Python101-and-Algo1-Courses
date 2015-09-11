#include <iostream>
#include <climits>
#include <cstring>
#include <string>
#include <stdio.h>

using namespace std;

class RMQ {
public:
	int size;
	int* tree;

	RMQ(int size) {
		int k = 1;
		// get the biggest power of two, greater or euql to size
		while (k < size) { 
			k *= 2;
		}

		this->size = k;
		k *= 2;
		tree = new int[k];
		for (int i = 0; i < k; i++) {
			tree[i] = INT_MAX;
		}
	}

	~RMQ() {
		//delete[] tree;
	}

	// sets the value at index
	void set(int index, int value) {
		index += size;
		tree[index] = value;
		index /= 2;

		while (index > 0) {
			int leftChild = index * 2;
			int rightChild = index * 2 + 1;

			tree[index] = (tree[leftChild] > tree[rightChild] ? tree[rightChild] : tree[leftChild]);
		
			index /= 2;
		}
	}

	// returns the minimum value in a range
	int min(int startIndex, int endIndex) {
		startIndex += size;
		endIndex += size;

		int min = INT_MAX;

		if (endIndex == startIndex) {
			return min > tree[endIndex] ? tree[endIndex] : min;
		}

		while (endIndex > startIndex) {
			if (endIndex % 2 == 0) {
				min = (min > tree[endIndex] ? tree[endIndex] : min);
				endIndex /= 2;
				endIndex--;
			}
			else {
				endIndex /= 2;
				min = (min > tree[endIndex] ? tree[endIndex] : min);
			}

			if (startIndex % 2) {
				min = (min > tree[startIndex] ? tree[startIndex] : min);
				startIndex /= 2;
				startIndex++;

				if (startIndex == endIndex) {
					min = (min > tree[startIndex] ? tree[startIndex] : min);
					break;
				}
			}
			else {
				startIndex /= 2;
				min = (min > tree[startIndex] ? tree[startIndex] : min);
			}

		}

		return min;
	}

};

int main() {
	int n,q;
  	scanf("%d%d",&n,&q);

  	RMQ rmq(n);

  	for(int i=0;i<n;i++) {
    		int temp;
    		scanf("%d",&temp);
    		rmq.set(i,temp);
  	}

  	for(int i=0;i<q;i++) {
    		char s[3];
    		int a,b;
    		scanf("%s%d%d",s,&a,&b);
    		if (strcmp(s,"min")==0) // if s is "min"
      			printf("%d\n",rmq.min(a,b));
    		else {
      			rmq.set(a,b);
    		}		
  	}

  	return 0;
}
