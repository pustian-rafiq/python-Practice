
#binary search using iteration method

def binarySearch(array, number, low, high):
    while low <= high:
        mid = (low + high)//2
        if number == array[mid]:
            return mid
        elif number > array[mid]:
            low = mid + 1

        else:
            high = mid - 1
    return -1


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = 6
high = len(array)-1
result = binarySearch(array, num, 0, high)
if result != -1:
    print("The index of the number is ", result)
else:
    print("not found the required data")