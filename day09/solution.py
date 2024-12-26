def read_number_from_file(file_path):
    with open(file_path, 'r') as file:
        number = file.read().strip()
    return number

def decode_disk_map(number):
    disk_map = []
    file_id = 0
    i = 0
    
    while i < len(number):
        # Size of file block
        file_block_size = int(number[i])
        disk_map.extend([str(file_id)] * file_block_size)
        file_id += 1
        i += 1
        
        if i < len(number):
            # Size of free space block
            free_space_size = int(number[i])
            disk_map.extend(['.'] * free_space_size)
            i += 1
    
    return disk_map

def move_file_blocks(disk_map):
    left, right = 0, len(disk_map) - 1
 
    while left < right:
        # Move the left pointer to the next free space
        while left < right and disk_map[left] != '.':
            left += 1
        # Move the right pointer to the next file block
        while left < right and disk_map[right] == '.':
            right -= 1
        
        if left < right:
            # Swap the free space with the file block
            disk_map[left], disk_map[right] = disk_map[right], disk_map[left]
            left += 1
            right -= 1
    
    return disk_map

def calculate_checksum(disk_map):
    checksum = 0
    for pos, char in enumerate(disk_map):
        if char != '.':
            checksum += pos * int(char)
    return checksum

# Part 1 - Non-contiguous file moving  
number = read_number_from_file("day09/input.txt")
original_map = decode_disk_map(number)
compact_map = move_file_blocks(original_map)
#print("Original map: ", original_map)
#print("Compact map - Part 1: ", compact_map)
print("Part 1:", calculate_checksum(compact_map))


from collections import deque

# Part 2 - Only contiguous file moving  
def find_free_space_blocks(disk_map):
    free_blocks = deque()
    start = None
    for i, char in enumerate(disk_map):
        if char == '.':
            if start is None:
                start = i
        else:
            if start is not None:
                free_blocks.append((start, i - start))
                start = None
    if start is not None:
        free_blocks.append((start, len(disk_map) - start))
    return free_blocks

def move_file_blocks_contiguous(disk_map):
    n = len(disk_map)
    free_blocks = find_free_space_blocks(disk_map)
    
    i = 0
    while i < n:
        if disk_map[i] != '.':
            file_id = disk_map[i]
            file_size = 1
            while i + file_size < n and disk_map[i + file_size] == file_id:
                file_size += 1
            
            while free_blocks:
                start, length = free_blocks[0]
                if length >= file_size:
                    # Move the file block to the free space
                    disk_map[start:start + file_size] = [file_id] * file_size
                    disk_map[i:i + file_size] = ['.'] * file_size
                    
                    # Update the free_blocks deque incrementally
                    if length > file_size:
                        free_blocks[0] = (start + file_size, length - file_size)
                    else:
                        free_blocks.popleft()
                        break
                else:
                    free_blocks.popleft()
        
        i += 1    
    return disk_map

compact_map2 = move_file_blocks_contiguous(original_map)
print("Compact map - Part 2: ", compact_map2)
print("Part 2:", calculate_checksum(compact_map2))
