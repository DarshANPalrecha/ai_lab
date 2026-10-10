
# 8-Puzzle Problem using A* Search Algorithm
from heapq import heappush, heappop

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def heuristic(state):
    distance = 0
    for i, tile in enumerate(state):
        if tile != 0:
            goal_pos = tile - 1
            distance += abs(i // 3 - goal_pos // 3)
            distance += abs(i % 3 - goal_pos % 3)
    return distance

def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    row, col = zero // 3, zero % 3

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        nr, nc = row + dr, col + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            new_pos = nr * 3 + nc
            new_state = list(state)
            new_state[zero], new_state[new_pos] = (
                new_state[new_pos], new_state[zero]
            )
            neighbors.append(tuple(new_state))

    return neighbors

def solve(start):
    pq = []
    heappush(pq, (heuristic(start), 0, start, [start]))
    visited = set()

    while pq:
        f, g, state, path = heappop(pq)

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(neighbor)
                heappush(
                    pq,
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    return None

# 0 represents the blank tile
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

path = solve(start)

if path:
    print("Solution found in", len(path) - 1, "moves:\n")
    for state in path:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()
else:
    print("No solution exists.")
