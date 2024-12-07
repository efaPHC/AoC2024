def read_file(file_path):
    with open(file_path, 'r') as file:
        rules = []
        sequences = []
        is_sequences = False
        
        for line in file:
            line = line.strip()
            if line == "":
                is_sequences = True
                continue
            
            if is_sequences:
                sequences.append(list(map(int, line.split(','))))
            else:
                n1, n2 = line.split('|')
                rules.append((int(n1), int(n2)))
                
    return rules, sequences

def check_rules(rules, sequences):
    sum1 = 0
    incorrects = []
    for sequence in sequences:
        valid = True
        for n1, n2 in rules:
            if n1 in sequence and n2 in sequence:
                if sequence.index(n1) > sequence.index(n2):
                    valid = False
                    incorrects.append(sequence)
                    break
        if valid:
            sum1 += sequence[len(sequence)//2]
    return sum1, incorrects

# Part 1 - Find the incorrect-ordered sequences
# and add up the middle numbers of the correct sequences
rules, sequences = read_file('day05/input.txt')
#print("Rules:", rules)
#print("Sequences:", sequences)

sum1, incorrects = check_rules(rules, sequences)
print("Result Part 1:", sum1)

# Part 2 - Re-order the incorrect sequences
# and add up the middle numbers of the updates

def reorder_sequence(rules, sequence):
    # Create a dictionary to store the position of each element in the sequence
    position = {value: idx for idx, value in enumerate(sequence)}
    
    # Sort the rules based on their positions in the sequence
    sorted_rules = sorted(rules, key=lambda x: (position.get(x[0], float('inf')), position.get(x[1], float('inf'))))
    
    # Reorder the sequence based on the sorted rules
    for n1, n2 in sorted_rules:
        if n1 in sequence and n2 in sequence:
            idx1 = sequence.index(n1)
            idx2 = sequence.index(n2)
            if idx1 > idx2:
                # Swap the elements to satisfy the rule
                sequence[idx1], sequence[idx2] = sequence[idx2], sequence[idx1]                
                #print(f"Swapped {n1} and {n2} in sequence: {sequence}")
    
    return sequence

sum2 = 0
reordered = []
for sequence in incorrects:
    reordered_sequence = reorder_sequence(rules, sequence)
    reordered.append(reordered_sequence)
    sum2 += reordered_sequence[len(reordered_sequence)//2]

print("Incorrect sequences:", len(incorrects))
print("Result Part 2 (no help):", sum2)

# Part 2 with a little help from my friend Copilot 

def topological_sort(rules, sequence):
    from collections import defaultdict, deque
    
    # Step 1: Build the graph and in-degree count
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    for n1, n2 in rules:
        if n1 in sequence and n2 in sequence:
            graph[n1].append(n2)
            in_degree[n2] += 1
            if n1 not in in_degree:
                in_degree[n1] = 0
    
    # Step 2: Initialize the queue with nodes having zero in-degree
    queue = deque([node for node in sequence if in_degree[node] == 0])
    sorted_sequence = []
    
    # Step 3: Process the nodes
    while queue:
        node = queue.popleft()
        sorted_sequence.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Step 4: Check if sorting was successful
    if len(sorted_sequence) == len(sequence):
        return sorted_sequence
    else:
        return sequence  # Return the original sequence if sorting fails


sum2 = 0
reordered = []
for sequence in incorrects:
    reordered_sequence = topological_sort(rules, sequence)
    reordered.append(reordered_sequence)
    sum2 += reordered_sequence[len(reordered_sequence)//2]

#print("Reordered sequences:", reordered)
print("Result Part 2 (Copilot help):", sum2)
