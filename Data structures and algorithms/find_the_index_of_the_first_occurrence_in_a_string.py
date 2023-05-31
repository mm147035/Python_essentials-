
# including spaces
string = "hello world"
substring = "d"

index = string.index(substring)

print(index)  # Output: 4



print("*"*10)


# without spaces
string = "hello world"
substring = "w"

# Remove spaces from the string
string = string.replace(" ", "")

# Find the index of the substring in the modified string
index = string.index(substring)

print(index)  # Output: 4

