def searchInsert(nums, target):
    # Initialize pointers to keep track of the start and end of the array
    left, right = 0, len(nums) - 1

    # Binary search the array for the target value
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            # If the target value is found, return the index
            return mid
        elif nums[mid] < target:
            # If the middle value is less than the target, move the left pointer to mid + 1
            left = mid + 1
        else:
            # If the middle value is greater than the target, move the right pointer to mid - 1
            right = mid - 1

    # If the target value is not found, return the index where it should be inserted
    return left

nums = [1, 3, 5, 6]
target = 5

result = searchInsert(nums, target)
print(result)  # Output: 2
