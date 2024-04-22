from __future__ import annotations
import random
import copy

class BoardInstance:
    """
    An instance of the N-puzzle board.
    
    Attributes:
        matrix: A square matrix (2D list). Contains all values from 1 to N,
            along with a `None` element denoting the blank tile.
        blank_position (tuple[int, int]): Indices of the blank tile in the 
            matrix.
    """

    def random(N: int) -> BoardInstance:
        """Returns a randomly-arranged BoardInstance for N-puzzle.
        Throws an Exception if (N + 1) is not a perfect-square.
        """
        edge_length = (N + 1)**0.5
        if edge_length % 1 != 0:
            raise Exception(f"(N + 1) = {N + 1} is not a perfect square.")

        tiles = [i for i in range(1, N + 1)] + [None] # N tiles and a blank (None)
        random.shuffle(tiles) # shuffle the tiles before placement in the matrix

        edge_length = int(edge_length) # 'twas a round integer, but stored as float
        random_matrix = [[0] * edge_length for i in range(edge_length)]  

        # place the tiles in the matrix
        for i in range(edge_length):
            for j in range(edge_length):
                random_matrix[i][j] = tiles.pop()
        
        return BoardInstance(random_matrix)


    def __init__(self, matrix: list[list[int]], blank_position: tuple[int, int] = None):
        if blank_position is None:
            # go row-by-row to find the blank tile
            for i, row in enumerate(matrix):
                try:
                    j = row.index(None)
                    blank_position = (i, j)
                    break
                except:
                    pass 
        
        self.blank_position = blank_position
        self.matrix = matrix


    def drunk_walk(self, n_steps: int) -> BoardInstance:
        result = copy.deepcopy(self)
        for _ in range(n_steps):
            result = random.choice(list(result.neighbors()))
        return result


    def neighbors(self) -> list:
        """Return a list of neighboring BoardInstance states."""
        (x, y) = self.blank_position
        
        # blank tile can be swapped with its neighboring tiles
        candidates = ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))

        # every x/i and y/j coordinate must be within bounds
        bounds = range(len(self.matrix))

        result = []
        for (i, j) in candidates:
            # if the neighbor is out-of-bounds, continue
            if i not in bounds or j not in bounds:
                continue

            # copy the current matrix
            neighbor_matrix = copy.deepcopy(self.matrix)

            # swap the blank tile with the neighbor
            neighbor_matrix[i][j], neighbor_matrix[x][y] = None, neighbor_matrix[i][j]

            # add corresponding BoardInstance to the result
            result.append(BoardInstance(neighbor_matrix, blank_position=(i, j)))

        return result
    

    def manhattan_distance(self, other) -> int:
        """Return the sum of Manhattan distances of corresponding tiles."""
        # to avoid O(n^4) computation, create a map for `other` BoardInstance
        value_to_index = {}
        for i in range(len(other.matrix)):
            for j in range(len(other.matrix[0])):
                value_to_index[other.matrix[i][j]] = (i, j)

        result = 0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                (i1, j1) = value_to_index[self.matrix[i][j]]
                result += abs(i - i1) + abs(j - j1)
        return result
    

    def is_reachable(self, other) -> bool:
        """Returns True if there's any path at all from `other` to self.
        https://math.stackexchange.com/questions/293527/how-to-check-if-a-8-puzzle-is-solvable
        """
        A = [element for row in self.matrix for element in row]

        B = [element for row in other.matrix for element in row]
        B_map = {B[i]: i for i in range(len(B))}

        # count the number of inverted pairs in A from POV of B
        inversions = 0
        for i in range(len(A)):
            if A[i] is None:
                continue
            for j in range(i + 1, len(A)):
                if A[j] is None:
                    continue
                if B_map[A[j]] < B_map[A[i]]:
                    inversions += 1

        # solvable if there are an even number of inverted pairs
        return inversions % 2 == 0


    def __hash__(self) -> int:
        """Return a hash value for the BoardInstance.
        Enables addition of BoardInstance objects to sets.
        Any arbitrary method for generating hash values will do.
        For now, the hash value is taken as the row-index of the blank tile.
        """
        return self.blank_position[0]
    

    def __eq__(self, other) -> bool:
        return self.matrix == other.matrix
    

    def __lt__(self, other) -> bool:
        return self.blank_position[0] < other.blank_position[0]
    
    
    def __str__(self) -> str:
        """Return a string representation. Used by print()."""
        width = len(str(len(self.matrix)**2 - 1))
        line = "-" * ((width + 1) * len(self.matrix) - 1)
        
        matrix_string = ""
        for row in self.matrix:
            for tile in row:
                s = str(tile) if tile is not None else "_" * width
                matrix_string += s + " " * (width - len(s) + 1)
            matrix_string += "\n"

        return line + "\n" + matrix_string + line