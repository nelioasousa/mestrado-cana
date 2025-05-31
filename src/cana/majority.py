"""Computes the majority element of an array."""

import sys


def check_majority(arr, lft_candidate, rgt_candidate):
    lft_count = 0
    rgt_count = 0
    for elem in arr:
        if elem == lft_candidate:
            lft_count += 1
        if elem == rgt_candidate:
            rgt_count += 1
    limit = len(arr) // 2
    if lft_count > limit:
        return lft_candidate
    elif rgt_count > limit:
        return rgt_candidate
    else:
        return None


def get_majority(arr):
    if not arr:
        raise ValueError("'arr' can't be empty.")
    if len(arr) == 1:
        return arr[0]
    mid = len(arr) // 2
    lft_candidate = get_majority(arr[:mid])
    rgt_candidate = get_majority(arr[mid:])
    return check_majority(arr, lft_candidate, rgt_candidate)


def main():
    if len(sys.argv) != 2:
        print("Example usage: python majority.py 10,4,10,7,10")
        return 1
    try:
        arr = [int(i) for i in sys.argv[1].split(",")]
    except ValueError:
        print("Use only base 10 integers!")
        print("Example usage: python majority.py 10,4,10,7,10")
        return 2
    majority = get_majority(arr)
    if majority is None:
        print("There's no majority.")
    else:
        print("Majority:", majority)
    return 0


if __name__ == "__main__":
    sys.exit(main())
