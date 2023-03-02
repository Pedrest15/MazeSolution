from __future__ import annotations
from typing import TypeVar, Generic
from MyDataStructures import Stack, Queue, PriorityQueue

T = TypeVar('T') 

class Node(Generic[T]):
    def __init__(self, state: T, parent: Node | None, cost: float = 0.0, heuristic: float = 0.0) -> None:
        self.state: T = state
        self.parent: Node | None = parent
        self.cost: float = cost
        self.heuristic: float = heuristic

    def __lt__(self, other: Node) -> bool:
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def node_to_path(node: Node[T]) -> list[T]:
    path: list[T] = []

    path.append(node.state)
    while node.parent is not None:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path

def dfs(initial: T, goal_test: callable[[T], bool], successors: callable[[T], list[T]]) -> Node[T] | None:
    frontier = Stack()
    frontier.push(Node(initial, None))
    explored = {initial}

    while not frontier.empty:
        current_node = frontier.pop()
        current_state = current_node.state

        if goal_test(current_state):
            return current_node
        
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))
    
    return None

def bfs(initial: T, goal_test: callable[[T], bool], successors: callable[[T], list[T]]) -> Node[T] | None:
    frontier = Queue()
    frontier.push(Node(initial, None))
    explored = {initial}

    while not frontier.empty:
        current_node = frontier.pop()
        current_state = current_node.state

        if goal_test(current_state):
            return current_node
        
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))
    
    return None

def manhattan_distance(goal: MazeLocation) -> MazeLocation | float:
    def distance(ml: MazeLocation) -> float:
        x: int = abs(ml.column - goal.column)
        y: int = abs(ml.row - goal.row)
        return (x + y)
    return distance

def a_star(initial: T, goal_test: callable[[T], bool], successors: callable[[T], list[T]],
            heuristic: callable[[T], float]) -> Node[T] | None:
    frontier = PriorityQueue()
    frontier.push(Node(initial, None, 0.0, heuristic(initial)))
    explored = {initial: 0.0}     

    while not frontier.empty:
        current_node = frontier.pop()
        current_state = current_node.state

        if goal_test(current_state):
            return current_node
        
        for child in successors(current_state):
            new_cost = current_node.cost + 1

            if child not in explored or explored[child] > new_cost:
                explored[child] = new_cost
                frontier.push(Node(child, current_node, new_cost, heuristic(child)))
    
    return None