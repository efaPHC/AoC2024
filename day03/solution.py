# Open the file and read all lines
with open('input.txt', 'r') as file:
    lines = file.read()
    
#print("Input:", lines)

import re

def multiply_instructions(text):
    # Regular expression pattern to find "mul(int1,int2)"
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, text)

    result = 0
    for match in matches:
        int1, int2 = map(int, match)
        result += int1 * int2

    return result

def get_all_first_occurrences(text, str1, str2):
    matches = []
    pos = 0

    while True:
        # Find the first occurrence of str1
        start_idx = text.find(str1, pos)
        if start_idx == -1:
            break

        # Move the start index to the end of str1
        start_idx += len(str1)

        # Find the first occurrence of str2 after str1
        end_idx = text.find(str2, start_idx)
        if end_idx == -1:
            break

        # Add the substring between start_idx and end_idx to matches
        matches.append(text[start_idx:end_idx])

        # Update position to continue searching after the current end_idx
        pos = end_idx + len(str2)

    return matches


## Part 1 - Calculate all multiply instructions
print("Result Part 1:", multiply_instructions(lines))

## Part 2 - Calculate only instructions between the first occurent of str1 and str2
str1 = "do()"
str2 = "don't()"

result = 0

lines = str1 + lines + str2
occurrences = get_all_first_occurrences(lines, str1, str2)
for occurrence in enumerate(occurrences):
    result += multiply_instructions(str(occurrence))

#print("Occurrences:", occurrences)    
print("Result Part 2:", result)
