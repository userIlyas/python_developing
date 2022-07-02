# Task: create an array that is sorted in ascending order
# find Smallest is a function that finds the smallest element among the list
# selectionSort is a function that sotrs a elements in ascending order

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print(selectionSort([5, 3, 2, 6, 7, 9, 56, 889, 3345, 1]))