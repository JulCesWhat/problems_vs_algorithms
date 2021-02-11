

def rotated_array_search(input_list, num):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if input_list is None or len(input_list) is 0:
        return []

    return search(input_list, num, 0, len(input_list) - 1)


def search(input_list, number, low, high):
    mid = (low + high) // 2

    if low > high:
        return - 1

    if input_list[mid] is number:
        return mid

    if input_list[low] <= input_list[mid]:
        if input_list[low] <= number <= input_list[mid]:
            return search(input_list, number, low, mid - 1)
        else:
            return search(input_list, number, mid + 1, high)
    else:
        if input_list[mid] <= number <= input_list[high]:
            return search(input_list, number, mid + 1, high)
        else:
            return search(input_list, number, low, mid - 1)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_1 = [6, 7, 8, 9, 10, 1, 2, 3, 4]
print(rotated_array_search(test_1, 8))
# 2

test_2 = [6, 7, 8, 1, 2, 3, 4]
print(rotated_array_search(test_2, 10))
# -1

test_3 = []
print(rotated_array_search(test_3, 6))
# -1

test_4 = None
print(rotated_array_search(test_4, 6))
# None
