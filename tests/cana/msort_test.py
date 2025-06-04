import random

from cana.msort import merge_sort


def test_msort():
    arr = [0, 1, 2, 3, 4, 5, 6]
    cp_arr = list(arr[2:])
    random.shuffle(cp_arr)
    cp_arr.insert(0, arr[0])
    cp_arr.insert(0, arr[1])
    assert arr != cp_arr
    merge_sort(cp_arr, 0, len(cp_arr) - 1)
    assert arr == cp_arr
