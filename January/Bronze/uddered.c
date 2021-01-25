#include <stdio.h>
#include <string.h>

int findIndex(const char abc[], char letter) {
	int i;
	// DEBUG
	// printf("%s\n", abc);
	// printf("%c\n", letter[0]);
	for (i = 0; i < 26; i++) {
		if (abc[i] == letter) {
			break;
		}
	}
	// DEBUG
	// printf("%d\n", r);
	// printf("%d\n", i);
	return i;
}

int main() {
	char order[26];
	char heard[1000];
	int Ind1, Ind2, i, count = 0;

	scanf("%s", &order);
	// DEBUG
	// printf("%s\n", order);
	scanf("%s", &heard);
	
	Ind1 = findIndex(order, heard[0]);
	for (i = 1; i < strlen(heard); i++) {
		Ind2 = findIndex(order, heard[i]);
		// printf("Ind1 = %d\nInd2 = %d\n", Ind1, Ind2);
		if (Ind2 <= Ind1) 
			count++;
		Ind1 = Ind2;
	}
	count++;
	printf("%d", count);
}

