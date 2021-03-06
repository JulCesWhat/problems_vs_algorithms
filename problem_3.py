
def merge_sort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sorted_input_list = merge_sort(input_list)

    first_num = 0
    sec_num = 0

    for i in range(len(sorted_input_list) - 1, -1, -1):
        if i % 2 is 0:
            first_num = (first_num * 10) + sorted_input_list[i]
        else:
            sec_num = (sec_num * 10) + sorted_input_list[i]

    return [first_num, sec_num]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_1 = rearrange_digits([1, 2, 3, 4, 5])
print(test_1)
# [531, 42]

test_2 = rearrange_digits([5])
print(test_2)
# [5, 0]

test_3 = rearrange_digits([])
print(test_3)
# [0, 0]
