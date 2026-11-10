
from collections import deque


def is_goal(state):
    bank = {(0, 0), (0, 1), (1, 0), (1, 1)}

    for coin in state:
        if coin in bank:
            return False

    return True


def get_successors(state):
    successors = []

    for coin in state:
        row, col = coin

        below = (row + 1, col)
        right = (row, col + 1)

        if below not in state and right not in state:

            new_state = set(state)

            new_state.remove(coin)
            new_state.add(below)
            new_state.add(right)

            successors.append(frozenset(new_state))

    return successors


def bfs(max_moves=10):

    start = frozenset({
        (0, 0),
        (0, 1),
        (1, 0)
    })

    queue = deque()
    queue.append((start, 0))

    visited = {start}

    while queue:

        state, moves = queue.popleft()

        
        if is_goal(state):
            print("Oplossing gevonden!")
            print("Aantal zetten:", moves)
            return state

       
        if moves >= max_moves:
            continue

        for successor in get_successors(state):

            if successor not in visited:
                visited.add(successor)
                queue.append((successor, moves + 1))

    print("Geen oplossing gevonden binnen", max_moves, "zetten.")
    print("Aantal onderzochte toestanden:", len(visited))

    return None


bfs(max_moves=15)
