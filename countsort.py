def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    # Create a count array to store count of each element
    count = [0] * range_of_elements

    # Store count of each element
    for i in range(len(arr)):
        count[arr[i] - min_val] += 1

    # Store the cumulative count
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Build the output array
    output = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1

    # Copy the output array to arr
    for i in range(len(arr)):
        arr[i] = output[i]

    return arr

# Example usage
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Sorted array is:", sorted_arr)
