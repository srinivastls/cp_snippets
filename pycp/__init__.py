"""pycp: compatibility package.

This repository's source lives under `cp_snippets/`, but some internal tests and
older code use the import path `pycp.*`.

Prefer importing from `cp_snippets` for new code.
"""

from __future__ import annotations

from cp_snippets import *  # noqa: F401,F403
