/*
 * Compare linear and binary search on ordered arrays
 */

#include <stdio.h>
#include <stdlib.h>

int linear_search(int *, size_t, int, int *);
int binary_search(int *, size_t, int, int *);


int main()
{

    int steps = 0;
    int value = 101;
    size_t array_size;
    int array[] = {1, 2, 4, 5, 8, 9, 20, 22, 24, 28, 30, 32, 34, 40, 42, 50, 52,
                   60, 80, 90, 92, 94, 96, 100};
    array_size = sizeof(array) / sizeof(array[0]);

    /* evaluate linear search  */
    int result = linear_search(array, array_size, value, &steps);
    printf("value: %d, steps: %d\n", result, steps);

    /* reset steps to zero to evaluate binary search  */
    steps = 0;

    /* evaluate linear search  */
    result = binary_search(array, array_size, value, &steps);
    printf("value: %d, steps: %d\n", result, steps);

    return 0;
}

int linear_search(int *ordered_array, size_t sz, int search_value, int *steps){

    int i;
    for (i = 0; i < sz; i++) {
        *steps += 1;
        if (search_value == ordered_array[i])
            return i;
        else if (search_value < ordered_array[i])
            break;
    }
    return -1;
}


int binary_search(int *ordered_array, size_t sz, int search_value, int *steps){

    int start = 0;
    int end = sz-1;

    while (start < end){
        *steps += 1;

        int midpoint = (start + end) / 2;

        if (search_value == ordered_array[midpoint])
            return midpoint;
        else if (search_value > ordered_array[midpoint])
            start = midpoint + 1;
        else if (search_value < ordered_array[midpoint])
            end = midpoint - 1;
    }

    return -1;
}
