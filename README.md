# N-Puzzle Problem
*4<sup>th</sup> semester AI project*

### Introduction

N-puzzle is a generalization of the 8-puzzle game to larger frames. The puzzle starts with a square frame consisting of $(n - 1)$ tiles inside. The tiles are numbered from $1$ 1o $(n - 1)$. There is also one empty slot in the frame not occupied by any tile. 

In each move, any tile with an adjacent edge to the empty slot may be moved there. Our goal is to arrange the randomly placed tiles in numerical order.

The game may be modelled as a state-search problem and solved using any standard graph traversal algorithm.[^1]

### Searching the state space

For a game with $(n - 1)$ tiles, the state space consists of $n!$ nodes. About half of these states are unsolvable, that is they do not have a path to the goal state.[^2] 

Applying DFS or BFS will yield a time complexity of $O(n!)$. One could use Dijkstra's algorithm or A* to improve the average-case performance, but the asymptotic bound will still remain on the order of $n!$.[^3] This motivates the need for methods to prune the search space.

Before searching for a path, we first run a simpler $O(n \log n)$ algorithm to determine if the initial state is even solvable.[^4] If the initial state is found *not* to be solvable, a search is not required.

#### Algorithm to verify solvability
1. Place the tile numbers in an array. Ordered from left to right, then top to bottom. Ignore the empty slot. 
2. Count the numbers of inversions in the array. An inverted pair is any ordered pair $(u, v)$ where $u > v$ and $u$ occurs before $v$ in the array.
3. The puzzle is solvable if and only if there an odd number of such inversions.

[^1]: Russell, S., & Norvig, P. (2020). _Artificial Intelligence: A Modern Approach_ (pp. 70-71).

[^2]: https://webdocs.cs.ualberta.ca/~hayward/355/jem/tile.html#pzl

[^3]: https://www.baeldung.com/cs/dijkstra-time-complexity

[^4]: https://math.stackexchange.com/questions/293527/how-to-check-if-a-8-puzzle-is-solvable