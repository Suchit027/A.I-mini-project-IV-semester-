from BoardInstance import BoardInstance
from search import a_star

import time
import os

def prompt(message: str):
    print(message, end="")
    for i in range(3):
        time.sleep(1)
        print(".", end="")
    time.sleep(1)


def show_hint(current: BoardInstance, goal: BoardInstance):
    path = a_star(current, goal)
    print("\nHINT", path[1], sep="\n")
    i = input("Press Enter to continue... ")


def play(current: BoardInstance, move: str):
    direction = {"a": (0, -1), "d": (0, 1), "w": (-1, 0), "s": (1, 0)}

    if move in direction:
        (i, j) = current.blank_position
        (di, dj) = direction[move]

        bounds = range(len(current.matrix))
        if (i + di) in bounds and (j + dj) in bounds:
            current.matrix[i][j] = current.matrix[i + di][j + dj]
            current.matrix[i + di][j + dj] = None
            current.blank_position = (i + di, j + dj)
            return True
    
    return False


def display_state(current, goal, n_moves, n_hints):
    os.system("clear")
    
    print(f"Moves: {n_moves}",
          f"Hints: {n_hints}",
          "\nGOAL STATE", goal,
          "\nCURRENT STATE", current, 
          sep="\n") # prints stuff


def main():
    N = int(input("N: "))

    difficulty = int(input("Difficulty [1|2|3]: "))
    if difficulty == 1:
        seed = 10
    elif difficulty == 2:
        seed = 25
    else:
        seed = 50

    # Initialize the current and goal state
    goal = BoardInstance.random(N)
    current = goal.drunk_walk(seed)

    best_path = a_star(current, goal)

    n_moves, n_hints = 0, 0
    display_state(current, goal, n_moves, n_hints)
    while current != goal:
        move = input("\nMove [A|W|S|D|hint]: ").lower() # n_moves the blank tile

        if move == "hint":
            n_hints += 1
            show_hint(current, goal)
        elif move in "awsd":
            if play(current, move): # modifies `current` in-place
                n_moves += 1
        elif move == "q":
            return

        display_state(current, goal, n_moves, n_hints)

    print(f"\nGoal state reached | {n_moves} moves | {n_hints} hints")
    print(f"\nBest path had {len(best_path) - 1} steps")
    score = round(100 * n_moves / (n_moves + len(best_path)), 2)
    print(f"\nSCORE: {score}")

    """print("BEST PATH")
    for state in best_path:
        print(state)"""
    
    i = input("\nPress Enter to continue... ")


if __name__ == "__main__":
    while True:
        try:
            os.system("clear")
            main()
        except Exception as e:
            print(e)
            prompt("Restarting")
