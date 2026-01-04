import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Distance from start
        self.h = 0  # Heuristic (estimated distance to end)
        self.f = 0  # Total cost (g + h)

    def __lt__(self, other):
        return self.f < other.f

def astar(grid, start, end):
    start_node = Node(start)
    end_node = Node(end)
    
    open_list = []
    closed_set = set()
    
    heapq.heappush(open_list, start_node)
    
    while open_list:
        current_node = heapq.heappop(open_list)
        closed_set.add(current_node.position)
        
        if current_node.position == end_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]
        
        (x, y) = current_node.position
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        
        for next_pos in neighbors:
            if next_pos[0] < 0 or next_pos[0] >= len(grid) or \
               next_pos[1] < 0 or next_pos[1] >= len(grid[0]) or \
               grid[next_pos[0]][next_pos[1]] == 1 or \
               next_pos in closed_set:
                continue
                
            neighbor = Node(next_pos, current_node)
            neighbor.g = current_node.g + 1
            neighbor.h = abs(neighbor.position[0] - end_node.position[0]) + \
                         abs(neighbor.position[1] - end_node.position[1])
            neighbor.f = neighbor.g + neighbor.h
            
            if any(open_node.position == neighbor.position and neighbor.g > open_node.g for open_node in open_list):
                continue
                
            heapq.heappush(open_list, neighbor)
            
    return None

# Example Usage
if __name__ == "__main__":
    # 0 = Path, 1 = Wall
    game_map = [
        [0, 0, 0, 0, 1],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start = (0, 0)
    end = (4, 4)
    path = astar(game_map, start, end)
    print(f"Path found: {path}")
