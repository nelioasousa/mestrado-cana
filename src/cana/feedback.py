"""Determine the minimum weight feedback edges."""

from cana.graphs import WeightedUndirectedGraph
from typing import Optional


class RootedInTreeNode:
    def __init__(
        self, parent: Optional["RootedInTreeNode"] = None, rank: int = 0
    ):
        self.parent = parent
        self.rank = rank

    def find(self, collapse: bool = False) -> "RootedInTreeNode":
        if collapse and self.parent is not None:
            self.parent = self.parent.find(collapse=True)
            return self.parent
        root = self
        while root.parent is not None:
            root = root.parent
        return root

    def union(
        self, other: "RootedInTreeNode", collapse: bool = False
    ) -> "RootedInTreeNode":
        self_root = self.find(collapse=collapse)
        other_root = other.find(collapse=collapse)
        if self_root.rank < other_root.rank:
            self_root.parent = other_root
            return other_root
        other_root.parent = self_root
        if self_root.rank == other_root.rank:
            self_root.rank += 1
        return self_root


def minimum_spanning_tree(
    graph: WeightedUndirectedGraph, reverse: bool = False
):
    nodes = {v: RootedInTreeNode() for v in graph.get_vertices()}
    edges = graph.edges
    edges.sort(key=(lambda e: e[2]), reverse=reverse)
    mst_edges = []
    for edge in edges:
        lft_root = nodes[edge[0]].find()
        rgt_root = nodes[edge[1]].find()
        if lft_root == rgt_root:
            continue
        mst_edges.append(edge)
        if len(mst_edges) == len(nodes) - 1:
            break
    if len(mst_edges) != len(nodes) - 1:
        return None
    return WeightedUndirectedGraph(vertices=nodes.keys(), edges=mst_edges)


def get_minimum_feedback_edges(
    graph: WeightedUndirectedGraph, reverse: bool = False
):
    max_sp_tree = minimum_spanning_tree(graph, reverse=(not reverse))
    return frozenset(graph.edges) - frozenset(max_sp_tree.edges)
