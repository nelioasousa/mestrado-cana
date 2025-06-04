"""Determine the minimum or maximum Spanning Tree."""

from cana.graphs import Edge, WeightedUndirectedGraph
from typing import Optional, NamedTuple


class RootedInTreeNode(NamedTuple):
    value: object
    parent: Optional["RootedInTreeNode"] = None
    rank: int = 0

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


def min_spanning_tree(
    graph: WeightedUndirectedGraph, max_spanning_tree: bool = False
) -> tuple[list[Edge], list[Edge]] | None:
    nodes = {v: RootedInTreeNode(v) for v in graph.get_vertices()}
    edges = graph.edges
    edges.sort(key=(lambda e: e[2]), reverse=max_spanning_tree)
    mst_edges = []
    out_edges = []
    for i, edge in enumerate(edges):
        lft_root = nodes[edge[0]].find()
        rgt_root = nodes[edge[1]].find()
        if lft_root == rgt_root:
            out_edges.append(edge)
            continue
        mst_edges.append(edge)
        lft_root.union(rgt_root)
        if len(mst_edges) == len(nodes) - 1:
            out_edges.extend(edges[i + 1 :])
            return mst_edges, out_edges
    return None
