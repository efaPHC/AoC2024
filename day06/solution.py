def parse_map(input_map):
    for i, row in enumerate(input_map):
        for j, char in enumerate(row):
            if char in "^<v>":
                return i, j, char

def move_player(position, direction):
    i, j = position
    if direction == "^":
        return i - 1, j
    elif direction == "v":
        return i + 1, j
    elif direction == "<":
        return i, j - 1
    elif direction == ">":
        return i, j + 1

def turn_clockwise(direction):
    turns = {"^": ">", ">": "v", "v": "<", "<": "^"}
    return turns[direction]

def play_game(input_map):
    position = parse_map(input_map)
    distinct_positions = set()
    i, j, direction = position
    distinct_positions.add((i, j))

    while True:
        next_position = move_player((i, j), direction)
        ni, nj = next_position

        if ni < 0 or ni >= len(input_map) or nj < 0 or nj >= len(input_map[0]):
            break

        if input_map[ni][nj] == "#":
            direction = turn_clockwise(direction)
        else:
            i, j = ni, nj
            distinct_positions.add((i, j))

    return distinct_positions

def is_loop(input_map, position, direction):
    visited_positions = set()
    i, j = position

    while (i, j, direction) not in visited_positions:
        visited_positions.add((i, j, direction))
        next_position = move_player((i, j), direction)
        ni, nj = next_position

        if ni < 0 or ni >= len(input_map) or nj < 0 or nj >= len(input_map[0]):
            return False

        if input_map[ni][nj] == "#":
            direction = turn_clockwise(direction)
        else:
            i, j = ni, nj

    return True

def check_for_loops(input_map):
    loop_positions = []
    modified_map = [list(row) for row in input_map]
    initial_position = parse_map(input_map)
    initial_i, initial_j, initial_direction = initial_position

    for i in range(len(input_map)):
        for j in range(len(input_map[0])):
            if input_map[i][j] == ".":
                # Place an obstacle and check for loop
                modified_map[i][j] = "#"
                if is_loop(["".join(row) for row in modified_map], (initial_i, initial_j), initial_direction):
                    loop_positions.append((i, j))
                # Remove the obstacle
                modified_map[i][j] = "."

    return loop_positions


def read_map_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]


# Read the map from the file
input_map = read_map_from_file("day06/input.txt")

# Part 1 - Get the distinct positions occupied by the player
distinct_positions = play_game(input_map)

# Part 2 - Get the positions where a new obstacle can create a loop
loop_positions = check_for_loops(input_map)

print("Part 1:", len(distinct_positions))
print("Part 2:", len(loop_positions))
