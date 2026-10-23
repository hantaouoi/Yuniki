//не закончина нету вывода только считает макс число 
int accounts[] = {5,2,6,8};
int main (void){
int maximumWealth(int** accounts, int accountSize, int* accountColSize){
	int maxWealth = 0;

	for(int i = 0; i < accountSize;i++){
		int sum  = 0;
		
		for (int j = 0;j < accountColSize[i]; i++){
			sum = sum +accounts[i][i];
	}

	if (sum > maxWealth){
		maxWealth = sum;
	}
	}
	return maxWealth;
}
}
