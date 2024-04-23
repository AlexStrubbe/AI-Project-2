class State:
    def _init_(self, missionaries, cannibals, boat):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        self.parent = None

    def is_valid(self):
        if self.missionaries < 0 or self.cannibals < 0:
            return False
        if self.missionaries > 3 or self.cannibals > 3:
            return False
        if self.missionaries < self.cannibals and self.missionaries > 0:
            return False
        if self.missionaries > self.cannibals and self.missionaries < 3:
            return False
        return True

    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0 and self.boat == 0

    def get_successors(self):
        successors = []
        if self.boat:
            moves = [(-1, 0, 0), (-2, 0, 0), (0, -1, 0), (0, -2, 0), (-1, -1, 0)]
        else:
            moves = [(1, 0, 1), (2, 0, 1), (0, 1, 1), (0, 2, 1), (1, 1, 1)]
        for m, c, b in moves:
            new_state = State(self.missionaries + m, self.cannibals + c, self.boat + b)
            if new_state.is_valid():
                new_state.parent = self
                successors.append(new_state)
        return successors

def breadth_first_search():
    initial_state = State(3, 3, 1)
    if initial_state.is_goal():
        return initial_state
    queue = [initial_state]
    explored = set()
    while queue:
        state = queue.pop(0)
        explored.add(state)
        for successor in state.get_successors():
            if successor not in explored and successor not in queue:
                if successor.is_goal():
                    return successor
                queue.append(successor)
    return None

def print_solution(solution):
    path = []
    while solution:
        path.append(solution)
        solution = solution.parent
    path.reverse()
    for state in path:
        print(f"Missionaries: {state.missionaries}, Cannibals: {state.cannibals}, Boat: {'left' if state.boat else 'right'}")

solution = breadth_first_search()
if solution:
    print("Solution Found!")
    print_solution(solution)
else:
    print("No solution found.")