from threading import Thread
import os
import time
from functools import partial

from BoardInstance import BoardInstance
from search import a_star


def test_instance(start: BoardInstance, goal: BoardInstance, result_list: list):
    result_list.append(a_star(start, goal))


if __name__ == "__main__":
    N = int(input("N: "))
    print_pretty = partial(print, sep="\n", end="\n\n")

    while True:
        goal = BoardInstance.random(N)
        # current = BoardInstance.random(N)
        start = goal.drunk_walk(10)

        print_pretty("\nSTART STATE", start)
        print_pretty("GOAL STATE", goal)
        # print_pretty(f"Solvable: {goal.is_reachable(start)}")

        result_list = []
        thread = Thread(target=test_instance, args=(start, goal, result_list))
        thread.start()
        thread.join(10)

        print("Search result: ", end="")
        print_pretty("SOLVED!" if result_list else "TIMEOUT!")

        if result_list:
            path = result_list[0]
            print("PATH")
            for state in path:
                print(state)
            print(f"{len(path)} steps")

        input("\nPress Enter to continue... ")
        
        os.system("clear")