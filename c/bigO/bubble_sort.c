/*
 * Compare linear and binary search on ordered arrays
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

void bubble_sort(int *, size_t, int *);


int main()
{
    int i;
    int steps = 0;
    size_t array_size;
    int array[] = {7, 4, 3, 2, 1};
    array_size = sizeof(array) / sizeof(array[0]);

    /* evaluate bubble sort  */
    bubble_sort(array, array_size, &steps);

    for (i = 0; i < array_size; i++) {
        printf("%d", array[i]);
    }
        
    printf("\n");
    printf("steps: %d\n", steps);

    return 0;
}

void bubble_sort(int *array, size_t sz, int *steps){

    bool sorted = false;
    int unsorted_index = sz - 1;
    int i, tmp;

    while (!sorted){
        sorted = true;

        for (i = 0; i < unsorted_index; i++) {
            *steps += 1;
            if (array[i] > array[i+1]){
                // do the swap
                tmp = array[i];
                array[i] = array[i+1];
                array[i+1] = tmp ;
                sorted = false;
                *steps += 1;
            }
        }
     
        unsorted_index -=1;
                
    }
}
