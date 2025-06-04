from cana.graphs import WeightedUndirectedGraph
from cana.spanning_trees import min_spanning_tree


def test_spanning_trees(graph_file_path):
    graph = WeightedUndirectedGraph.from_file(graph_file_path, value_parser=int)
    min_cost = 14
    max_cost = 24
    # Minimum ST
    min_edges = min_spanning_tree(graph)
    assert min_edges is not None
    assert sum(e.weight for e in min_edges[0]) == min_cost
    # Maximum ST
    max_edges = min_spanning_tree(graph, max_spanning_tree=True)
    assert max_edges is not None
    assert sum(e.weight for e in max_edges[0]) == max_cost
