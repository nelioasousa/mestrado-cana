import pytest
from importlib.resources import files as resource_files
from importlib.resources import as_file

from cana.graphs import WeightedUndirectedGraph


@pytest.fixture
def graph_file_path():
    resource = resource_files("tests.cana").joinpath("resources/graph.yaml")
    with as_file(resource) as file_path:
        yield file_path


def test_from_file_constructor(graph_file_path):
    graph = WeightedUndirectedGraph.from_file(graph_file_path, value_parser=int)
    vertices = graph.get_vertices()
    vertices.sort(key=(lambda x: x.key))
    assert list(range(1, len(vertices) + 1)) == [v.value for v in vertices]
    assert len(graph.edges) == 10
    assert graph.check_connection(vertices[0], vertices[1])
    assert graph.check_connection(vertices[-2], vertices[-1])
