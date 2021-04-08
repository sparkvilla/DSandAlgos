"""
Bubble sort implementation.

Basic sorting algorithm with a O(n^2); i.e. quadratic time complexity
"""

def bubble_sort(array):
    """
    Return a sorted array and number of steps taken (within loops only)

    >>> bubble_sort([4, 2, 7, 1, 3])
    ([1, 2, 3, 4, 7], 16)
    >>> bubble_sort([7, 4, 3, 2, 1])
    ([1, 2, 3, 4, 7], 20)
    """
    unsorted_until_index = len(array) -1
    sorted_ = False
    steps = 0

    while not sorted_:
        sorted_ = True

        # this is a pass-through
        for i in range(unsorted_until_index):
            steps += 1 # count number of comparisons
            if array[i] > array[i+1]:
                array[i], array [i+1] = array[i+1], array[i]
                steps += 1 # count number of swaps
                sorted_ = False

        unsorted_until_index -= 1

    return array, steps


if __name__ == "__main__":
    import doctest
    doctest.testmod()
