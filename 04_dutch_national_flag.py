# Given an input array consisting of only 0, 1, and 2, sort the array in a single traversal.

def sort_012(input_list):

    bottom = 0                  # the top of the bottom group (Source 1)
    middle = 0                  # the top of the middle group
    top = len(input_list) - 1   # the bottom of the top group
    # Elements that are yet to be sorted fall between the middle and the top group

    # At each step, examine the element just above the middle.
    while middle <= top:
        # If it belongs in the bottom, swap it with the element just above the bottom.
        if(input_list[middle]) == 0:
            input_list[bottom], input_list[middle] = input_list[middle], input_list[bottom]
            bottom += 1
            middle += 1
        
        # If it belongs to the top group, swap it with the element just below the top.
        elif(input_list[middle] == 2):
            input_list[middle], input_list[top] = input_list[top], input_list[middle]
            top -= 1
        
        # If it is in the middle, leave it.
        else:
            middle += 1

    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

test_function([0, 1, 1])
test_function([0, 0, 0])
test_function([])


# Source 1: https://en.wikipedia.org/wiki/Dutch_national_flag_problem