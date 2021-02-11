import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    if len(ints) == 2:
        return ints[0], ints[1]
    elif len(ints) == 1:
        return ints[0], ints[0]
    elif len(ints) < 1:
        return -1, -1

    min_val = None
    max_val = None

    for num in ints:
        if min_val is None or num < min_val:
            if min_val is not None and (max_val is None or min_val > max_val):
                max_val = min_val
            min_val = num
        elif max_val is None or num > max_val:
            if max_val is not None and (min_val is None or max_val < min_val):
                min_val = max_val
            max_val = num
    return min_val, max_val


# Example Test Case of Ten Integers

l = [i for i in range(0, 10)]  # a list containing 0 - 9

random.shuffle(l)
test_1 = get_min_max(l)
print(test_1)
# (0, 9)

random.shuffle(l)
test_1 = get_min_max([1])
print(test_1)
# (1, 1)

random.shuffle(l)
test_1 = get_min_max([])
print(test_1)
# (-1, -1)
