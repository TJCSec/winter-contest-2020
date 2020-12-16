from heapq import heappop, heappush
from collections import deque

def replaceAtIndex(board, index, newChar):
    if index == 0:
        return newChar + board[1:]
    return board[:index] + newChar + board[index+1:]


def children(index, board):
    directions = {"R": 1, "L": -1, "U": -41, "D": 41}
    allowed = ["R", "L", "U", "D"]
    if index >= 821:
        allowed.remove("D")
        allowed.remove("R")
        allowed.remove("L")
    elif index <= 40:
        allowed.remove("U")
        allowed.remove("R")
        allowed.remove("L")
    else:
        if board[index - 1] == "#":
            allowed.remove("L")
        if board[index + 1] == "#":
            allowed.remove("R")
        if board[index - 41] == "#":
            allowed.remove("U")
        if board[index + 41] == "#":
            allowed.remove("D")
    
    result = []
    for x in allowed:
        result.append(index + directions[x])
    return result

    
def bfs(board):
    initial = board.index("S")
    end = board.index("E")
    visited = set()
    visited.add(initial)
    fringe = deque()
    fringe.append(initial)
    path = { initial: None }

    while len(fringe) > 0:
        node = fringe.popleft()
        visited.add(node)
        if node == end:
            finish = []
            finish.append(node)
            while path.get(node) is not None:
                node = path.get(node)
                finish.append(node)
            return finish
        
        for index in children(node, board):
            if index not in visited:
                fringe.append(index)
                visited.add(index)
                path[index] = node
    return None

def get_solution(maze):
    directions = {1: "R", -1: "L", -41: "U", 41: "D"}
    path = bfs(maze)[::-1][1:]
    path_string = ""
    prev = maze.index("S")
    for x in path:
        diff = x - prev
        path_string += directions[diff]
        prev = x
    return path_string



from pwn import *
connection = remote('0.0.0.0', 30002) # localhost
text = str(connection.recvuntil("Enter your answer: "))
lines = text.split("\\n")
print(lines)
maze = ''
for line in lines:
    if "#" in line:
        maze += line
print(maze)
solution = get_solution(maze)
connection.sendline(solution)
print(connection.recvline())
print(connection.recvline())
