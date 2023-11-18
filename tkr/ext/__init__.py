"""
The tkr.ext folder contains extension tools for interacting with tkr.

Classes:
- `tests.Driver`: The github testing folder webdriver for tkr. 
"""

__all__: tuple = (
  'tests',
)

from . import driver as tests
