def isValid(s):
    # Create a stack to store the opening parentheses
    stack = []

    # Create a dictionary to map the opening and closing parentheses
    parentheses_map = {')': '(', '}': '{', ']': '['}

    # Loop through the characters in the input string
    for char in s:
        # If the current character is an opening parenthesis, push it onto the stack
        if char in parentheses_map.values():
            stack.append(char)
        # If the current character is a closing parenthesis, check if it matches the most recent opening parenthesis
        elif char in parentheses_map.keys():
            if not stack or stack.pop() != parentheses_map[char]:
                return False
        # If the current character is not a parenthesis, ignore it
        else:
            continue

    # If there are any opening parentheses left on the stack, the string is invalid
    return not stack



s = "()[]{}"
result = isValid(s)
print(result)  # Output: True
