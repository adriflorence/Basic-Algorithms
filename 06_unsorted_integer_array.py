def get_min_max(ints):
    if len(ints) < 1:
        return -1

    smallest = ints[0]
    largest = ints[0]

    for num in ints: # O(N)
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    return (smallest, largest)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print(l)
print(get_min_max(l))
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

edge_case_1 = []
print('------')
print(edge_case_1)
print(get_min_max(edge_case_1))
print ("Pass" if (-1 == get_min_max(edge_case_1)) else "Fail")

edge_case_2 = [0, 0]
print('------')
print(edge_case_2)
print(get_min_max(edge_case_2))
print ("Pass" if ((0,0) == get_min_max(edge_case_2)) else "Fail")