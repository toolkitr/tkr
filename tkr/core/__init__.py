"""
The tkr.core folder contains core tools for interacting with tkr.

Classes:
- `ChangeLog`: Represents a changelog for a tkr.

Functions:
- `tkr_setup_hook`: Setup hook for tkr.
- `get_changelog`: Gets the changelog for tkr.
- `get_tool_by_name`: Gets a tool by name.
- `get_tool_by_method`: Gets a tool by method.
- `get_tool_by_id`: Gets a tool by id.
- `tkr_help_hook`: Help hook for tkr.
"""

__all__: tuple = (
    'ChangeLog',
    'get_changelog',
    'get_tool_by_name',
    'get_tool_by_method',
    'get_tool_by_id',
    'tkr_help_hook',
    'tkr_setup_hook',
)

import os, json

from .changelog import ChangeLog
from .. import resource
from ..abc import (
                             global_tools_by_name, 
                             global_tools_by_method, 
                             global_tools_by_id
)
tkr_version:    str       =  '0.1.9'
changelog:      ChangeLog =  ChangeLog()

@resource.notdeprecated
def tkr_setup_hook() -> tuple:
  """
  Setup hook for tkr.

  Returns:
  tuple: The setup hook.
  """
  return (tkr_version, 'tkr', 'toolkitr.tkr', 'tklr.', 'toolkitr.email@gmail.com', 'Python Toolkit')

@resource.notdeprecated
def get_changelog(version: str = tkr_version) -> str:
  """
  Get the changelog for the given version.

  Parameters:
  version (str): The version to get the changelog for.

  Returns:
  str: The changelog for the given version.
  """
  version: str = str(version).lower().replace('v', '')
  cl_return: ChangeLog = changelog.cl.get(version)
  if cl_return is None:
    cl_return: ChangeLog = changelog.cl.get(version.split('-')[0], f'No version found. tkr.Versions.{tkr_version}, requested_version=<{version}>')

  return cl_return

@resource.notdeprecated
def get_tool_by_name(name: str) -> object:
  """
  Get the tool by name.

  Parameters:
  name (str): The name of the tool.

  Returns:
  object: The tool.
  """
  return global_tools_by_name.get(name)

@resource.notdeprecated
def get_tool_by_method(method: object) -> list:
  """
  Get the tool by method.

  Parameters:
  method (object): The method of the tool.

  Returns:
  object: The tool.
  """
  return global_tools_by_method.get(method)

@resource.notdeprecated
def get_tool_by_id(id: str) -> list:
  """
  Get the tool by id.

  Parameters:
  id (str): The id of the tool.

  Returns:
  object: The tool.
  """
  return global_tools_by_id.get(id)

@resource.notdeprecated
def tkr_help_hook(print_help: bool = True) -> str:
  """
  Help hook for tkr.

  Parameters:
  print_help (bool): Whether to print help or not.

  Returns:
  str: The help hook.
  """
  help_str = f"""
  ## tkr - Python Toolkit
  VERSION: {tkr_version}
  CHANGELOG: https://github.com/toolkitr/tkr/blob/main/CHANGELOG.md

  pypi/pip: https://pypi.org/project/tkr/
  github: https://github.com/toolkitr/tkr

  ## Installing/Upgrading

  install > `pip install tkr`
  upgrade > `pip install --upgrade tkr`

  ## Example:
  ```
  import tkr

  def tkr_tool_test() -> list:
    return tkr.ToolProxy

  mytool = tkr.Tool(
    name="mytool",
    version="0.0.1",
    method=tkr_tool_test, *REQUIRED
    description="A simple tool.",
    id="mytoolid",
    type="TOOL.TKR.CLASSIC" <TOOL.TKR.CLASSIC by default
  )
  ```

  ## Test Features
  ```
  import tkr
  from tkr.ext import tests

  driver = tests.Driver('testingfeature.py')
  print(driver) # Returns the code from our github's testingfeature.py
  """
  if print_help == True: print(help_str)
  else: return help_str

attrs: str = 'tkr.coreattrs.WriteStart'
path: str = str(os.path.abspath(__file__)).replace('__init__.py', 'coreattrs.json')

try:
  with open(path, 'w') as file:
    attrs_content: dict = {"version": tkr_version}
    json.dump(attrs_content, file, indent=4)
except: attrs: str = 'tkr.coreattrs.WriteFailed'
