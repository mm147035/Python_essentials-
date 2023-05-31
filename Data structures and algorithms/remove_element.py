def removeElement(nums, val):
    # Initialize a pointer to keep track of the current index in the array
    i = 0

    # Loop through the array and compare each element to the value to be removed
    for j in range(len(nums)):
        if nums[j] != val:
            # If the current element is not equal to the value to be removed, move the pointer to the next index
            nums[i] = nums[j]
            i += 1

    # Return the length of the non-removed part of the array
    return i

nums = [3, 2, 2, 3]
val = 3
result = removeElement(nums, val)
print(nums[:result])  # Output: [2, 2]
print(result)  # Output: 2
