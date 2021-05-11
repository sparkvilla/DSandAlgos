import pdb

"""
Different implementations of the has_dupl_val algos

Compare time complexity of the different versions

has_dupl_val1 -> O(n^2)
has_dupl_val2 -> O(n)
"""

def has_dupl_val1(array):
    """
    Return (True, steps taken) if a duplicate value was found in the array
    else (False, steps taken)

    >>> has_dupl_val1([1, 2, 3, 1, 9])
    (True, 4)
    >>> has_dupl_val1([1, 2, 3, 4, 9])
    (False, 25)
    >>> has_dupl_val1(range(10))
    (False, 100)
    >>> has_dupl_val1(range(100))
    (False, 10000)
    >>> has_dupl_val1(range(1000))
    (False, 1000000)
    """
    steps = 0
    for idx_v1, val1 in enumerate(array):
        for idx_v2, val2 in enumerate(array):
            steps += 1
            if idx_v1 != idx_v2:
                if val1 == val2:
                    return True, steps
    return False, steps


def has_dupl_val2(array):
    """
    Return (True, steps taken) if a duplicate value was found in the array
    else (False, steps taken)

    >>> has_dupl_val2([1, 2, 3, 1, 9])
    (True, 4)
    >>> has_dupl_val2([1, 2, 3, 4, 9])
    (False, 5)
    >>> has_dupl_val2(range(10))
    (False, 10)
    >>> has_dupl_val2(range(100))
    (False, 100)
    >>> has_dupl_val2(range(1000))
    (False, 1000)
    """
    steps = 0
    index = {}
    for val in array:
        steps += 1
        if index.get(val):
            return True, steps
        else:
            index[val] = True
    return False, steps


if __name__ == "__main__":
    import doctest
    doctest.testmod()
