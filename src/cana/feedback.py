"""Determine the lightest or heaviest set of feedback edges."""

from cana.graphs import WeightedUndirectedGraph
from cana.spanning_trees import min_spanning_tree


def min_feedback_edges(
    graph: WeightedUndirectedGraph, max_feedback_edges: bool = False
):
    _, out_edges = min_spanning_tree(
        graph, max_spanning_tree=(not max_feedback_edges)
    )
    return out_edges
