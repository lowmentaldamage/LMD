# Correct number of chess pieces

required = [1, 1, 2, 2, 2, 8]

# Read input and convert each value to an integer

found = input().split()
for i in range(len(found)):
    found[i] = int(found[i])

# List to store differences

diffs = []

# Calculate how many pieces are missing or extra

for i in range(6):
    diffs.append(required[i] - found[i])

# Print the result
# This makes that every line in the list is printed as an argument on its own

print(*diffs)
