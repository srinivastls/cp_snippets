from __future__ import annotations

from bisect import bisect_left
from typing import List, Sequence


def lis_length(arr: Sequence[int]) -> int:
    """Length of the Longest Increasing Subsequence (strict) in O(n log n)."""
    tails: List[int] = []
    for x in arr:
        i = bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)


def knapsack_01(weights: Sequence[int], values: Sequence[int], capacity: int) -> int:
    """0/1 knapsack maximum value.

    Args:
        weights: item weights
        values: item values
        capacity: knapsack capacity

    Returns:
        Maximum attainable value.

    Complexity:
        O(n * capacity) time, O(capacity) memory.
    """
    if len(weights) != len(values):
        raise ValueError("weights and values must have the same length")
    if capacity < 0:
        raise ValueError("capacity must be non-negative")

    dp = [0] * (capacity + 1)
    for w, v in zip(weights, values):
        if w < 0:
            raise ValueError("weights must be non-negative")
        for c in range(capacity, w - 1, -1):
            dp[c] = max(dp[c], dp[c - w] + v)
    return dp[capacity]
