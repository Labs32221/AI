from heapq import heappop, heappush

class PuzzleNode:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)


def get_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def get_manhattan_distance(row1, col1, row2, col2):
    return abs(row1 - row2) + abs(col1 - col2)


def get_heuristic_value(state, goal_state):
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                value = state[i][j]
                goal_row, goal_col = find_position(goal_state, value)
                h += get_manhattan_distance(i, j, goal_row, goal_col)
    return h


def get_valid_moves(row, col):
    moves = []
    if row > 0:
        moves.append((-1, 0))  # Move blank tile up
    if row < 2:
        moves.append((1, 0))  # Move blank tile down
    if col > 0:
        moves.append((0, -1))  # Move blank tile left
    if col < 2:
        moves.append((0, 1))  # Move blank tile right
    return moves


def get_new_state(state, move):
    row, col = get_blank_position(state)
    new_state = [row[:] for row in state]
    new_row, new_col = row + move[0], col + move[1]
    new_state[row][col] = new_state[new_row][new_col]
    new_state[new_row][new_col] = 0
    return new_state


def print_state(state):
    for row in state:
        print(row)
    print()


def is_goal_state(state, goal_state):
    return state == goal_state


def find_position(state, value):
    for i in range(3):
        for j in range(3):
            if state[i][j] == value:
                return i, j


def get_solution_path(node):
    path = []
    while node is not None:
        path.append(node.state)
        node = node.parent
    path.reverse()
    return path


def solve_puzzle(initial_state, goal_state):
    open_set = []
    closed_set = set()

    h = get_heuristic_value(initial_state, goal_state)
    initial_node = PuzzleNode(initial_state, g=0, h=h)
    heappush(open_set, initial_node)

    while open_set:
        current_node = heappop(open_set)
        closed_set.add(tuple(map(tuple, current_node.state)))

        if is_goal_state(current_node.state, goal_state):
            return get_solution_path(current_node)

        row, col = get_blank_position(current_node.state)
        moves = get_valid_moves(row, col)
        for move in moves:
            new_state = get_new_state(current_node.state, move)
            if tuple(map(tuple, new_state)) not in closed_set:
                g = current_node.g + 1
                h = get_heuristic_value(new_state, goal_state)
                new_node = PuzzleNode(new_state, parent=current_node, g=g, h=h)
                heappush(open_set, new_node)

    return None


# Test the puzzle solver
#initial_state = [[1, 2, 3], [0,4,6], [7, 5, 8]]
#goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

#initial_state = [[2,8,3], [1,6,4], [7, 0,5]]
#goal_state = [[1, 2, 3], [8,0,4], [7, 6,5]]

#initial_state = [[1,2,3], [5,6,0], [7, 8,4]]
#goal_state = [[1, 2, 3], [5,8,6], [0,7,4]]

print("Enter the initial state (0 represents the blank tile):")
initial_state = []
for i in range(3):
    row = list(map(int, input().split()))
    initial_state.append(row)

# Get user input for the goal state
print("Enter the goal state:")
goal_state = []
for i in range(3):
    row = list(map(int, input().split()))
    goal_state.append(row)

solution = solve_puzzle(initial_state, goal_state)

if solution is not None:
    print("Solution found!")
    for state in solution:
        print_state(state)
else:
    print("No solution found.")
