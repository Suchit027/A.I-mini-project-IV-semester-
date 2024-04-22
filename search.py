from BoardInstance import BoardInstance

from heapq import heappush, heappop
from collections import defaultdict

def backtrack(end: BoardInstance, prev: dict) -> list:
    """Return backtracked path
    Path goes from `start` to `end`, constructed using parents from `prev`.
    `start` is any node such that `prev[start] = None`.
    """
    current = end
    path = []

    while prev[current]:
        path.append(current)
        current = prev[current]
    
    path.append(current)
    return path[::-1]


def a_star(start: BoardInstance, goal: BoardInstance) -> list[BoardInstance]:
    """Return a list of BoardConfigurations from start to solved"""
    dist = defaultdict(lambda: float("inf"))  # initial distance estimates
    dist[start] = 0

    prev = defaultdict(lambda: None)
    prev[start] = None

    frontier = [(0, start)] # "frontier" to be explored 
    closed = set()

    while frontier:
        priority_current, current = heappop(frontier)
        
        if current == goal:
            return backtrack(current, prev)

        closed.add(current)

        for neighbor in current.neighbors():
            if neighbor in closed:
                continue

            alt_dist = dist[current] + 1 
            if alt_dist < dist[neighbor]:
                dist[neighbor] = alt_dist
                prev[neighbor] = current
                priority = alt_dist + neighbor.manhattan_distance(goal)
                heappush(frontier, (priority, neighbor)) 

    return None