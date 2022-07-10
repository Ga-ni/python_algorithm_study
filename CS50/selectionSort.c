#include <stdio.h>

const int LIST_SIZE = 10;

int* selectionSort(int list[]);
void printList(int list[]);

int main(void)
{
    int list[10] = {4, 5, 2, 7, 9, 3, 1, 6, 10, 8};
    int *sorted;

    printf("Before sorting : ");
    printList(list);

    sorted = selectionSort(list);

    printf("After sorting : ");
    printList(list);
}


int* selectionSort(int list[])
{
    for (int i = 0; i < LIST_SIZE; i++)
    {
        int min = list[i];
        int minIdx = i;

        for (int j = 0 + i; j < LIST_SIZE; j++)
        {
            if (min > list[j])
            {
                min = list[j];
                minIdx = j;
            }
        }

        int tmp = list[i];
        list[i] = min;
        list[minIdx] = tmp;

        printf("Step %d : ", i);
        printList(list);
    }
    return list;
}


void printList(int list[])
{
    for (int i = 0; i < LIST_SIZE; i++)
    {
        printf("%i ", list[i]);
    }
    printf("\n");
}