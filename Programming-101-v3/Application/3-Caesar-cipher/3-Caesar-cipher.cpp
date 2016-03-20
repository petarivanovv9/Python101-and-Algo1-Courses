#include <iostream>
#include <cstring>

using namespace std;

char* caesar_encrypt(char *str, int n);
char modifyLetter(char c, int n);

const int MAX_SIZE = 50;

int main() {

	char str[MAX_SIZE];
	cout << "Enter a string: ";
	cin.getline(str, MAX_SIZE);

	int n = 0;
	cout << "Enter n: ";
	cin >> n;

	char *pStr = str;

	cout << "The result is: " << caesar_encrypt(pStr, n) << endl;

	return 0;
}

char* caesar_encrypt(char *str, int n) {
	
	int sizeStr = strlen(str);
	str[sizeStr] = '\0';

	for (int i = 0; i < sizeStr; i++){
		str[i] = modifyLetter(str[i], n);
	}

	return str;
}

char modifyLetter(char c, int n) {

	if (!isalpha(c)) {
		return c;
	}

	while (n != 0) {
		if (c == 'z') {
			c = 'a';
		}
		else if (c == 'Z') {
			c = 'A';
		}
		else {
			c += 1;
		}
		n--;
	}

	return c;	
}