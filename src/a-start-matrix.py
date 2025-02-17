import heapq
from collections import defaultdict

MOVES = [
    # Orthogonal
    (-1, 0, 100),
    (1, 0, 100),
    (0, -1, 100),
    (0, 1, 100),

    # Diagonals
    (-1, -1, 141),
    (-1, 1, 141),
    (1, -1, 141),
    (1, 1, 141)
]

def heuristic(a, b):
    """The heuristic function calculates the Manhattan distance between two points"""
    x1, y1 = a
    x2, y2 = b
    return abs(x2 - x1) * 100 + abs(y2 - y1) * 100

def a_star(start, goal, matrix):
    rows, cols = len(matrix), len(matrix[0])

    # For the open list, we use a heap queue to store the nodes with the lowest f(n) value at the top (priority queue)
    # ( f(n), node, g(n), path )
    open_list = []
    heapq.heappush(open_list, (heuristic(start, goal), start, 0, [start]))

    close_list = defaultdict(lambda: float('inf'))

    while open_list:
        # Pop the node with the lowest f(n) from the open list
        _, current_cell, g_cost_parent, path = heapq.heappop(open_list)

        # If the current node is the goal, we return the path and the cost
        if current_cell == goal:
            return path, g_cost_parent

        x, y = current_cell
        close_list[current_cell] = g_cost_parent

        # Explore the neighbors of the current node
        for dx, dy, move_cost in MOVES:
            neighbor_x, neighbor_y = x + dx, y + dy

            # Check if the neighbor is within the bounds of the matrix
            if neighbor_x < 0 or neighbor_x >= cols or neighbor_y < 0 or neighbor_y >= rows:
                continue

            # Check if the neighbor is an obstacle
            if matrix[neighbor_y][neighbor_x] == 1:
                continue

            g_score = g_cost_parent + move_cost
            f_cost_closed = close_list[(neighbor_x, neighbor_y)]

            if g_score < f_cost_closed:
                heuristic_cost = heuristic((neighbor_x, neighbor_y), goal)
                f_cost = g_score + heuristic_cost

                # Create the path to the neighbor
                new_path = path.copy() + [(neighbor_x, neighbor_y)]
                heapq.heappush(open_list, (f_cost, (neighbor_x, neighbor_y), g_score, new_path))

    # No path found
    return None


maze = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 2)
goal = (4, 2)

path, cost = a_star(start, goal, maze)

if path is not None:
    print(f'Path: {" > ".join(str(pos) for pos in path)}')
    print(f'Cost: {cost}')
else:
    print('No path found')
