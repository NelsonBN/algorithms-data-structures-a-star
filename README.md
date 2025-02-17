# Algorithms and Data Structures - A-Star (A*)


## Demo

### Using a graph

[Find the shortest path between two cities](./src/a-start-graph.py)

```mermaid
flowchart LR
  PT((PT)) --> |6| ES
  PT --> |12| FR
  PT --> |21| GB

  ES((ES)) -->|18| DE
  ES --> |9| FR

  FR((FR)) -->|7| DE
  FR --> |24| IT
  FR --> |8| GB

  GB((GB)) --> |12| DE
  GB((GB)) --> |7| NL((NL))

  IT((IT)) --> |13| DE
  IT --> |26| FI((FI))

  DE((DE)) --> |19| FI
  DE --> |6| NL

  style PT stroke:#0AF,stroke-width:2px;
  style FI stroke:#FA0,stroke-width:2px;
```

**Heuristic `h(n)`**

| Origem | Cidade      | `h(n)` |
|--------|-------------|--------|
| PT     | Portugal    | 27     |
| ES     | Espanha     | 19     |
| FR     | França      | 25     |
| GB     | Reino Unido | 10     |
| NL     | Holanda     | 26     |
| DE     | Alemanha    | 19     |
| IT     | Itália      | 23     |
| FI     | Finlândia   | 0      |


### Using a grid (matrix)
[Find the shortest path in a maze](./src/a-start-matrix.py)

![Maze](./media/maze.svg)

- Movement custs:
  - `100` for orthogonal movement (⬅️ ➡️ ⬆️ ⬇️)
  - `141` for diagonal movement (↖️ ↗️ ↘️ ↙️)
- Heuristic `h(n)` is the manhattan distance to the goal

## References
- [Other algoritmos & Data Structures](https://github.com/NelsonBN/algorithms-data-structures)
- [Wikipedia](https://en.wikipedia.org/wiki/A*_search_algorithm)
