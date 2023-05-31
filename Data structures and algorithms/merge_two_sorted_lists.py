def merge_sorted_lists(list1, list2):
    # Initialize two pointers to the start of the input lists
    i = 0
    j = 0

    # Initialize an empty list to store the merged result
    merged = []

    # Loop until one of the pointers reaches the end of its list
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            # If the current element in list1 is smaller, add it to the merged list and move the pointer to the next element in list1
            merged.append(list1[i])
            i += 1
        else:
            # If the current element in list2 is smaller or equal, add it to the merged list and move the pointer to the next element in list2
            merged.append(list2[j])
            j += 1

    # Add any remaining elements from list1 or list2 to the merged list
    merged += list1[i:]
    merged += list2[j:]

    return merged


list1 = [1, 3, 5]
list2 = [2, 4, 6]

result = merge_sorted_lists(list1, list2)
print(result)  # Output: [1, 2, 3, 4, 5, 6]
