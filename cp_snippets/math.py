"""Compatibility re-export for `math_utils`.

The project historically used the name `math` in documentation, while the actual
implementation lives in `math_utils.py`.
"""

from .math_utils import *  # noqa: F401,F403
