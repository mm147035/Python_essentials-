# This program creates a list of numbers and performs several operations on it.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Print the list of numbers
print("The original list of numbers is:", numbers)

# Add up all the numbers in the list
total = sum(numbers)
print("The sum of the numbers is:", total)

# Find the maximum and minimum numbers in the list
maximum = max(numbers)
minimum = min(numbers)
print("The maximum number in the list is:", maximum)
print("The minimum number in the list is:", minimum)

# Sort the list of numbers in ascending order
numbers.sort()
print("The list of numbers in ascending order is:", numbers)

# Filter the list of numbers to only include even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("The even numbers in the list are:", evens)
