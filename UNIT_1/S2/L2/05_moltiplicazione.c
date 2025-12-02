#include <stdio.h>

int main()
{
    int a , b , moltiplicazione;

    printf("inserisci il primo numero\n");
    scanf("%d" , &a);

    printf("inserisci il secondo numero\n");
    scanf("%d" , &b);

    moltiplicazione = a * b;

    printf("la moltiplicazione e': %d" , moltiplicazione);

    return 0;
}