"""cp_snippets: competitive programming snippets for Python."""

from __future__ import annotations

from importlib import metadata


def __getattr__(name: str):
	if name == "__version__":
		try:
			return metadata.version("cp-snippets")
		except Exception:
			return "0.0.0"
	raise AttributeError(name)


__all__ = ["__version__"]
