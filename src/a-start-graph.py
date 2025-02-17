import heapq
from collections import defaultdict

def a_star(start, goal, graph, heuristics):
    # For the open list, we use a heap queue to store the nodes with the lowest f(n) value at the top (priority queue)
    # ( f(n), node, g(n), path )
    open_list = []
    heapq.heappush(open_list, (heuristics[start], start, 0, [start]))

    close_list = defaultdict(lambda: float('inf'))

    while open_list:
        # Pop the node with the lowest f(n) from the open list
        _, current, g_cost_parent, path = heapq.heappop(open_list)

        # If the current node is the goal, we return the path and the cost
        if current == goal:
            return path, g_cost_parent

        close_list[current] = g_cost_parent

        # Explore the neighbors of the current node
        for neighbor, move_cost in graph.get(current, {}).items():
            g_score = g_cost_parent + move_cost

            f_cost_closed = close_list[neighbor]
            if g_score < f_cost_closed:
                heuristic = heuristics[neighbor]
                f_cost = g_score + heuristic
                # Create the path to the neighbor
                path = path + [neighbor]
                heapq.heappush(open_list, (f_cost, neighbor, g_score, path))

    # No path found
    return None


heuristics = {
    "PT": 27,
    "ES": 19,
    "FR": 25,
    "GB": 10,
    "NL": 26,
    "DE": 19,
    "IT": 23,
    "FI": 0
}

graph = {
    'PT': { 'ES': 6, 'FR': 12, 'GB': 21 },
    'ES': { 'DE': 18, 'FR': 9 },
    'FR': { 'DE': 7, 'IT': 24, 'GB': 8 },
    'GB': { 'DE': 12, 'NL': 7 },
    'IT': { 'DE': 13, 'FI': 26 },
    'DE': { 'FI': 19, 'NL': 6 }
}

start = 'PT'
goal = 'FI'

path, cost = a_star(start, goal, graph, heuristics)

if path is not None:
    print(f'Path: {" > ".join(path)}')
    print(f'Cost: {cost}')
else:
    print('No path found')
