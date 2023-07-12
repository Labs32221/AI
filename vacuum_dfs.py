class State:
    def __init__(self, agent_position, room_a, room_b):
        self.agent_position = agent_position
        self.room_a = room_a
        self.room_b = room_b
        self.left = None
        self.right = None
        self.clean = None

    def get_states(self):
        next_states = []
        if self.left:
            next_states.append(self.left)
        if self.right:
            next_states.append(self.right)
        if self.clean:
            next_states.append(self.clean)
        return next_states


class Agent:
    def __init__(self, first_state, goal_state1, goal_state2):
        self.first_state = first_state
        self.goal_state1 = goal_state1
        self.goal_state2 = goal_state2

    def run_dfs(self):
        visited = set()
        return self.dfs(self.first_state, visited)

    def dfs(self, current_state, visited):
        if current_state in visited:
            return False

        visited.add(current_state)

        print("\nMove to state", current_state.state_name)
        self.prompt_attributes(current_state)

        if current_state == self.goal_state1 or current_state == self.goal_state2:
            print("Final State:", current_state.state_name)
            return True

        next_states = current_state.get_states()

        for state in next_states:
            if self.dfs(state, visited):
                return True

        return False

    def prompt_attributes(self, current):
        #print("Vacuum is in room", str(current.agent_position))
        if current.room_a:
            print("Room A is clean")
        else:
            print("Room A is dirty")

        if current.room_b:
            print("Room B is clean")
        else:
            print("Room B is dirty")


def main():
    # Input Section
    print("Enter the initial state of each room where: 1 - Clean | 2 - Dirty")
    status_a = int(input("Enter the state of the first room: ")) == 1
    status_b = int(input("Enter the state of the second room: ")) == 1

    print("Enter the initial position of the vacuum where: 1 - Room A | 2 - Room B")
    position = int(input("Enter the initial position: "))

    # Create state instances
    state1 = State(None, status_a, status_b)
    state2 = State(None, status_a, status_b)
    state3 = State(None, status_a, status_b)
    state4 = State(None, status_a, status_b)
    state5 = State(None, status_a, status_b)
    state6 = State(None, status_a, status_b)
    state7 = State(None, status_a, status_b)
    state8 = State(None, status_a, status_b)

    # Setup and connect each state
    state1.agent_position = state1
    state1.right = state2
    state1.clean = state5
    state1.state_name = "State 1"

    state2.agent_position = state2
    state2.left = state2
    state2.right = state4
    state2.state_name = "State 2"

    state3.left = state3
    state3.right = state4
    state3.clean = state7
    state3.state_name = "State 3"

    state4.agent_position = state4
    state4.left = state4
    state4.right = state4
    state4.state_name = "State 4"

    state5.left = state5
    state5.right = state6
    state5.state_name = "State 5"

    state6.agent_position = state6
    state6.left = state6
    state6.right = state8
    state6.state_name = "State 6"

    state7.left = state7
    state7.right = state8
    state7.state_name = "State 7"

    state8.agent_position = state8
    state8.left = state8
    state8.right = state8
    state8.state_name = "State 8"

    # Run agent
    initial_state = None
    if position == 1:
        if status_a and status_b:
            initial_state = state7
        elif status_a:
            initial_state = state5
        elif status_b:
            initial_state = state3
        else:
            initial_state = state1
    elif position == 2:
        if status_a and status_b:
            initial_state = state8
        elif status_a:
            initial_state = state6
        elif status_b:
            initial_state = state4
        else:
            initial_state = state2
    else:
        print("\nInitial state is unknown...")
        return

    agent = Agent(initial_state, state7, state8)
    if agent.run_dfs():
        print("\nAgent achieved the goal.")
    else:
        print("\nAgent failed to reach the goal.")


if __name__ == "__main__":
    main()
