
# cp-snippets

[![PyPI version](https://img.shields.io/pypi/v/cp-snippets.svg)](https://pypi.org/project/cp-snippets/)
[![Python versions](https://img.shields.io/pypi/pyversions/cp-snippets.svg)](https://pypi.org/project/cp-snippets/)
[![Docs](https://img.shields.io/badge/docs-online-blue.svg)](https://srinivastls.github.io/cp_snippets/)
[![License](https://img.shields.io/pypi/l/cp-snippets.svg)](LICENSE)

Small, fast, and reusable **competitive programming snippets** for Python.  
Built for **GATE / ICPC / Codeforces / LeetCode** preparation.

---

## 📦 Installation

```bash
pip install cp-snippets
```

---

## 🚀 Quick Start

```python
from cp_snippets.arrays import binary_search

arr = [1, 3, 5, 7, 9]
print(binary_search(arr, 7))  # 3
```

---

## 📚 Modules Overview

| Module               | Description                              |
| -------------------- | ---------------------------------------- |
| `cp_snippets.arrays` | Binary search, prefix sums, windows      |
| `cp_snippets.bit_utils` | Bit manipulation helpers              |
| `cp_snippets.dp`     | Common DP templates (LIS, knapsack)      |
| `cp_snippets.graphs` | BFS/DFS, DSU, Dijkstra, topo sort        |
| `cp_snippets.io`     | Fast input/output helpers                |
| `cp_snippets.math_utils` | GCD/LCM, modular arithmetic, sieve   |
| `cp_snippets.math`   | Alias of `cp_snippets.math_utils`        |
| `cp_snippets.misc`   | Small helpers (ceil div, compression)    |
| `cp_snippets.strings` | KMP/Z, rolling hash, Manacher           |
| `cp_snippets.trees`  | Fenwick, segment tree, LCA               |

---

## 📖 Documentation

👉 **Full API reference (auto-generated from docstrings):**
🔗 https://srinivastls.github.io/cp_snippets/

The documentation is automatically generated using **MkDocs + mkdocstrings**
and deployed via **GitHub Actions**.

---

## 🎯 Design Philosophy

* 🧠 Contest-friendly APIs
* ⚡ Minimal & fast
* 📘 Clear docstrings
* 🧩 Organized by topic
* 🧪 Easy to test and extend

---

## 🤝 Contributing

Contributions are welcome!

If you add a new snippet:

* include a clear docstring
* mention time complexity
* keep the API contest-friendly

---

## 📄 License

MIT License © Lakshmi Srinivas