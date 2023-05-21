def romanToInt(s):
    # Create a dictionary to store the values of each Roman numeral
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    # Initialize the result to zero
    result = 0

    # Loop through the input string
    for i in range(len(s)):
        # If the current Roman numeral is less than the next one, subtract its value from the result
        if i < len(s) - 1 and roman_dict[s[i]] < roman_dict[s[i+1]]:
            result -= roman_dict[s[i]]
        # Otherwise, add its value to the result
        else:
            result += roman_dict[s[i]]

    # Return the final result
    return result

s = "MCMXCIV"
result = romanToInt(s)
print(result)  # Output: 1994
