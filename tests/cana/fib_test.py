import pytest

from cana.fib import fib


@pytest.mark.parametrize("n,f_n", ((0, 0), (1, 1), (2, 1), (3, 2), (6, 8)))
def test_fib(n, f_n):
    assert fib(n) == f_n
