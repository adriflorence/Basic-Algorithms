def recursive_binary_search(input_list, number, start, end):
    if start > end:
        return -1

    middle_index = (start + end) // 2
    middle_element = input_list[middle_index]

    if middle_element == number:
        return middle_index

    left_side = recursive_binary_search(input_list, number, start, middle_index - 1)
    right_side = recursive_binary_search(input_list, number, middle_index + 1, end)

    return max(left_side, right_side)


def rotated_array_search(input_list, number):
    end = len(input_list) - 1
    return recursive_binary_search(input_list, number, 0, end)

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

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])