import numpy as np
import random
from collections import deque

class Agent:
    def __init__(self,width,height) -> None:
        self.maze = self.generate_random_maze(width=width,height=height)
        self.maze[0][0]=1
        self.pos= (0,0)
        while True:
            goal_pos = (random.randint(0, width-1), random.randint(0, height-1))
            if goal_pos != self.pos:
                self.goal_pos = goal_pos
                break
        self.maze[goal_pos[0]][goal_pos[1]]=1
        self.visited = np.zeros((width, height), dtype=bool)
        print(goal_pos)
        self.path = list()
        
    def animate_maze(self):
        for pos in reversed(self.path):
            
            self.print_maze()
            self.pos=pos
                
    ## ai generated
    def print_maze(self):
        """Print the maze in a human-readable way."""
        for i in range(self.maze.shape[0]):
            for j in range(self.maze.shape[1]):
                if (i, j) == self.pos:
                    print("S", end=" ")  # Starting Aposition
                elif (i, j) == self.goal_pos:
                    print("G", end=" ")  # Goal position
                elif self.maze[i, j] == 1:
                    print(".", end=" ")  # Open space
                else:
                    print("#", end=" ")  # Wall
            print()  # Newline after each row
        print("#########")  
        
    def bfs(self):
        queue = deque([self.pos])
        self.visited[self.pos[0],self.pos[1]] = True
        came_from = dict()
        came_from[self.pos] = None
        
        while queue:
            current_pos = queue.popleft()
            if current_pos == self.goal_pos:
                self.print_path(path=came_from,cpos=self.goal_pos)
                print("Goal reached")
                
                return True
            neigbors=self.get_neighbors(current_pos)
            
            for neighbor in neigbors:
                
                x, y = neighbor
                if not self.visited[x, y] and self.maze[x, y] == 1:
                    came_from[neighbor] = current_pos
                    queue.append(neighbor)
                    self.visited[x, y] = True
        print("Goal not reachable")
        return False
            
    def print_path(self, path: dict, cpos: tuple):
        pos  = path[cpos]
        if pos is None:
            self.path.append(cpos)  
            return
        self.path.append(cpos)
        self.print_path(path=path, cpos=pos)
        
    def get_neighbors(self, pos):
        x, y = pos
        neighbors = []
        if x > 0:
            neighbors.append((x-1, y))
        if x < self.maze.shape[0] - 1:
            neighbors.append((x+1, y))
        if y > 0:
            neighbors.append((x, y-1))
        if y < self.maze.shape[1] - 1:
            neighbors.append((x, y+1))
        return neighbors
        
    def generate_random_maze(self,width, height):
        # Randomly generate a maze with walls (0) and open spaces (1)
        coordinates = (width,height)
        maze =np.ones(coordinates,dtype=np.int8)
        maze = self._modify_random_elements_(maze,20,0)
        return maze
        
    def _modify_random_elements_(self,np_array, percentage:int, new_value):
        total_elements = np_array.size
        num_elements_to_modify = int(total_elements * percentage / 100)
        
        np.put(np_array,np.random.choice(total_elements, num_elements_to_modify, replace=False),new_value)
        
        return np_array
    
    def run(self):
        self.bfs()
        self.animate_maze()
        
agent = Agent(5,5)
agent.run()