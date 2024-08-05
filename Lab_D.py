def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        return -1
sorted_array = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target_value = 12
result_index = binary_search(sorted_array, target_value)
if result_index != -1:
    print(f"Target {target_value} found at index {result_index}.")
else:
    print(f"Target {target_value} not found in the array.")
