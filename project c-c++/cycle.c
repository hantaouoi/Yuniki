#include <cs50.h>
#include <stdio.h>

int main(void)
{
    printf("Выбери Натуральное число: ");
    int n = get_int("");

    if (n < 0)
    {
    printf("Вы ввели отрицательное число, попробуйте снова\n");
    }
    else if (n == 0)
    {
    printf("Вы ввели ноль, попробуйте снова\n");
    }
    else
    {
    printf("Вы ввели: %i\n", n);
}
}
