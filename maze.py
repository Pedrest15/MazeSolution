import tkinter as tk
from enum import Enum
from typing import NamedTuple
import random
from math import sqrt
from generic_search import Node, dfs, node_to_path, bfs, manhattan_distance, a_star

class Cell(str, Enum):
    empty = " "
    blocked = "X"
    barrier_floor = '='
    barrier_wall = '|'
    start = "S"
    goal = "G"
    path = "*"

class MazeLocation(NamedTuple):
    row: int
    column: int
class Maze:
    def __init__(self, 
                rows: int = 10,
                columns: int = 12,
                sparseness: float = 0.2,
                start = MazeLocation(0,1),
                goal = MazeLocation(9,10)) -> None:
        self.rows = rows
        self.columns = columns
        self.start = start
        self.goal = goal
        self.create_maze()

    ''' print("=S==========")
        print("|   XX     |")
        print("| X    XX X|")
        print("|X XXX     |")
        print("|    XX XX |")
        print("| X      X |")
        print("|  X  XXXX |")
        print("|  X X    X|")
        print("| X    X   |")
        print("==========G=")'''

    def create_maze(self) -> None:
        self.grid: list[list[Cell]] = [[Cell.empty for c in range(self.columns)] for r in range(self.rows)]

        for i in range(1, self.rows - 1):
            self.grid[i][0] = Cell.barrier_wall
            self.grid[i][self.columns-1] = Cell.barrier_wall

        for i in range(self.columns):
            self.grid[0][i] = Cell.barrier_floor
            self.grid[self.rows-1][i] = Cell.barrier_floor

        self.grid[self.start.row][self.start.column] = Cell.start
        self.grid[self.goal.row][self.goal.column] = Cell.goal

        self.grid[1][4] = Cell.blocked
        self.grid[1][5] = Cell.blocked
        self.grid[2][2] = Cell.blocked
        self.grid[2][7] = Cell.blocked
        self.grid[2][8] = Cell.blocked
        self.grid[2][10] = Cell.blocked
        self.grid[3][1] = Cell.blocked
        self.grid[3][3] = Cell.blocked
        self.grid[3][4] = Cell.blocked
        self.grid[3][5] = Cell.blocked
        self.grid[4][5] = Cell.blocked
        self.grid[4][6] = Cell.blocked
        self.grid[4][8] = Cell.blocked
        self.grid[4][9] = Cell.blocked
        self.grid[5][2] = Cell.blocked
        self.grid[5][9] = Cell.blocked
        self.grid[6][3] = Cell.blocked
        self.grid[6][6] = Cell.blocked
        self.grid[6][7] = Cell.blocked
        self.grid[6][8] = Cell.blocked
        self.grid[6][9] = Cell.blocked
        self.grid[6][10] = Cell.blocked
        self.grid[7][3] = Cell.blocked
        self.grid[7][5] = Cell.blocked
        self.grid[7][10] = Cell.blocked
        self.grid[8][2] = Cell.blocked
        self.grid[8][7] = Cell.blocked

    def __str__(self) -> str:
        output: str = ""

        for row in self.grid:
            output += "".join([c.value for c in row]) + '\n'
        return output

    def goal_test(self, ml: MazeLocation) -> bool:
        return ml == self.goal

    def successors(self, ml: MazeLocation) -> list[MazeLocation]:
        locations: list[MazeLocation] = []
        
        if (ml.row + 1 < self.rows and self.grid[ml.row + 1][ml.column] != Cell.blocked and
            ml.row + 1 < self.rows and self.grid[ml.row + 1][ml.column] != Cell.barrier_floor and
            ml.row + 1 < self.rows and self.grid[ml.row + 1][ml.column] != Cell.barrier_wall):
            locations.append(MazeLocation(ml.row+1, ml.column))
        
        if (ml.row - 1 >= 0 and self.grid[ml.row - 1][ml.column] != Cell.blocked and
            ml.row - 1 >= 0 and self.grid[ml.row - 1][ml.column] != Cell.barrier_floor and
            ml.row - 1 >= 0 and self.grid[ml.row - 1][ml.column] != Cell.barrier_wall):
            locations.append(MazeLocation(ml.row-1, ml.column))

        if (ml.column + 1 < self.columns and self.grid[ml.row][ml.column+1] != Cell.blocked and
            ml.column + 1 < self.columns and self.grid[ml.row][ml.column+1] != Cell.barrier_floor and
            ml.column + 1 < self.columns and self.grid[ml.row][ml.column+1] != Cell.barrier_wall):
            locations.append(MazeLocation(ml.row, ml.column+1))

        if (ml.column - 1 >= 0 and self.grid[ml.row][ml.column-1] != Cell.blocked and
            ml.column - 1 >= 0 and self.grid[ml.row][ml.column-1] != Cell.barrier_floor and
            ml.column - 1 >= 0 and self.grid[ml.row][ml.column-1] != Cell.barrier_wall):
            locations.append(MazeLocation(ml.row, ml.column-1))

        return locations

    def mark(self, path: list[MazeLocation]):
        for maze_location in path:
            self.grid[maze_location.row][maze_location.column] = Cell.path
        
        self.grid[self.start.row][self.start.column] = Cell.start
        self.grid[self.goal.row][self.goal.column] = Cell.goal

    def clear(self, path: list[MazeLocation]):
        for maze_location in path:
            self.grid[maze_location.row][maze_location.column] = Cell.empty
        
        self.grid[self.start.row][self.start.column] = Cell.start
        self.grid[self.goal.row][self.goal.column] = Cell.goal

if __name__ == "__main__":
    maze = Maze()
    print(maze)

    solution_dfs: Node[MazeLocation] | None = dfs(maze.start, maze.goal_test, maze.successors)

    print("===== Resolvendo o labirinto com DFS =====")
    print()
    if solution_dfs is None:
        print("Sem solução")
    else:
        path_dfs: list[MazeLocation] = node_to_path(solution_dfs)
        maze.mark(path_dfs)
        print(maze)
        maze.clear(path_dfs)

    solution_bfs: Node[MazeLocation] | None = bfs(maze.start, maze.goal_test, maze.successors)

    print("===== Resolvendo o labirinto com BFS =====")
    print()
    if solution_dfs is None:
        print("Sem solução")
    else:
        path_bfs: list[MazeLocation] = node_to_path(solution_bfs)
        maze.mark(path_bfs)
        print(maze)
        maze.clear(path_bfs)

    distance = manhattan_distance(maze.goal)
    solution_a_star: Node[MazeLocation] | None = a_star(maze.start, maze.goal_test, maze.successors, distance)

    print("===== Resolvendo o labirinto com A* =====")
    print()
    if solution_a_star is None:
        print("Sem solução")
    else:
        path_a_star: list[MazeLocation] = node_to_path(solution_a_star)
        maze.mark(path_a_star)
        print(maze)
        maze.clear(path_a_star)
