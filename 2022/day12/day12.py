from collections import namedtuple
from dataclasses import dataclass
import heapq
from typing import List, Optional, Tuple, TypeVar, Union
from elves.ip_ops import IPOps

test_ip = IPOps("day12/test_ip.txt").ip
ip = IPOps("day12/ip.txt").ip

Location = namedtuple("Location", ["x", "y"])

@dataclass
class Graph:
    width: int
    height: int
    grid: List[List[str]]
    start: Location
    end: Location

    def __init__(self, ip: list[str], weights: Optional[dict[Location, float]] = {}, start: Optional[Location] = None):
        self.grid = [list(i) for i in ip]
        self.width = len(ip[0])
        self.height = len(ip)
        self.weights = weights

        for y in range(self.height):
            for x in range(self.width):
                check = self.grid[y][x]
                if check == "S":
                    self.start = Location(x, y)
                elif check == "E":
                    self.end = Location(x, y)
        
        if start is not None:
            self.start = start

    def in_bounds(self, loc: Location) -> bool:
        return 0 <= loc.x < self.width and 0 <= loc.y < self.height
    
    def is_passable(self, from_loc: Location, to_loc: Location) -> bool:
        if from_loc == self.start:
            return ord(self.grid[to_loc.y][to_loc.x]) < ord("c")
        elif to_loc == self.end:
            return ord(self.grid[from_loc.y][from_loc.x]) >= ord("y")

        return ord(self.grid[to_loc.y][to_loc.x]) <= ord(self.grid[from_loc.y][from_loc.x]) + 1
                    
    def neighbours(self, loc: Location) -> list[Location]:
        locs = [Location(loc.x, loc.y+1), Location(loc.x+1, loc.y), Location(loc.x, loc.y-1), Location(loc.x-1, loc.y)]
        return [i for i in locs if self.in_bounds(i) and self.is_passable(loc, i)]
    
    def cost(self, from_loc: Location, to_loc: Location):
        if len(self.weights) == 0:
            # no weights so return 1
            return 1
        return self.weights[to_loc]

@dataclass
class PriorityQueue:
    T = TypeVar("T")
    elements: List[Tuple[float, T]]
    def __init__(self) -> None:
        self.elements = []

    @property
    def empty(self) -> bool:
        return not self.elements
    
    def put(self, item: T, priority: float):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self) -> T:
        return heapq.heappop(self.elements)[1]


def draw_tile(loc: Location, style: dict[str, Union[str, list[Location]]]) -> str:
    tile = "."
    if style and style["style"] == "path" and loc in style["data"]:
        tile = "#"
    if style["style"] == "dir" and style["go_to"]:
        go_to = style["go_to"]
        if go_to.x == loc.x + 1: tile = ">"
        elif go_to.x == loc.x - 1: tile = "<"
        elif go_to.y == loc.y + 1: tile = "v"
        elif go_to.y == loc.y - 1: tile = "^"
    return tile

def draw_grid(graph: Graph, style: Optional[dict[str, Union[str, dict]]]):
    print("-" * (graph.width+2))
    for y in range(graph.height):
        row = []
        for x in range(graph.width):
            if Location(x,y) == graph.start:
                tile = "S"
            elif Location(x,y) == graph.end:
                tile = "E"
            else:
                loc = Location(x,y)
                path = style["data"]
                style["go_to"] = path[path.index(loc)+1] if loc in path and path.index(loc) < len(path) else None
                tile = draw_tile(Location(x,y), style)
            row.append(tile)
        print(f' {"".join(row)} ')
    print("-" * (graph.width+2))

def a_star(graph: Graph) -> List[Location]:
    frontier = PriorityQueue()
    frontier.put(graph.start, 0)
    came_from: dict[Location, Optional[Location]] = {graph.start: None}
    cost_so_far: dict[Location, float] = {graph.start: 0}

    while not frontier.empty:
        current: Location = frontier.get()
        if current == graph.end:
            break

        for next in graph.neighbours(current):
            cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or cost < cost_so_far[next]:
                cost_so_far[next] = cost
                frontier.put(next, cost)
                came_from[next] = current
    
    return came_from, cost_so_far

def reconstruct_path(came_from: dict[Location, Optional[Location]], start: Location, end: Location) -> list[Location]:
    current: Location = end
    path: List[Location] = []
    if end not in came_from:
        # no path found
        return []
    
    while current != start:
        path.append(current)
        current = came_from[current]
    
    # path.append(start)
    path.reverse()
    return path

def heuristic(end: Location, current: Location) -> float:
    return abs(end.x - current.x) + abs(end.y - current.y)

def construct_graph(ip: list[str], start: Optional[Location] = None):
    graph = Graph(ip, start=start)
    weights = {}
    for y in range(graph.height):
        for x in range(graph.width):
            weights[Location(x,y)] = heuristic(graph.end, Location(x,y))
    graph.weights = weights
    return graph

def part1(ip):
    graph = construct_graph(ip)
    came_from, cost = a_star(graph)
    return len(reconstruct_path(came_from, graph.start, graph.end))

def part2(ip):
    path_lengths = []
    for y in range(len(ip)):
        for x in range(len(ip[0])):
            if ip[y][x] in ["a", "S"]:
                graph = construct_graph(ip, Location(x,y))
                came_from, cost = a_star(graph)
                path_lengths.append(len(reconstruct_path(came_from, graph.start, graph.end)))

    return min([i for i in path_lengths if i > 0])

# print(part1(ip))
print(part2(ip))