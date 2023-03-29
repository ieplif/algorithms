# Selcetion Sort is a algorithm
# Ex.: find a smaller element in array

def findSmaller(arr):
    smaller = arr[0]  # store the smaller value
    smaller_idx = 0  # index of the smaller value
    for i in range(1, len(arr)):
        if arr[i] < smaller:
            smaller = arr[i]
            smaller_idx = i
    return smaller_idx

def selectionSort(arr):
    newArr = []
    for i in range (len(arr)):
        smaller = findSmaller(arr)
        newArr.append(arr.pop(smaller))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))
