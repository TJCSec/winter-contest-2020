# Code is from https://github.com/theJollySin/mazelib, modified to remove some unnecessary things and 
# remove numpy dependency

from random import randrange
import abc

class Maze:
    """ This is a master object meant to hold a rectangular, 2D maze.
    This object includes the methods used to generate and solve the maze,
    as well as the start and end points.
    """

    def __init__(self, seed=None):
        self.generator = None
        self.grid = None
        self.start = None
        self.end = None
        self.transmuters = []
        self.solver = None
        self.solutions = None
        self.prune = True

    def generate(self):
        """ public method to generate a new maze, and handle some clean-up
        Returns: None
        """
        assert not (self.generator is None), 'No maze-generation algorithm has been set.'

        self.grid = self.generator.generate()
        self.start = None
        self.end = None
        self.solutions = None

    def generate_entrances(self, start_outer=True, end_outer=True):
        """ Generate maze entrances. Entrances can be on the walls, or inside the maze.
        Args:
            start_outer (bool): Do you want the start of the maze to be on an outer wall?
            end_outer (bool): Do you want the end of the maze to be on an outer wall?
        Returns: None
        """

        self._generate_outer_entrances()

        if abs(self.start[0] - self.end[0]) + abs(self.start[1] - self.end[1]) < 2:
            self.generate_entrances(start_outer, end_outer)

    def _generate_outer_entrances(self):
        """ Generate maze entrances, along the outer walls.
        Returns: None
        """
        H = 21
        W = 41

        start_side = randrange(4)

        # maze entrances will be on opposite sides of the maze.
        if start_side == 0:
            self.start = (0, randrange(1, W, 2))  # North
            self.end = (H - 1, randrange(1, W, 2))
        elif start_side == 1:
            self.start = (H - 1, randrange(1, W, 2))  # South
            self.end = (0, randrange(1, W, 2))
        elif start_side == 2:
            self.start = (randrange(1, H, 2), 0)  # West
            self.end = (randrange(1, H, 2), W - 1)
        else:
            self.start = (randrange(1, H, 2), W - 1)  # East
            self.end = (randrange(1, H, 2), 0)

    def tostring(self, entrances=False, solutions=False):
        """ Return a string representation of the maze.
        This can also display the maze entrances/solutions IF they already exist.
        Args:
            entrances (bool): Do you want to show the entrances of the maze?
            solutions (bool): Do you want to show the solution to the maze?
        Returns:
            str: string representation of the maze
        """
        if self.grid is None:
            return ''

        # build the walls of the grid
        txt = []
        for row in self.grid:
            txt.append(''.join(['#' if cell else '.' for cell in row]))

        # insert the start and end points
        if entrances and self.start and self.end:
            r, c = self.start
            txt[r] = txt[r][:c] + 'S' + txt[r][c + 1:]
            r, c = self.end
            txt[r] = txt[r][:c] + 'E' + txt[r][c + 1:]

        # if extant, insert the solution path
        if solutions and self.solutions:
            for r, c in self.solutions[0]:
                txt[r] = txt[r][:c] + '+' + txt[r][c + 1:]

        return '\n'.join(txt)

    def __str__(self):
        """ display maze walls, entrances, and solutions, if available
        Returns:
            str: string representation of the maze
        """
        return self.tostring(True, True)

    def __repr__(self):
        """ display maze walls, entrances, and solutions, if available
        Returns:
            str: string representation of the maze
        """
        return self.__str__()

class MazeGenAlgo:
    __metaclass__ = abc.ABCMeta

    def __init__(self, h, w):
        assert (w >= 3 and h >= 3), 'Mazes cannot be smaller than 3x3.'
        self.h = h
        self.w = w
        self.H = (2 * self.h) + 1
        self.W = (2 * self.w) + 1

    @abc.abstractmethod
    def generate(self):
        return None

    """ All of the methods below this are helper methods,
    common to many maze-generating algorithms.
    """

    def _find_neighbors(self, r, c, grid, is_wall=False):
        """ Find all the grid neighbors of the current position; visited, or not.
        Args:
            r (int): row of cell of interest
            c (int): column of cell of interest
            grid (np.array): 2D maze grid
            is_wall (bool): Are we looking for neighbors that are walls, or open cells?
        Returns:
            list: all neighboring cells that match our request
        """
        ns = []

        if r > 1 and grid[r - 2][c] == is_wall:
            ns.append((r - 2, c))
        if r < self.H - 2 and grid[r + 2][c] == is_wall:
            ns.append((r + 2, c))
        if c > 1 and grid[r][c - 2] == is_wall:
            ns.append((r, c - 2))
        if c < self.W - 2 and grid[r][c + 2] == is_wall:
            ns.append((r, c + 2))

        return ns


class Prims(MazeGenAlgo):
    """
    The Algorithm
    1. Choose an arbitrary cell from the grid, and add it to some
        (initially empty) set visited nodes (V).
    2. Randomly select a wall from the grid that connects a cell in
        V with another cell not in V.
    3. Add that wall to the Minimal Spanning Tree (MST), and the edge's other cell to V.
    4. Repeat steps 2 and 3 until V includes every cell in G.
    """

    def __init__(self, h, w):
        super(Prims, self).__init__(h, w)

    def generate(self):
        """ highest-level method that implements the maze-generating algorithm
        Returns:
            np.array: returned matrix
        """
        grid = [[1 for y in range(self.W)] for x in range(self.H)]

        # choose a random starting position
        current_row = randrange(1, self.H, 2)
        current_col = randrange(1, self.W, 2)
        grid[current_row][current_col] = 0

        # created a weighted list of all vertices connected in the graph
        neighbors = self._find_neighbors(current_row, current_col, grid, True)

        # loop over all current neighbors, until empty
        visited = 1

        while visited < self.h * self.w:
            # find neighbor with lowest weight, make it current
            nn = randrange(len(neighbors))
            current_row, current_col = neighbors[nn]
            visited += 1
            grid[current_row][current_col] = 0
            neighbors = neighbors[:nn] + neighbors[nn + 1:]
            # connect that neighbor to a random neighbor with grid[posi] == 0
            nearest_n0, nearest_n1 = self._find_neighbors(current_row, current_col, grid)[0]
            grid[(current_row + nearest_n0) // 2][(current_col + nearest_n1) // 2] = 0

            # find all unvisited neighbors of current, add them to neighbors
            unvisited = self._find_neighbors(current_row, current_col, grid, True)
            neighbors = list(set(neighbors + unvisited))

        return grid