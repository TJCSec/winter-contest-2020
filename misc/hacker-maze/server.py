import select
import sys
from random import shuffle, randrange
import mazemaker

def input_with_timeout(prompt, timeout):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    ready, _, _ = select.select([sys.stdin], [],[], timeout)
    if ready:
        return sys.stdin.readline().rstrip('\n')
    raise TimeoutExpired

def check(string, maze):
    directions = {"R": 1, "L": -1, "U": -41, "D": 41}
    start = maze.index("S")
    for index, direction in enumerate(string):
        start += directions[direction]
        if maze[start] == "#":
            return False
        if maze[start] == "S":
            return False
        if maze[start] == "E":
            return True if index == len(string) - 1 else False
    return False    

flag = open('flag.txt', 'r').read()

print("Any% HackerMaze Speedrun")
print("R means right, U means up, L means left, D means down.")
print("You start at S, and your goal is E.")
print("Enter in a solution to the maze below: ")

maze = mazemaker.Maze()
maze.generator = mazemaker.Prims(10, 20) #dimensions are actually 21x41
maze.generate()
maze.generate_entrances()

result = maze.tostring(True, False)
print(result)

actual = result.replace("\n", "").strip()

print("Use this format: RDLURDLURDLU")
print("You have three seconds, starting now.")

try:
    answer = input_with_timeout("Enter your answer: ", 3)
    if check(answer, actual):
        print("Not bad.")
        print(flag)
    else:
        print("Incorrect path.")
except Exception as e:
    print("\nToo slow!")

