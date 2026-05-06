from __future__ import annotations

from typing import Dict, Iterable, List, Sequence, Tuple, TypeVar


T = TypeVar("T")


def ceil_div(a: int, b: int) -> int:
	"""Ceiling division for integers.

	Works for negative values as well.
	"""
	if b == 0:
		raise ZeroDivisionError("division by zero")
	return -(-a // b)


def floor_div(a: int, b: int) -> int:
	"""Floor division for integers (same as `a // b`, here for symmetry)."""
	if b == 0:
		raise ZeroDivisionError("division by zero")
	return a // b


def coordinate_compress(values: Sequence[T]) -> Tuple[List[int], List[T], Dict[T, int]]:
	"""Coordinate compression.

	Args:
		values: Any sortable values.

	Returns:
		(compressed, uniq, index)
		compressed: list of ints, same length as values
		uniq: sorted unique values
		index: mapping from value -> compressed index
	"""
	uniq = sorted(set(values))
	index = {v: i for i, v in enumerate(uniq)}
	compressed = [index[v] for v in values]
	return compressed, uniq, index


def chunks(arr: Sequence[T], size: int) -> Iterable[Sequence[T]]:
	"""Yields consecutive chunks of length `size` from `arr`."""
	if size <= 0:
		raise ValueError("size must be positive")
	for i in range(0, len(arr), size):
		yield arr[i : i + size]
