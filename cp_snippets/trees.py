from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Callable, Deque, List, Optional, Sequence


class FenwickTree:
	"""Fenwick Tree (Binary Indexed Tree) for point updates and prefix sums.

	Indexing:
		Public methods accept 0-based indices; internally we use 1-based.
	"""

	def __init__(self, n_or_arr: int | Sequence[int]):
		if isinstance(n_or_arr, int):
			n = n_or_arr
			if n < 0:
				raise ValueError("n must be non-negative")
			self.n = n
			self.bit = [0] * (n + 1)
		else:
			arr = list(n_or_arr)
			self.n = len(arr)
			self.bit = [0] * (self.n + 1)
			for i, v in enumerate(arr):
				self.add(i, v)

	def add(self, idx: int, delta: int) -> None:
		"""Adds `delta` to a[idx]."""
		i = idx + 1
		while i <= self.n:
			self.bit[i] += delta
			i += i & -i

	def sum_prefix(self, r: int) -> int:
		"""Returns sum(a[0..r]) inclusive. If r < 0 returns 0."""
		if r < 0:
			return 0
		i = r + 1
		res = 0
		while i > 0:
			res += self.bit[i]
			i -= i & -i
		return res

	def sum_range(self, l: int, r: int) -> int:
		"""Returns sum(a[l..r]) inclusive."""
		if r < l:
			return 0
		return self.sum_prefix(r) - self.sum_prefix(l - 1)


class SegmentTree:
	"""Iterative segment tree for range queries and point updates.

	Default operation is sum; you can supply any associative `op` with identity `e`.

	Query semantics:
		query(l, r) returns op over the half-open interval [l, r).
	"""

	def __init__(
		self,
		arr: Sequence[int],
		op: Callable[[int, int], int] = lambda a, b: a + b,
		e: int = 0,
	):
		self.n = len(arr)
		self.op = op
		self.e = e
		self.size = 1
		while self.size < self.n:
			self.size <<= 1
		self.data = [e] * (2 * self.size)
		# build
		for i in range(self.n):
			self.data[self.size + i] = arr[i]
		for i in range(self.size - 1, 0, -1):
			self.data[i] = op(self.data[2 * i], self.data[2 * i + 1])

	def update(self, idx: int, value: int) -> None:
		"""Sets a[idx] = value."""
		i = self.size + idx
		self.data[i] = value
		i //= 2
		while i:
			self.data[i] = self.op(self.data[2 * i], self.data[2 * i + 1])
			i //= 2

	def query(self, l: int, r: int) -> int:
		"""Returns op(a[l..r))"""
		res_left = self.e
		res_right = self.e
		l += self.size
		r += self.size
		while l < r:
			if l & 1:
				res_left = self.op(res_left, self.data[l])
				l += 1
			if r & 1:
				r -= 1
				res_right = self.op(self.data[r], res_right)
			l //= 2
			r //= 2
		return self.op(res_left, res_right)


class BinaryLiftingLCA:
	"""Lowest Common Ancestor for a rooted tree via binary lifting.

	Complexity:
		Preprocess: O(n log n)
		Query LCA:  O(log n)
	"""

	def __init__(self, n: int, adj: Sequence[Sequence[int]], root: int = 0):
		self.n = n
		self.root = root
		self.LOG = (n).bit_length()
		self.up = [[-1] * n for _ in range(self.LOG)]
		self.depth = [-1] * n

		q: Deque[int] = deque([root])
		self.depth[root] = 0
		self.up[0][root] = root

		while q:
			u = q.popleft()
			for v in adj[u]:
				if self.depth[v] != -1:
					continue
				self.depth[v] = self.depth[u] + 1
				self.up[0][v] = u
				q.append(v)

		for k in range(1, self.LOG):
			prev = self.up[k - 1]
			cur = self.up[k]
			for v in range(n):
				cur[v] = prev[prev[v]]

	def kth_ancestor(self, v: int, k: int) -> int:
		"""Returns the k-th ancestor of v (0-th ancestor is v)."""
		i = 0
		while k:
			if k & 1:
				v = self.up[i][v]
			k >>= 1
			i += 1
		return v

	def lca(self, a: int, b: int) -> int:
		"""Returns LCA(a, b)."""
		if self.depth[a] < self.depth[b]:
			a, b = b, a

		# lift a
		diff = self.depth[a] - self.depth[b]
		a = self.kth_ancestor(a, diff)
		if a == b:
			return a

		for k in range(self.LOG - 1, -1, -1):
			if self.up[k][a] != self.up[k][b]:
				a = self.up[k][a]
				b = self.up[k][b]

		return self.up[0][a]

	def dist(self, a: int, b: int) -> int:
		"""Number of edges on the path between a and b."""
		c = self.lca(a, b)
		return self.depth[a] + self.depth[b] - 2 * self.depth[c]
