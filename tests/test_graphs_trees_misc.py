import unittest
import sys
import os

# Add the project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pycp.graphs import UnionFind, bfs_dist, bfs_path, topological_sort_kahn
from pycp.trees import FenwickTree, SegmentTree, BinaryLiftingLCA
from pycp.misc import coordinate_compress, ceil_div


class TestGraphsTreesMisc(unittest.TestCase):
    def test_union_find(self):
        uf = UnionFind(5)
        self.assertTrue(uf.union(0, 1))
        self.assertTrue(uf.same(0, 1))
        self.assertFalse(uf.union(0, 1))
        self.assertFalse(uf.same(0, 2))

    def test_bfs(self):
        # 0-1-2 and 1-3
        adj = [[1], [0, 2, 3], [1], [1]]
        self.assertEqual(bfs_dist(4, adj, 0), [0, 1, 2, 2])
        self.assertEqual(bfs_path(4, adj, 0, 3), [0, 1, 3])

    def test_toposort(self):
        # 0 -> 1 -> 2
        adj = [[1], [2], []]
        self.assertEqual(topological_sort_kahn(3, adj), [0, 1, 2])

    def test_fenwick_and_segtree(self):
        arr = [1, 2, 3, 4]
        ft = FenwickTree(arr)
        self.assertEqual(ft.sum_range(1, 3), 9)
        ft.add(2, 5)  # arr[2] += 5
        self.assertEqual(ft.sum_range(0, 3), 1 + 2 + 8 + 4)

        st = SegmentTree(arr)
        self.assertEqual(st.query(0, 4), 10)
        st.update(1, 10)
        self.assertEqual(st.query(0, 2), 11)

    def test_lca(self):
        # tree: 0-1, 1-2, 1-3
        adj = [[1], [0, 2, 3], [1], [1]]
        lca = BinaryLiftingLCA(4, adj, root=0)
        self.assertEqual(lca.lca(2, 3), 1)
        self.assertEqual(lca.dist(2, 0), 2)

    def test_misc(self):
        compressed, uniq, mp = coordinate_compress([10, 5, 10, 7])
        self.assertEqual(uniq, [5, 7, 10])
        self.assertEqual(compressed, [2, 0, 2, 1])
        self.assertEqual(mp[7], 1)
        self.assertEqual(ceil_div(5, 2), 3)


if __name__ == '__main__':
    unittest.main()
