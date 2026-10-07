#include <stdio.h>

int main(void)
{
    int s;
    {
        printf("Введите число: ");
    }
    scanf("%d", &s);
    if (s <= 0)
    {
        printf("Вы ввели отрицательное число или ноль\n");
    }
    else
    {
        printf("Вы ввели: %d\n", s);
    }
}