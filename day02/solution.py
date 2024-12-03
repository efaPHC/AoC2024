# Open the file and read all lines
with open('input.txt', 'r') as file:
    # Read lines and split them into lists of integers
    lines = [list(map(int, line.split())) for line in file]

#print("Array:", lines)

# Function to check if a list is strictly increasing by up to n
def is_increasing_by_up_to_n(lst, n):
    return all(1 <= y - x <= n for x, y in zip(lst, lst[1:]))

# Function to check if a list is strictly decreasing by up to n
def is_decreasing_by_up_to_n(lst, n):
    return all(1 <= x - y <= n for x, y in zip(lst, lst[1:]))

# Function to check if removing one element makes the list strictly 
#    increasing or decreasing by up to n
def can_be_strictly_increasing_or_decreasing_by_removing_one(lst, n):
    for i in range(len(lst)):
        new_lst = lst[:i] + lst[i+1:]
        if is_increasing_by_up_to_n(new_lst, n) or is_decreasing_by_up_to_n(new_lst, n):
            return True
    return False

# Define n
n = 3

# Check each line
sum_safes = 0
for line in enumerate(lines):
    if is_increasing_by_up_to_n(line, n):
        sum_safes += 1
    elif is_decreasing_by_up_to_n(line, n):
        sum_safes += 1

        
print("Safe reports:", sum_safes)

sum_safes = 0
# Check each line
for line in enumerate(lines):
    if is_increasing_by_up_to_n(line, n):
        sum_safes += 1
    elif is_decreasing_by_up_to_n(line, n):
        sum_safes += 1
    else:
        if can_be_strictly_increasing_or_decreasing_by_removing_one(line, n):
            sum_safes += 1

print("Safe reports with Dampener:", sum_safes)