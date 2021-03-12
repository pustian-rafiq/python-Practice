#Binary search using Recursive method

def binarySearchByRecursion(array, number, low, high):
    if low <= high:
        mid = (low + high)//2

        if number == array[mid]:
            return mid
        elif number > array[mid]:
            return binarySearchByRecursion(array, number, mid+1, high)
        else:
            return binarySearchByRecursion(array, number, low, mid - 1)
    return -1


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number = 5
high = len(array)
result = binarySearchByRecursion(array, number, 0, high)
if result != -1:
    print("The index of the number is ", result)
else:
    print("Data not found")