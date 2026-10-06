"""
Oefening 2: Sliding Puzzle (8-puzzle)
======================================
Implementeer de sliding puzzle en los hem op met BFS/DFS.
"""
import numpy as np
from collections import deque

class SlidingPuzzle:
    GRIDSIZE = 3
    EMPTY = 0

    GOAL = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    def __init__(self, game):
        self.Game = np.array(game)

    def possible_new_configurations(self):
        # TODO: geef alle nieuwe configuraties door het lege vakje te verschuiven
        moves = [
        [-1, 0],  #naar omhoog
        [1, 0],   #naar omlaag
        [0, -1],  #naar links
        [0, 1 ]   #naar rechts
        ]
        lijst_puzzels = []
        rij, kol = self.locate_empty()
        for delta_r,delta_k in moves:
            new_rij = rij + delta_r
            new_kol = kol + delta_k
            if 0 <= new_rij < 3 and 0 <= new_kol < 3:
                new_puzzle = self.duplicate()
                new_puzzle.Game[rij][kol] = new_puzzle.Game[new_rij][new_kol]
                new_puzzle.Game[new_rij][new_kol] = self.Game[rij][kol]   
                lijst_puzzels.append(new_puzzle)

        return lijst_puzzels

    def locate_empty(self):
        for row in range(self.GRIDSIZE):
            for col in range(self.GRIDSIZE):
                if self.Game[row][col] == self.EMPTY:
                    return (row, col)
        raise Exception("Geen leeg vakje!")

    def manhattan_distance(self):
        # TODO: bereken de Manhattan-afstand tot de goal-configuratie
        return 0

    def is_goal(self):
        return np.array_equal(self.Game, self.GOAL)

    def duplicate(self):
        return SlidingPuzzle([[self.Game[r][c] for c in range(self.GRIDSIZE)] for r in range(self.GRIDSIZE)])

    def log(self):
        print("---")
        for row in self.Game:
            print(", ".join(str(int(x)) for x in row))
        print("---")


def solve_puzzle(start_puzzle):
    # TODO: los de puzzel op met BFS
    queue = deque([start_puzzle])
    visited = set()

    while queue:
        puzzle = queue.popleft()
        if puzzle.is_goal():
            return puzzle
        
        config = str(puzzle.Game)
        if config in visited:
            continue

        visited.add(config)
        new_configurations = puzzle.possible_new_configurations()
        for new_puzzle in new_configurations:
            queue.append(new_puzzle)
    return None




if __name__ == "__main__":
    game = [
        [1, 2, 3],
        [4, 5, 0],
        [7, 8, 6]
    ]
    puzzle = SlidingPuzzle(game)
    print("Startconfiguratie:")
    puzzle.log()
    mogelijk = SlidingPuzzle.possible_new_configurations(puzzle)
    for p in mogelijk:
        p.log()

    oplossing = solve_puzzle(puzzle)
    print("Oplossing:")
    oplossing.log()