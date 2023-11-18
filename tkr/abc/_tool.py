"""
The abc._tool file contains tools for interacting with tkr.

Classes:
- `ToolProxy`: Represents a tool that can be used to perform a specific task.

Usage:
- Import tkr.abc._tool
"""

__all__: tuple = (
  'ToolProxy',
)

from .. import resource
from typing import (Optional, TypeVar, Protocol, runtime_checkable)

abc_types:   tuple = (
                    'TOOL.TKR.PROXY',
                    'TOOL.TKR.CLASSIC'
)

VERSION:     str   = abc_types[0]

@resource.notdeprecated
@runtime_checkable
class ToolProxy(Protocol):
  """
  Proxy for tools

  Attributes:
  name (str): The name of the tool.
  version (str): The version of the tool.
  id (str): The id of the tool.
  description (str): The description of the tool.
  method (function): The method of the tool.
  type (str): The type of the tool.
  """
  name:            str
  __name__:        str
  version:         str
  __version__:     str
  description:     str
  __description__: str
  method:          object
  __method__:      object
  type: str =      VERSION
  __type__: str =  VERSION
