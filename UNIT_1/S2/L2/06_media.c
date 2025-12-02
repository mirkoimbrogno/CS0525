#include <stdio.h>

int main()
{
    int num1 , num2 , med;

    printf("inserisci il primo numero:\n");
    scanf("%d" , &num1);

    printf("inserisci il secondo numero\n");
    scanf("%d" , &num2);

    med = (num1 + num2)/2;

    printf("la media aritmetica e': %d", med);

    return 0;
}