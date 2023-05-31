def is_palindrome(string):
    """
    Check if a string is a palindrome.
    """
    string = string.lower()  # convert string to lowercase
    return string == string[::-1]  # check if the reversed string is equal to the original string

# Example usage
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))  # Output: False


