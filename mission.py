from collections import deque

def is_valid_state(state):
    m_left, c_left, m_right, c_right, boat = state
    if (m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0 or
            (m_left != 0 and m_left < c_left) or
            (m_right != 0 and m_right < c_right)):
        return False
    return True
def generate_next_states(state):
    m_left, c_left, m_right, c_right, boat = state
    possible_states = []

    if boat == 'left':
        for m in range(3):
            for c in range(3):
                if m + c > 2 or m + c == 0:
                    continue
                new_state = (m_left - m, c_left - c, m_right + m, c_right + c, 'right')
                if is_valid_state(new_state):
                    possible_states.append(new_state)
    else:
        for m in range(3):
            for c in range(3):
                if m + c > 2 or m + c == 0:
                    continue
                new_state = (m_left + m, c_left + c, m_right - m, c_right - c, 'left')
                if is_valid_state(new_state):
                    possible_states.append(new_state)

    return possible_states
def bfs(start_state, goal_state):
    visited = set()
    queue = deque([(start_state, [])])

    while queue:
        current_state, path = queue.popleft()
        visited.add(current_state)

        if current_state == goal_state:
            return path

        for next_state in generate_next_states(current_state):
            if next_state not in visited:
                queue.append((next_state, path + [next_state]))
                visited.add(next_state)

    return []

def dfs(current_state, goal_state, path, visited):
    visited.add(current_state)

    if current_state == goal_state:
        return path

    for next_state in generate_next_states(current_state):
        if next_state not in visited:
            solution = dfs(next_state, goal_state, path + [next_state], visited)
            if solution:
                return solution
print("dfs solution:")
solution = dfs(start_state, goal_state, [start_state], visited)
if solution:
    for i, state in enumerate(solution):
        print(f"Step {i+1}: {state}")
else:
    print("No solution found.")            

start_state = (3, 3, 0, 0, 'left')
goal_state = (0, 0, 3, 3, 'right')
print("bfs solution:")
solution = bfs(start_state, goal_state)
if solution:
    for i, state in enumerate(solution):
        print(f"Step {i+1}: {state}")
else:
    print("No solution found.")
print()