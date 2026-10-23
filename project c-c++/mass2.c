#include <stdio.h>

int main (void){
	int arr[7] = {1,5,6,3,9,2,8};

	int *p = arr;

	for (int i = 0; i < 7; i++) {
		printf("%d\n", *(p + i));
	}
return 0;
}
