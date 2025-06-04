import pytest
from importlib.resources import files as resource_files
from importlib.resources import as_file


@pytest.fixture
def graph_file_path():
    resource = resource_files("tests.cana").joinpath("resources/graph.yaml")
    with as_file(resource) as file_path:
        yield file_path
