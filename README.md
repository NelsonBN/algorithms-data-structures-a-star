# Algorithms and Data Structures - A-Star (A*)


## Demo

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

**Tabela de heurísticas para chegar ao destino:**

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



## References
- [Other algoritmos & Data Structures](https://github.com/NelsonBN/algorithms-data-structures)
- [Wikipedia](https://en.wikipedia.org/wiki/A*_search_algorithm)
