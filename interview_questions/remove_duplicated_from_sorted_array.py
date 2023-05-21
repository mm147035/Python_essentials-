def removeDuplicates(nums):
    # Initialize a pointer to keep track of the current index in the array
    i = 0

    # Loop through the array and compare each element to the previous element
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            # If the current element is not equal to the previous element, move the pointer to the next index
            i += 1
            # Replace the value at the current pointer with the value of the current element
            nums[i] = nums[j]

    # Return the length of the non-duplicate part of the array
    return i + 1

nums = [1, 1, 2, 2, 2, 3, 4, 4, 5]
result = removeDuplicates(nums)
print(nums[:result])  # Output: [1, 2, 3, 4, 5]
print(result)  # Output: 5
