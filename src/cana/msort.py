"""Merge sort."""

import sys

def merge(arr, i, k, j):
	"""
	Inplace merge of ordered arrays 'arr[i:k+1]' and
	'arr[k+1:j+1]' into a fully ordered array 'arr[i:j+1]'.
	"""
	if not i <= k <= j:
		raise ValueError("Must have 'i' <= 'k' <= 'j'")
	cp = list(arr[i:j+1]) # Copy of arr from i to j
	stop = (k-i, j-i)
	lft_idx = 0
	rgt_idx = stop[0] + 1
	ptr = i
	while lft_idx <= stop[0] and rgt_idx <= stop[1]:
		if cp[lft_idx] <= cp[rgt_idx]:
			arr[ptr] = cp[lft_idx]
			lft_idx += 1
		else:
			arr[ptr] = cp[rgt_idx]
			rgt_idx += 1	
		ptr += 1
	if lft_idx > stop[0]:
		arr[ptr:j+1] = cp[rgt_idx:stop[1]+1]
	else:
		arr[ptr:j+1] = cp[lft_idx:stop[0]+1]
	return

def merge_sort(arr, i, j, merge_routine=merge):
	"""
	Inplace sorting of 'arr' from 'i' to 'j',
	both inclusive.
	"""
	if i == j:
		return arr
	if i > j:
		raise ValueError("'j' must be >= 'i'")
	mid = (i + j) // 2
	merge_sort(arr, i, mid, merge_routine)
	merge_sort(arr, mid+1, j, merge_routine)
	merge_routine(arr, i, mid, j)
	return arr

def main():
	if len(sys.argv) != 4:
		print("Example usage: python msort.py 45,87,42,50 1 3")
		return 1
	try:
		arr = [int(i) for i in sys.argv[1].split(",")]
		i = int(sys.argv[2])
		j = int(sys.argv[3])
	except ValueError:
		print("Use only base 10 integers!")
		print("Example usage: python msort.py 45,87,42,50 1 3")
		return 2
	if not 0 <= i <= j < len(arr):
		print("Bad 0-based indexing!")
		print("Example usage: python msort.py 45,87,42,50 1 3")
		return 4
	print(merge_sort(arr, i, j))
	return 0

if __name__ == "__main__":
	sys.exit(main())
