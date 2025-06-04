"""Determine the lightest or heaviest set of feedback edges."""

from cana.graphs import WeightedUndirectedGraph
from cana.spanning_trees import min_spanning_tree


def min_feedback_edges(
    graph: WeightedUndirectedGraph, max_feedback_edges: bool = False
):
    mst = min_spanning_tree(graph, max_spanning_tree=(not max_feedback_edges))
    return None if mst is None else mst[1]
