from cana.graphs import WeightedUndirectedGraph
from cana.feedback import min_feedback_edges


def test_spanning_trees(graph_file_path):
    graph = WeightedUndirectedGraph.from_file(graph_file_path, value_parser=int)
    min_cost = 14
    max_cost = 24
    total_cost = sum(e.weight for e in graph.edges)
    # Lightest feedback edges
    min_fdb = min_feedback_edges(graph)
    assert min_fdb is not None
    assert sum(e.weight for e in min_fdb) == (total_cost - max_cost)
    # Heaviest feedback edges
    max_fdb = min_feedback_edges(graph, max_feedback_edges=True)
    assert max_fdb is not None
    assert sum(e.weight for e in max_fdb) == (total_cost - min_cost)
