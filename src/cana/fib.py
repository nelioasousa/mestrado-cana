"""Fibonacci sequence using matrix multiplication."""

import sys
import numpy as np
from math import log2

num_muls = 0


def matrix_mul_with_counter(A, B):
    """Matrix multiplication with a counter."""
    global num_muls
    num_muls += 1
    return A @ B


def fib_matrix_pow(n):
    """Raise 'A' to a power of 'n'."""
    A = np.array([[0, 1], [1, 1]], dtype="uint64")
    if n == 1:
        return A
    if n < 1:
        raise ValueError("'n' must be positive")
    is_odd = bool(n % 2)
    half = fib_matrix_pow(n // 2)
    if is_odd:
        return matrix_mul_with_counter(matrix_mul_with_counter(half, half), A)
    else:
        return matrix_mul_with_counter(half, half)


def fib(n):
    """Calculate the 'n'-th Fibonacci number."""
    if n == 0:
        return 0
    # '@' as a dot product
    return int(fib_matrix_pow(n)[0] @ [0, 1])


def main():
    if len(sys.argv) != 2:
        print("Usage: python fib.py <base 10 integer>")
        return 1
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Usage: python fib.py <base 10 integer>")
        return 2
    print(f"Fib_{n} = {fib(n)}")
    print(f"> {num_muls} matrix multiplications total")
    if n:
        print(f"> log2({n}) ~= {log2(n):.3f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
