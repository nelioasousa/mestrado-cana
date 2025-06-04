import pytest

from cana.msort import merge_sort
import cana.inversion as inversion


@pytest.mark.parametrize(
    "arr,num_inv", (([0, 1, 2, 3], 0), ([0, 1, 3, 2], 1), ([3, 1, 2, 0], 5))
)
def test_inversion_counter(arr, num_inv, monkeypatch):
    # inversion.num_inversions = 0
    monkeypatch.setattr(inversion, "num_inversions", 0)
    merge_sort(arr, 0, len(arr) - 1, merge_routine=inversion.inv_merge)
    assert inversion.num_inversions == num_inv
