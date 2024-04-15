from threading import Thread
import os
import time
from functools import partial

from BoardInstance import BoardInstance
from search import a_star


def display_path(path):
    for state in path:
        print(state)


def test_instance(start: BoardInstance, goal: BoardInstance, result_list: list):
    result_list.append(a_star(start, goal))


if __name__ == "__main__":
    print_pretty = partial(print, sep="\n", end="\n\n")

    while True:
        start = BoardInstance.random(8)
        goal = BoardInstance.random(8)

        print_pretty("START STATE", start)
        print_pretty("GOAL STATE", goal)
        print_pretty(f"Solvable: {goal.is_reachable(start)}")

        result_list = []
        thread = Thread(target=test_instance, args=(start, goal, result_list))
        thread.start()
        thread.join(3)

        print("Result: ", end="")
        print_pretty("SOLVED!" if result_list else "TIMEOUT!")

        if result_list:
            display_path(result_list[0])

        input("\nPress Enter to continue... ")
        
        os.system("clear")