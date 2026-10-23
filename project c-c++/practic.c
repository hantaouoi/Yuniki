#include <stdio.h>

int main(void){
	int arr[] = {8,-2,0,5,45};

	printf("Массив:");

	for (int i = 0; i < 5; i++) {
		printf("%d ", arr[i]);
	}

	int min = arr[0];

	for (int i = 0; i < 5; i++) {
		if (arr[i] < min) {
			min = arr[i];
		}
	}

	printf("Минимум: %d\n", min);

	return 0;
}
