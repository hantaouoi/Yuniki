#include <stdio.h>

int main(void)
{ 
	 int s;	
			printf("Выбери Натуральное число: ");
			scanf("%d", &s);

			if (s < 0)
			{
			printf("Вы ввели отрицательное число, попробуйте снова\n");
			}
			else if (s == 0)
			{
			printf("Вы ввели ноль, попробуйте снова\n");
			}
			else
			{
			printf("Вы ввели: %i\n", s);
}
}
