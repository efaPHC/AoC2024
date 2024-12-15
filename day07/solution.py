import itertools

def evaluate_expression(nums, ops, cache):
    # Search first in cache to increase code efficiency
    key = (tuple(nums), tuple(ops))
    if key in cache:
        return cache[key]
    
    # Calculate expression
    result = nums[0]
    for i in range(1, len(nums)):
        if ops[i-1] == '+':
            result += nums[i]
        elif ops[i-1] == '*':
            result *= nums[i]
        elif ops[i-1] == '||':
            result = int(str(result) + str(nums[i]))

    # Add last calculation in cache
    cache[key] = result
    return result

def check_calibration(data, is_part2):
    results = {}
    total_results = 0
    
    for line in data:
        # Separate result from individual measurements 
        result, measurements = line.split(":")
        result = int(result.strip())
        measurements = list(map(int, measurements.strip().split()))

        # Generate all combinations of operators
        if is_part2:
            operators = ["+", "*", "||"]
        else:
            operators = ["+", "*"]
        all_combinations = list(itertools.product(operators, repeat=len(measurements)-1))

        match_found = False
        cache = {} 
        for combination in all_combinations:
            if evaluate_expression(measurements, combination, cache) == result:
                match_found = True
                total_results += result
                break
        
        results[result] = match_found
    
    return results, total_results

def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return data

# Read data from file
data = read_data_from_file("day07/input.txt")

# Part 1 - + and * operators
results, total_results = check_calibration(data, False)

#for key, value in results.items():
#    print(f"Calibration Result: {key}, Match Found: {value}")
print("Part 1:", total_results)

# Part 2 - +, *, || operators
results, total_results = check_calibration(data, True)
print("Part 2:", total_results)
