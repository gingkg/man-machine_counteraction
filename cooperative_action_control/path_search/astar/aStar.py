import draw
import math


# Enter your code here. Read input from STDIN. Print output to STDOUT
class Node:
    def __init__(self, value, point):
        self.value = value
        self.point = point
        self.parent = None
        self.H = 0
        self.G = 0

    def move_cost(self, other):
        if self.value == '.' and other.value == '.':
            return 1
        else:
            return 10


def children(point, grid):
    x, y = point.point
    direction = [(x-1, y), (x, y-1), (x, y+1), (x+1, y)]
    links = []
    for d in direction:
        if 0 <= d[0] < len(grid) and 0 <= d[1] < len(grid[x]):
            if grid[d[0]][d[1]].value != '%':
                links.append(grid[d[0]][d[1]])
    return links


def distance(point, point2, way="manhattan"):
    if way == "manhattan":
        return abs(point.point[0] - point2.point[0]) + abs(point.point[1] - point2.point[1])
    elif way == "euclidean":
        return math.sqrt((point.point[0] - point2.point[0]) ** 2 + (point.point[1] - point2.point[1]) ** 2)
    else:
        raise ValueError('No Way')


def a_star(start, goal, grid):
    # The open and closed sets
    openset = set()
    closeset = set()
    # Current point is the starting point
    current = start
    # Add the starting point to the open set
    openset.add(current)
    # While the open set is not empty
    while openset:
        # Find the item in the open set with the lowest G + H score
        current = min(openset, key=lambda o:o.G + o.H)
        # If it is the item we want, retrace the path and return it
        if current == goal:
            path = []
            while current.parent:
                path.append(current)
                current = current.parent
            path.append(current)
            # 倒转
            return path[::-1]
        # Remove the item from the open set
        openset.remove(current)
        # Add it to the closed set
        closeset.add(current)
        # Loop through the node's children/siblings
        for node in children(current, grid):
            if node in closeset:
                continue
            # Otherwise if it is already in the open set
            if node in openset:
                # Check if we beat the G score
                new_g = current.G + current.move_cost(node)  # ???
                if node.G > new_g:
                    # If so, update the node to have a new parent
                    node.G = new_g
                    node.parent = current
            else:
                # If it isn't in the open set, calculate the G and H score for the node
                node.G = current.G + current.move_cost(node)
                node.H = distance(node, goal, "manhattan")
                # Set the parent to our current item
                node.parent = current
                # Add it to the set
                openset.add(node)
    # Throw an exception if there is no path
    raise ValueError('No Path Found')


def next_move(pacman, food, grid):
    # Convert all the points to instances of Node
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            grid[x][y] = Node(grid[x][y], (x, y))
    # Get the path
    path = a_star(grid[pacman[0]][pacman[1]], grid[food[0]][food[1]], grid)
    # Output the path
    print(len(path) - 1)
    print(f"H: {path[len(path) - 1].H}")
    print(f"G: {path[len(path) - 1].G}")
    for node in path:
        x, y = node.point
        print([x, y])
        
    draw.draw_map(grid, path, pacman, food)


def main(default):
    if default:
        pacman_x, pacman_y = 0, 0
        food_x, food_y = 9, 9
        x, y = 10, 10
        # grid = [['.', '.', '.', '%', '.', '.', '.', '.', '.', '.'],
        #         ['.', '.', '.', '%', '.', '.', '.', '.', '.', '.'],
        #         ['.', '.', '.', '%', '.', '.', '.', '.', '.', '.'],
        #         ['.', '.', '.', '%', '.', '.', '.', '.', '.', '.'],
        #         ['.', '.', '.', '%', '.', '%', '.', '.', '.', '.'],
        #         ['.', '.', '.', '%', '.', '.', '.', '.', '.', '.'],
        #         ['.', '.', '%', '%', '.', '%', '.', '.', '.', '.'],
        #         ['.', '%', '.', '.', '.', '.', '.', '%', '.', '.'],
        #         ['.', '%', '.', '%', '.', '%', '.', '.', '.', '.'],
        #         ['.', '.', '.', '.', '.', '%', '.', '.', '.', '.']]
        grid = [['.', '.', '.', '%', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '%', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '%', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]
    else:
        pacman_x, pacman_y = [int(i) for i in input().strip().split()]  # 吃豆人起始位置
        food_x, food_y = [int(i) for i in input().strip().split()]  # 食物位置
        x, y = [int(i) for i in input().strip().split()]  # 地图大小

        # 输入地图, '.'可以走，'%'不可以走
        grid = []
        for i in range(0, x):
            grid.append(list(input().strip()))  # 注意输入中间不能有空格

    next_move((pacman_x, pacman_y), (food_x, food_y), grid)


if __name__ == '__main__':
    main(True)


