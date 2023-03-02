from typing import TypeVar, Generic
from collections import deque
from heapq import heappush, heappop

T = TypeVar('T') 

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.container: list[T] = []

    @property
    def empty(self) -> bool:
        return not self.container

    def push(self, item: T) -> None:
        self.container.append(item)

    def pop(self) -> T: #LIFO
        return self.container.pop()

    def __repr__(self) -> str:
        return repr(self.container)

class Queue(Generic[T]):
    def __init__(self) -> None:
        self.container: Deque[T] = deque()

    @property
    def empty(self) -> bool:
        return not self.container
    
    def push(self, item: T) -> None:
        self.container.append(item)

    def pop(self) -> T:
        return self.container.popleft()

    def __repr__(self) -> str:
        return repr(self.container)

class PriorityQueue(Generic[T]):
    def __init__(self) -> None:
        self.container: list[T] = []

    @property
    def empty(self) -> bool:
        return not self.container
    
    def push(self, item: T) -> None:
        heappush(self.container, item)

    def pop(self) -> T:
        return heappop(self.container)

    def __repr__(self) -> str:
        return repr(self.container)