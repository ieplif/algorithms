# Binary search is an algorithm. 
# It's input is an ordered list of elements.

# With binary search, you guess an intermediate number and eliminate
# half of the remaining numbers each time.

# Generally speaking, for a list of n numbers, binary search needs 
# log2n to return the correct value.

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        half = (low + high) // 2
        guess = list[half]

        if guess == item:
            return half
        if guess > item:
            high = half - 1
        else:
            low = half + 1
    return -1

#my_list = [1, 3, 5, 7, 9]

#print(binary_search(my_list, 3))
#print(binary_search(my_list, -5))
