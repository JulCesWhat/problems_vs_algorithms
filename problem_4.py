

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    start_pos = 0
    end_pos = len(input_list) - 1

    front_in = 0

    while front_in <= end_pos:
        if input_list[front_in] == 0:
            input_list[front_in] = input_list[start_pos]
            input_list[start_pos] = 0
            start_pos += 1
            front_in += 1
        elif input_list[front_in] == 2:
            input_list[front_in] = input_list[end_pos]
            input_list[end_pos] = 2
            end_pos -= 1
        else:
            front_in += 1

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_1 = []
print(sort_012(test_1))
# []

test_2 = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
print(sort_012(test_2))
# [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]

test_3 = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
print(sort_012(test_3))
# [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
