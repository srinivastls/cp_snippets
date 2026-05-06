from __future__ import annotations

from collections import deque
from dataclasses import dataclass
import heapq
from typing import Deque, Dict, Iterable, List, Optional, Sequence, Tuple


class UnionFind:
	"""Disjoint Set Union (Union-Find) with path compression + union by size."""

	def __init__(self, n: int):
		if n < 0:
			raise ValueError("n must be non-negative")
		self.parent = list(range(n))
		self.size = [1] * n

	def find(self, x: int) -> int:
		while self.parent[x] != x:
			self.parent[x] = self.parent[self.parent[x]]
			x = self.parent[x]
		return x

	def union(self, a: int, b: int) -> bool:
		ra, rb = self.find(a), self.find(b)
		if ra == rb:
			return False
		if self.size[ra] < self.size[rb]:
			ra, rb = rb, ra
		self.parent[rb] = ra
		self.size[ra] += self.size[rb]
		return True

	def same(self, a: int, b: int) -> bool:
		return self.find(a) == self.find(b)


def bfs_dist(n: int, adj: Sequence[Sequence[int]], src: int) -> List[int]:
	"""Shortest distances from `src` in an unweighted graph.

	Returns a list `dist` where dist[v] is the number of edges in the shortest
	path from src to v, or -1 if unreachable.
	"""
	dist = [-1] * n
	q: Deque[int] = deque([src])
	dist[src] = 0
	while q:
		u = q.popleft()
		for v in adj[u]:
			if dist[v] != -1:
				continue
			dist[v] = dist[u] + 1
			q.append(v)
	return dist


def bfs_path(n: int, adj: Sequence[Sequence[int]], src: int, dst: int) -> Optional[List[int]]:
	"""Returns one shortest path (as a list of vertices) from src to dst in an unweighted graph."""
	parent = [-1] * n
	q: Deque[int] = deque([src])
	parent[src] = src
	while q:
		u = q.popleft()
		if u == dst:
			break
		for v in adj[u]:
			if parent[v] != -1:
				continue
			parent[v] = u
			q.append(v)

	if parent[dst] == -1:
		return None

	path = [dst]
	while path[-1] != src:
		path.append(parent[path[-1]])
	path.reverse()
	return path


def dfs_iterative(adj: Sequence[Sequence[int]], start: int) -> List[int]:
	"""Iterative DFS that returns the visitation order."""
	n = len(adj)
	seen = [False] * n
	order: List[int] = []
	stack = [start]
	while stack:
		u = stack.pop()
		if seen[u]:
			continue
		seen[u] = True
		order.append(u)
		# push neighbors in reverse for a more "recursive-like" order
		for v in reversed(adj[u]):
			if not seen[v]:
				stack.append(v)
	return order


def connected_components(n: int, adj: Sequence[Sequence[int]]) -> List[List[int]]:
	"""Connected components in an undirected graph."""
	seen = [False] * n
	comps: List[List[int]] = []
	for i in range(n):
		if seen[i]:
			continue
		comp: List[int] = []
		stack = [i]
		seen[i] = True
		while stack:
			u = stack.pop()
			comp.append(u)
			for v in adj[u]:
				if not seen[v]:
					seen[v] = True
					stack.append(v)
		comps.append(comp)
	return comps


def topological_sort_kahn(n: int, adj: Sequence[Sequence[int]]) -> Optional[List[int]]:
	"""Topological sort of a directed graph.

	Returns:
		A topological order list of length n, or None if a cycle exists.
	"""
	indeg = [0] * n
	for u in range(n):
		for v in adj[u]:
			indeg[v] += 1

	q: Deque[int] = deque([i for i, d in enumerate(indeg) if d == 0])
	order: List[int] = []
	while q:
		u = q.popleft()
		order.append(u)
		for v in adj[u]:
			indeg[v] -= 1
			if indeg[v] == 0:
				q.append(v)

	if len(order) != n:
		return None
	return order


def dijkstra(
	n: int, adj: Sequence[Sequence[Tuple[int, int]]], src: int
) -> Tuple[List[int], List[int]]:
	"""Dijkstra shortest paths for non-negative edge weights.

	Args:
		n: Number of vertices.
		adj: Adjacency list where adj[u] contains (v, w).
		src: Source vertex.

	Returns:
		(dist, parent)
		dist[v] is the shortest distance from src to v (or a large number if unreachable).
		parent[v] is previous vertex on a shortest path (or -1 if unreachable, src's parent is src).
	"""
	INF = 10**30
	dist = [INF] * n
	parent = [-1] * n
	dist[src] = 0
	parent[src] = src
	pq: List[Tuple[int, int]] = [(0, src)]
	while pq:
		d, u = heapq.heappop(pq)
		if d != dist[u]:
			continue
		for v, w in adj[u]:
			nd = d + w
			if nd < dist[v]:
				dist[v] = nd
				parent[v] = u
				heapq.heappush(pq, (nd, v))
	return dist, parent


def reconstruct_path(parent: Sequence[int], src: int, dst: int) -> Optional[List[int]]:
	"""Reconstruct a path from `src` to `dst` given a `parent` array.

	The convention is that parent[src] == src, and parent[v] == -1 means unreachable.
	"""
	if dst < 0 or dst >= len(parent):
		raise IndexError("dst out of bounds")
	if parent[dst] == -1:
		return None
	path = [dst]
	while path[-1] != src:
		p = parent[path[-1]]
		if p == -1:
			return None
		path.append(p)
	path.reverse()
	return path
