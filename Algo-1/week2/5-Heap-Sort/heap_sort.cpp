#include <iostream>

class HeapSort {
public:
	void sort(int*, int);
private:
	//void heapify(int*, int);
	//void swap(int, int, int*);
	void sift(int*, int, int);
};

void HeapSort::sort(int* sequence, int size) {

	int i = size / 2;

	while (i--) {
		sift(sequence, i, size);
	}

	i = size;

	while (--i) {
		std::swap(sequence[0], sequence[i]);
		sift(sequence, 0, i);
	}
}

void HeapSort::sift(int* pArr, int pos, int size) {
	
	// Âçèìàìå åëåìåíòà, êîéòî òðÿáâà äà ñå ïîçèöèîíèðà
	int elem = pArr[pos];

	int ni = pos; // èíäåêñ íà òåêóù âúçåë
	int si = pos * 2 + 1; // èíäåêñ íà òåêóù íàñëåäíèê

	while (si < size) {

		// â ìîìåíòà succ å èíäåêñúò íà ëåâèÿ íàñëåäíèê.
		// àêî èìà äåñåí íàñëåäíèê è òîé å ïî-ãîëÿì,
		// òðÿáâà äà ïðåìåñòèì succ
		if (si < size - 1 && pArr[si] < pArr[si + 1]) {
			si++;
		}

		// Âå÷å succ e ïîçèöèÿòà íà ïî-ãîëåìèÿ îò äâàòà íàñëåäíèêà

		// Àêî åëåìåíòúò, êîéòî ìåñòèì å ïî-ãîëÿì îò ïî-ãîëåìèÿ íàñëåäíèê,
		// ïðèêëþ÷âàìå ðàáîòàòà
		if (elem > pArr[si]) {
			break;
		}

		pArr[ni] = pArr[si];
		ni = si;
		si = si * 2 + 1;
	}

	pArr[ni] = elem;
}

int main() {

	int sizeArr;
	//std::cout << "sizeArr: ";
	std::cin >> sizeArr;

	int* arr = new (std::nothrow) int[sizeArr];

	for (int i = 0; i < sizeArr; i++) {
		std::cin >> arr[i];
	}

	HeapSort test;

	test.sort(arr, sizeArr);

	//std::cout << "result:" << std::endl;
	for (int i = 0; i < sizeArr; i++) {
		//std::cout << arr[i] << " ";
		std::cout << arr[i];
	}
	//std::cout << std::endl;

	return 0;

}
