"""Graphs representation using Python."""

import yaml
from collections.abc import Hashable, Collection, Callable


type Edge = tuple[Vertex, Vertex, float]
type KeyParser = Callable[[str], Hashable]
type ValueParser = Callable[[str], object]


class Vertex:
    def __init__(self, key: Hashable, value: object):
        self.key = key
        self.value = value

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, value):
        if isinstance(value, type(self)):
            return self.key == value.key
        return False


class WeightedUndirectedGraph:
    """Weighted, undirected graph using adjacency list (hash map)."""

    def __init__(self, vertices: Collection[Vertex], edges: Collection[Edge]):
        self.edges = list(edges)
        # comprehension needed so each list() is unique for each vertice
        self.adjacency = {v: list() for v in vertices}
        for lft, rgt, weight in self.edges:
            self.adjacency.setdefault(lft, list()).append((rgt, weight))
            self.adjacency.setdefault(rgt, list()).append((lft, weight))

    @classmethod
    def from_file(
        cls,
        file_path: str,
        key_parser: KeyParser = str,
        value_parser: ValueParser = str,
    ):
        """Load a graph from a file."""
        with open(file_path, mode="r") as f:
            gf = yaml.load(f, Loader=yaml.BaseLoader)
        vertices = {
            k: Vertex(key=key_parser(k), value=value_parser(v))
            for k, v in gf["vertices"].items()
        }
        gf_edges = gf["edges"]
        edges = []
        for lft in gf_edges:
            from_ = gf_edges[lft]
            edges.extend(
                [
                    (vertices[lft], vertices[rgt], float(w))
                    for rgt, w in zip(from_["to"], from_["weight"])
                ]
            )
        return cls(vertices.values(), edges)

    def insert_edge(self, edge: Edge) -> None:
        """Insert an edge into the graph."""
        self.adjacency.setdefault(edge[0], list()).append((edge[1], edge[2]))
        self.adjacency.setdefault(edge[1], list()).append((edge[0], edge[2]))
        self.edges.append(edge)
        return None

    def insert_edges(self, edges: Collection[Edge]) -> None:
        """Insert many edges into the graph."""
        for lft, rgt, weight in edges:
            self.adjacency.setdefault(lft, list()).append((rgt, weight))
            self.adjacency.setdefault(rgt, list()).append((lft, weight))
        self.edges.extend(edges)
        return None

    def insert_vertex(self, vertex: Vertex) -> None:
        """Insert a vertex into the graph."""
        self.adjacency.setdefault(vertex, list())
        return None

    def insert_vertices(self, vertices: Collection[Vertex]) -> None:
        """Insert many vertices into the graph."""
        self.adjacency.update(
            {v: list() for v in vertices if v not in self.adjacency}
        )
        return None

    def get_vertices(self) -> list[Vertex]:
        """Return all the vertices in the graph."""
        return list(self.adjacency)

    def get_edges(self) -> list[Edge]:
        """Return all the edges in the graph."""
        return self.edges

    def check_connection(self, a: Vertex, b: Vertex, /) -> bool:
        """Check if two vertices are connected."""
        if a not in self.adjacency:
            return False
        return b in tuple(i[0] for i in self.adjacency[a])
