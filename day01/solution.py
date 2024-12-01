# Open the file and read all lines
with open('input.txt', 'r') as file:
    lines = file.readlines()

# Use list comprehensions and zip to split the columns
array1, array2 = zip(*(map(int, line.split()) for line in lines))

# Convert the tuples to lists
array1 = list(array1)
array2 = list(array2)

#print("Array 1:", array1)
#print("Array 2:", array2)

# Sort the arrays in place
array1.sort()
array2.sort()

#print("Sorted Array 1:", array1)
#print("Sorted Array 2:", array2)


## Part 1 - Calculate distance between elements of array 1 and 2
# Calculating the differences
distances = [abs(a - b) for a, b in zip(array1, array2)]

# Sum the differences
distancesSum = sum(distances)

#print("Distances:", distances)
print("Sum of Distances:", distancesSum)

## Part 2 - Calculate similarity score
from collections import Counter

# Create a Counter object for array2
counter_array2 = Counter(array2)

# Multiply each each element in array1 by its occurrences count within array2
occurrences = [element * counter_array2[element] for element in array1]
similarityScore = sum(occurrences)

#print("Occurrences:", occurrences)
print("Similarity score:", similarityScore)
