#include <iostream>

#include "Vector.h"
#include "Queue.h"
#include "Stack.h"

#include <time.h>

int main() {

	clock_t beg = clock();

	Vector pesho;
	pesho.add(5);
	pesho.add(2);
	pesho.add(8);
	pesho.add(16);

	pesho.insert(1, 10);
	pesho.add(33);

	pesho.printVector();
	pesho.insert(2, 10);

	std::cout << "pesho at(2): " << pesho.get(2) << std::endl;
	pesho.remove(2);
	pesho.printVector();
	pesho.pop();
	pesho.printVector();

	//for (int i = 0; i < 60000; i++) {
	//	pesho.insert(0, 9);
	//}
	//clock_t end = clock();
	//std::cout << double(end - beg) / CLOCKS_PER_SEC << std::endl;
	pesho.printVector();
	std::cout << "size of the Vector: " << pesho.getSize() << std::endl;
	std::cout << "capacity of the Vector: " << pesho.getCapacity() << std::endl;

	std::cout << "----------------------------------------" << std::endl;

	Queue pencho;
	pencho.push(1);
	pencho.push(3);
	pencho.push(5);
	pencho.push(7);

	int firstElement = pencho.pop();
	std::cout << "firstElement: " << firstElement << std::endl;
	firstElement = pencho.peek();
	std::cout << "firstElement: " << firstElement << std::endl;

	std::cout << "size of the Queue: " << pencho.getSize() << std::endl;
	pencho.printQueue();

	std::cout << "----------------------------------------" << std::endl;

	Stack pepi;
	pepi.push(1);
	pepi.push(3);
	pepi.push(5);
	pepi.push(7);

	firstElement = pepi.pop();
	std::cout << "firstElement: " << firstElement << std::endl;
	firstElement = pepi.peek();
	std::cout << "firstElement: " << firstElement << std::endl;

	std::cout << "size of the Queue: " << pepi.getSize() << std::endl;
	pepi.printQueue();

	std::cout << "----------------------------------------" << std::endl;


	return 0;
}