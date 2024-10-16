class RatRobot:

  def __init__(self, environment, initial_state, goal_state):
    """
    Initializes the robot with a given environment (maze),
    starting state, and goal state.
    Sets up the initial parameters for the robot.
    """
    self.env = environment
    self.current_state = initial_state
    self.goal_state = goal_state

  def get_next_state(self, state, action):
    """
    Determines the next state based on the current state
    and action (up, down, left, right).
    Returns the new state or
    the same state if the action is invalid or out of bounds.
    """
    row, col = state
    if action == "up":
      return (row - 1, col)
    elif action == "down":
      return (row + 1, col)
    elif action == "left":
      return (row, col - 1)
    elif action == "right":
      return (row, col + 1)
    else:
      return state

  def get_possible_actions(self, state):
      """
      Returns a list of valid actions (up, down, left, right) that
      the robot can take from the current state,
      ensuring it doesn't move into walls or out of the maze.
      """
      row, col = state
      possible_actions = []
      if row > 0 and self.env[row - 1][col] != 0:
        possible_actions.append("up")
      if row < len(self.env) - 1 and self.env[row + 1][col] != 0:
        possible_actions.append("down")
      if col > 0 and self.env[row][col - 1] != 0:
        possible_actions.append("left")
      if col < len(self.env[0]) - 1 and self.env[row][col + 1] != 0:
        possible_actions.append("right")
      return possible_actions

  def choose_action(self, visited_states):
    """
    Selects the first action that leads to a new,
    unvisited state from the possible actions list.
    If no valid action is found, returns None.
    """
    possible_actions = self.get_possible_actions(self.current_state)
    best_action = None
    for action in possible_actions:
      next_state = self.get_next_state(self.current_state, action)
      if next_state not in visited_states:
        best_action = action
        break
    return best_action

  def run(self):
    """
    Runs the robot until it reaches the goal state or gets stuck.
    Keeps track of visited states and appends the chosen actions to a list,
    which is returned at the end.
    """
    actions_taken = []
    visited_states = set()
    while self.current_state != self.goal_state:
      visited_states.add(self.current_state)
      action = self.choose_action(visited_states)
      if action is None:
        print("No action is possible! !!! Robot Stucked !!!")
        break
      actions_taken.append(action)
      self.current_state = self.get_next_state(self.current_state, action)
    return actions_taken

# Define the maze parameters
environment = [ [1,1,1], [1,0,1], [1,1,1] ]
initial_state = (0, 0)
goal_state = (2, 2)

# Create the agent
agent = RatRobot(environment, initial_state, goal_state)

# Run the agent and print the actions
actions = agent.run()
print("Actions taken:", actions)
