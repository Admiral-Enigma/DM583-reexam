"""DM583 exam toolkit.

Exam warm-up (2 minutes):
  uv run python
  >>> from exam import *
  >>> res = analyze("A 5 2 / B 1 7 / C 3 3", metric="man", k=2, db=(3, 2))
  >>> check_order("C,A,B", res["lof"])
"""
import sys

# Windows consoles may default to cp1252; keep prints (fractions, tables) safe.
if getattr(sys.stdout, "reconfigure", None):
  try:
    sys.stdout.reconfigure(encoding="utf-8")
  except Exception:
    pass

from .dist import *
from .prob import *
from .density import *
from .freq import *
from .apriori import (apriori, apriori_full, load_transactions,
                      find_maximal, find_closed, generate_rules)
from .gmm import *
from .cluster import *
from .outliers import *
from .driver import *
