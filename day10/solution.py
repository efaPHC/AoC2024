def read_map_from_file(file_path):
    with open(file_path, 'r') as file:
        topo_map = [list(map(int, line.strip())) for line in file.readlines()]
    return topo_map

def find_trailheads(topo_map):
    trailheads = []
    for i in range(len(topo_map)):
        for j in range(len(topo_map[i])):
            if topo_map[i][j] == 0:
                trailheads.append((i, j))
    return trailheads

def is_valid_position(topo_map, x, y):
    return 0 <= x < len(topo_map) and 0 <= y < len(topo_map[0])

def find_summits(topo_map, trailhead):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    summits = set()
    stack = [trailhead]
    visited = set()
    
    while stack:
        x, y = stack.pop()
        visited.add((x, y))
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid_position(topo_map, nx, ny) and (nx, ny) not in visited:
                if topo_map[nx][ny] == topo_map[x][y] + 1:
                    if topo_map[nx][ny] == 9:
                        summits.add((nx, ny))
                    else:
                        stack.append((nx, ny))
    
    return summits

def calculate_scores(topo_map, trailheads):
    scores = {}
    sum_scores = 0
    for trailhead in trailheads:
        scores[trailhead] = len(find_summits(topo_map, trailhead))
        sum_scores += scores[trailhead]
    return scores, sum_scores

# Part 1 - Calculate trail scores
# Number of summits reached by each trailhead
topo_map = read_map_from_file('day10/input_test1.txt')
trailheads = find_trailheads(topo_map)
scores, sum_scores = calculate_scores(topo_map, trailheads)

#print("Trailhead scores:")
#for trailhead, score in scores.items():
#    print(f"Trailhead at {trailhead} has a score of {score}")

print("Part 1:", sum_scores)

# Part 2 - Calculate trail ratings
# Number of different paths in each trailhead that reach summits

def find_paths(topo_map, trailhead, summits):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    paths = 0
    stack = [trailhead]
    visited = set()

    while stack:
        x, y = stack.pop()
        visited.add((x, y))
        
        for dx, dy in directions:
            if is_valid_position(topo_map, nx, ny) and (nx, ny) not in visited:
                if topo_map[nx][ny] == topo_map[x][y] + 1:
                    if (nx,ny) in summits:
                        paths += 1

    return paths

def calculate_ratings(topo_map, trailheads):
    ratings = {}
    sum_ratings = 0
    for trailhead in trailheads:
        summits = find_summits(topo_map, trailhead)
        ratings[trailhead] = find_paths(topo_map, trailhead, summits)
        sum_ratings += ratings[trailhead]
    return ratings, sum_ratings


ratings, sum_ratings = calculate_ratings(topo_map, trailheads)
print("Trailhead ratings:")
for trailhead, rating in ratings.items():
    print(f"Trailhead at {trailhead} has a rating of {rating}")

print("Part 2:", sum_ratings)
