# Merge Sort is a Divide and Conquer algorithm.
# It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves.


# implements merge sort to sort array
def rearrange_digits(input_list):
    if len(input_list) <= 1:
        return input_list

    middle = len(input_list) // 2
    left = rearrange_digits(input_list[:middle])
    right = rearrange_digits(input_list[middle:])

    return compare(left, right)

def compare(left, right):
    result = []
    left_index = 0
    right_index = 0

    # iterate and compare left to right
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    
    # add any remaining items from the left array
    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1

    # add any remaining items form the right array
    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1

    # merged and sorted array
    return result

# TEST

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

print(rearrange_digits([4, 6, 2, 5, 9, 8]))

# test_function([[1, 2, 3, 4, 5], [542, 31]])
# test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]