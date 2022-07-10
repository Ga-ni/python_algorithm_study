#include <stdio.h>

const int LIST_SIZE = 10;

int* bubbleSort(int list[]);
void printList(int arr[]);


int main(void)
{
    int list[10] = {4, 5, 2, 7, 9, 3, 1, 6, 8, 10};
    int *sorted;

    printf("Before sorting : ");
    printList(list);

    sorted = bubbleSort(list);

    printf("After sorting : ");
    printList(list);
}



int* bubbleSort(int list[])
{
    for (int i = 0; i < LIST_SIZE; i++ )
    {
        int changeCnt = 0;

        for (int j = 0; j < LIST_SIZE - 1 - i; j++)
        {
            if (list[j] > list[j+1])
            {
                int tmp = list[j];
                list[j] = list[j+1];
                list[j+1] = tmp;
                changeCnt++;
            }
        }
        printf("Step %d : ", i + 1);
        printList(list);

        if (changeCnt == 0)
        {
            break;
        }
    }
    return list;
}


void printList(int arr[])
{
    for (int i = 0; i < LIST_SIZE; i++)
    {
        printf("%i ", arr[i]);
    }
    printf("\n");
}