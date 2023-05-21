
def longest_common_prefix(strs):
    if not strs:
        # If the input list is empty, return an empty string
        return ""

    # Initialize the longest common prefix as the first string in the list
    prefix = strs[0]

    for string in strs[1:]:
        # Compare each string in the list to the current prefix
        while string.find(prefix) != 0:
            # If the current prefix is not a prefix of the current string, remove the last character from the prefix
            prefix = prefix[:-1]
            if not prefix:
                # If the prefix becomes empty, there is no common prefix
                return ""

    return prefix



strs = ["flower", "flow", "flight"]

result = longest_common_prefix(strs)
print(result)  # Output: "fl"
