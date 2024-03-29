# N-Puzzle Problem
_4<sup>th</sup> semester AI project_ 

N-puzzle is a generalization of the 8-puzzle game to larger frames. The puzzle starts with a square frame consisting of $(n - 1)$ tiles inside. The tiles are numbered from $1$ 1o $(n - 1)$. There is also one empty slot in the frame not occupied by any tile. 

In each move, any tile with an adjacent edge to the empty slot may be moved there. Our goal is to arrange the randomly placed tiles in numerical order.

The game may be modelled as a state-search problem and solved using any standard graph traversal algorithm.[^1]

## References

[^1]: Russell, S., & Norvig, P. (2020). _Artificial Intelligence: A Modern Approach_ (pp. 70-71).