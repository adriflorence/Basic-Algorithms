# Find the square root of the integer without using any Python library. You have to find the floor value of the square root.
# For example if the given number is 16, then the answer would be 4.
# If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.
# The expected time complexity is O(log(n))

def sqrt(number):

    if number < 0:
        return None

    if (number == 0) or (number == 1):
        return number

    start = 0
    end = number // 2

    while start <= end:
        middle = (start + end) // 2
        # print(start, middle, end, number)
        if middle * middle == number:
            return middle

        elif middle * middle < number:
            start = middle + 1
            result = middle
        else:
            end = middle - 1
    
    return result


print("basic tests")
print("Pass" if  (3 == sqrt(9)) else "Fail") # Pass
print("Pass" if  (0 == sqrt(0)) else "Fail") # Pass
print("Pass" if  (1 == sqrt(1)) else "Fail") # Pass
print("Pass" if  (5 == sqrt(27)) else "Fail") # Pass
print("Pass" if (None == sqrt(-1)) else "Fail") # Pass

print("------")
print("squares of 3:")
print("Pass" if  (3 == sqrt(10)) else "Fail") # Pass
# print("Pass" if  (3 == sqrt(11)) else "Fail") # Pass
# print("Pass" if  (3 == sqrt(12)) else "Fail") # Pass
# print("Pass" if  (3 == sqrt(13)) else "Fail") # Pass
# print("Pass" if  (3 == sqrt(14)) else "Fail") # Pass
# print("Pass" if  (3 == sqrt(15)) else "Fail") # Pass
# print("Pass" if  (3 == sqrt(16)) else "Fail") # Fail
# print("Pass" if  (4 == sqrt(16)) else "Fail") # Pass

# print("------")
# print("large numbers")
# print("Pass" if (12345 == sqrt(152399025)) else "Fail") # Pass
# print("Pass" if (578 == sqrt(334084)) else "Fail") # Pass
# print("Pass" if (None == sqrt(-334084)) else "Fail") # Pass