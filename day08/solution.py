def read_antennas_from_file(file_path):
    # Read input file
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file.readlines()]

    # Map the antennas
    antennas = {}
    for row_index, row in enumerate(grid):
        for col_index, cell in enumerate(row):
            if cell != '.':
                if cell not in antennas:
                    antennas[cell] = []
                antennas[cell].append((row_index, col_index))
    return grid, antennas

def add_antinode(grid, position):
    row, col = position
    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        grid[row] = grid[row][:col] + '#' + grid[row][col+1:]
    return grid

def find_antinodes(grid, antennas, repeat):
    for freq, positions in antennas.items():
        for i in range(len(positions)):
            for j in range(i+1, len(positions)):
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                xdiff = (x1 - x2)
                ydiff = (y1 - y2)

                # Antinodes according to rules in Part 1
                grid = add_antinode(grid, (x1 + xdiff, y1 + ydiff))
                grid = add_antinode(grid, (x2 - xdiff, y2 - ydiff))

                if repeat:
                    # Additional antinodes according to rules in Part 2
                    grid = add_antinode(grid, (x1, y1))
                    grid = add_antinode(grid, (x2, y2))
                    rep = 2
                    while 0 <= rep*abs(xdiff) < len(grid) and 0 <= rep*abs(ydiff) < len(grid[0]):
                        grid = add_antinode(grid, (x1 + rep*xdiff, y1 + rep*ydiff))
                        grid = add_antinode(grid, (x2 - rep*xdiff, y2 - rep*ydiff))
                        rep += 1
    return grid

# Part 1 - Count antinodes without repetition
grid, antennas = read_antennas_from_file("day08/input.txt")
grid1 = find_antinodes(grid, antennas, False)

print("Part 1 result:", sum(row.count('#') for row in grid1))

# Part 2 - Count antinodes with repetition
grid2 = find_antinodes(grid, antennas, True)
#for line in grid2:
#    print(line)
#print(antennas)

print("Part 2 result:", sum(row.count('#') for row in grid2))
