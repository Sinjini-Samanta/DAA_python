def quick_sort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pi = partition(arr, low, high)

        # Recursively sort the left and right subarrays
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j][0] <= pivot[0]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def check_stability():
    # Create a list of tuples (value, original index)
    arr = [(4, 0), (3, 1), (4, 2), (2, 3), (3, 4)]

    # Perform the quick sort
    quick_sort(arr, 0, len(arr) - 1)

    # Check if the relative order of equal elements is maintained
    for i in range(1, len(arr)):
        if arr[i][0] == arr[i - 1][0] and arr[i][1] < arr[i - 1][1]:
            print("Quick Sort is not stable")
            return False
    
    print("Quick Sort is stable")
    return True

# Example usage
check_stability()