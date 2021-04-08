"""
Compare linear and binary search on ordered arrays
"""

def linear_search(ordered_array, search_value):

    """Return:
       index of search_value, number of steps taken

       If search_value is not in the array return -1 and the number of steps taken

    >>> linear_search([1, 2, 5, 7, 14], 7)
    (3, 4)
    >>> linear_search([1, 2, 5, 7, 14], 4)
    (-1, 3)
    >>> linear_search([1, 2, 5, 7, 14], 15)
    (-1, 5)
    >>> linear_search(range(0, 1000, 2) , 62)
    (31, 32)
    >>> linear_search(range(0, 1000, 2) , 761)
    (-1, 382)
    """
    checks = 0
    for idx, val in enumerate(ordered_array):
        checks += 1
        if val == search_value:
            return idx, checks
        # if we reach an element greater the then search_value
        elif val > search_value:
            break
    return -1, checks


def binary_search(ordered_array, search_value):

    """Return:
       index of search_value, number of steps taken

       If search_value is not in the array return -1 and the number of steps taken

    >>> binary_search([1, 2, 5, 6, 7, 10, 12], 10)
    (5, 2)
    >>> binary_search(range(0, 1000, 2) , 62)
    (31, 8)
    >>> binary_search(range(0, 1000, 2) , 761)
    (-1, 9)
    """
    checks = 0
    start=0
    end=len(ordered_array) - 1

    while start <= end:
        checks += 1
        val_idx = (start + end) // 2
        val_midpoint = ordered_array[val_idx]

        if search_value == val_midpoint:
            return val_idx, checks

        elif search_value < val_midpoint:
            end = val_idx - 1

        elif  search_value > val_midpoint:
            start = val_idx + 1

    return -1, checks

if __name__ == "__main__":
    import doctest
    doctest.testmod()
