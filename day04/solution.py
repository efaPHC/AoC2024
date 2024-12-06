# Open the file and read all lines
with open('input.txt', 'r') as file:
    grid = [line.strip() for line in file]
    
#print(f"Input:", grid)

## Part 1 - Search for all occurrences of word XMAS
def search_word(grid, word):
    word_lenght = len(word)
    grid_height = len(grid)
    grid_width = len(grid[0])
    directions = [
        (1, 0), (1, 1), (0, 1), (-1, 1),
        (-1, 0), (-1, -1), (0, -1), (1, -1) 
    ]

    def is_word_at_position(x, y, dx, dy):
        for i in range(word_lenght):
            nx = x + i*dx
            ny = y + i*dy
            if nx < 0 or ny < 0 or nx >= grid_width or ny >=grid_height:
                return False
            if grid[ny][nx] != word[i]:
                return False
        return True
    
    count = 0

    for y in range(grid_height):
        for x in range(grid_width):
            for dx, dy in directions:
                if is_word_at_position(x, y, dx, dy):
                    count += 1

    return count

print(f"Result Part 1:", search_word(grid, 'XMAS'))

## Part 2 - Search for all occurrences of xpattern MAS
def search_xpattern(grid, word):
    word_lenght = len(word)
    grid_height = len(grid)
    grid_width = len(grid[0])

    def is_word_at_position(x, y, dx, dy):
        for i in range(word_lenght):
            nx = x + i*dx
            ny = y + i*dy
            if nx < 0 or ny < 0 or nx >= grid_width or ny >=grid_height:
                return False
            if grid[ny][nx] != word[i]:
                return False
        return True
    
    count = 0

    for y in range(grid_height):
        for x in range(grid_width):
            if is_word_at_position(x, y, 1, 1):
                if is_word_at_position(x+word_lenght-1, y, -1, 1) or is_word_at_position(x, y+word_lenght-1, 1, -1):
                    count += 1
            if is_word_at_position(x, y, -1, -1):
                if is_word_at_position(x-(word_lenght-1), y, 1, -1) or is_word_at_position(x, y-(word_lenght-1), -1, 1):
                    count += 1

    return count


print(f"Result Part 2:", search_xpattern(grid, 'MAS'))
