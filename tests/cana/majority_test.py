import pytest

from cana.majority import get_majority


@pytest.mark.parametrize(
    "arr,majority",
    (
        ([0, 1, 2, 3, 4], None),
        ([1, 1, 1, 2, 3], 1),
        (["a", "b", "a", "c", "a"], "a"),
    ),
)
def test_majority(arr, majority):
    assert get_majority(arr) == majority
