#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


typedef struct
{
    int *p;
    bool isMalloc;
} outForm;


outForm mergeSort(int len, int arr[]);
void merge(int len, outForm output, outForm mergedFirst, outForm mergedSecond);
void printList(int length, int list[]);



int main(void)
{
    int input[10] = {4, 5, 2, 7, 9, 3, 1, 6, 10, 8};

    printf("Input : ");
    printList(10, input);

    outForm output = mergeSort(10, input);
    free(output.p);
}



outForm mergeSort(int len, int arr[])
{
    int halfLen = len/2;

    if ( len <= 1)
    {
        outForm new = {arr, false};
        return new;
    }

    // 절반 나누기
    int frontHalf[halfLen], rearHalf[len - halfLen];

    for (int i = 0; i < len; i++)
    {
        if (i < halfLen)
        {
            frontHalf[i] = arr[i];
        }
        else
        {
            rearHalf[i - halfLen] = arr[i];
        }
    }

    outForm output;
    output.p = malloc(sizeof(int) * len);
    output.isMalloc = true;

    outForm mergedFirst = mergeSort(halfLen, frontHalf);
    outForm mergedSecond = mergeSort(len - halfLen, rearHalf);

    merge(len, output, mergedFirst, mergedSecond);

    if (mergedFirst.isMalloc){
        free(mergedFirst.p);
    }
    if (mergedSecond.isMalloc){
        free(mergedSecond.p);
    }
    return output;
}


void merge(int len, outForm output, outForm mergedFirst, outForm mergedSecond)
{
    int firstH = 0, secondH = 0;

    for (int i = 0; i < len; i++)
    {
        if (firstH == len/2)
        {
            output.p[i] = mergedSecond.p[secondH];
            secondH++;
            continue;
        }

        if (secondH == len - len/2)
        {
            output.p[i] = mergedFirst.p[firstH];
            firstH++;
            continue;
        }

        if (mergedFirst.p[firstH] < mergedSecond.p[secondH])
        {
            output.p[i] = mergedFirst.p[firstH];
            firstH++;
        }
        else
        {
            output.p[i] = mergedSecond.p[secondH];
            secondH++;
        }
    }

    printf("Merged : ");
    printList(len, output.p);
}


void printList(int length, int list[])
{
    for (int i = 0; i < length; i++)
    {
        printf("%i ", list[i]);
    }
    printf("\n");
}