def twoSum(nums, target):
    # Create an empty dictionary to store the complement of each number and its index
    complement_dict = {}

    # Loop through the list of numbers
    for i in range(len(nums)):
        # Check if the complement of the current number is already in the dictionary
        if nums[i] in complement_dict:
            # If it is, return the indices of the two numbers that add up to the target
            return [complement_dict[nums[i]], i]
        else:
            # If it isn't, add the complement of the current number and its index to the dictionary
            complement_dict[target - nums[i]] = i

    # If no two numbers add up to the target, return an empty list
    return []


nums = [2, 7, 11, 15]
target = 9

result = twoSum(nums, target)
print(result)  # Output: [0, 1]
