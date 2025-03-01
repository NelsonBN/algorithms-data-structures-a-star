# A-* (A-Star) Heuristic Consistency Checker

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

consitent = True

for node, neighbors in graph.items():
    for neighbor, move_cost in neighbors.items():

        node_heuristic = heuristics[node]
        neighbor_heuristic = heuristics[neighbor]

        cost = move_cost + neighbor_heuristic
        current_consitent = node_heuristic <= cost

        if not current_consitent:
            consitent = False

        print(f"{node} -> {neighbor} | h({node_heuristic}) <= c({move_cost}') + h({neighbor_heuristic}') | {node_heuristic} <= {cost} | Consistent: {current_consitent}")

print(f'Consistent: {consitent}')
