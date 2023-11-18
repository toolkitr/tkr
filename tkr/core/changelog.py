"""
Changelog for tkr.

Classes:
- `Changelog`: The changelog class.
"""

__all__: tuple = (
  'Changelog',
)

from .. import resource

@resource.notdeprecated
class ChangeLog:
  """
  Changelog for tkr.

  Attributes:
  self.cl (dict): The changelog.
  """

  slots: tuple = ('cl')
  def __init__(self):
    """
    Initialize ChangeLog.
    """
    self.cl = {'0.1.6': self.v016, '0.1.7': self.v017, '0.1.8': self.v018}

  @property
  def v016(self) -> str:
    """
    Changelog for version 0.1.6.

    Returns:
    str: The changelog.
    """
    return """
    # Changelog

All notable changes to tkr will be documented in this file

## [V0.1.6]

### Added

- tkr.core coreattrs.json: Working on implementing a system of change during runtime
- tkr.core.get_changelog: tkr.changelog(version = '0.1.6.3') # Defaults to current version.

### Changed

- tkr.Tool attribute & variable updates: More functions, attributes, and variables in tkr.abc.Tool and tkr.abc._tool.ToolProxy 

### Deprecated

- No deprecated features: N/A

### Fixed

- toolkitr.tkr install error: Fixed all errors when installing using pip/pypi

### Removed

- tkr.set_abc: Removed tkr.abc.set_abc and tkr.core.set_abc

### Security

- tkr.core.coreattrs: Added simple try/except handling for any possible errors. On error creates variable attrs at tkr.core.attrs"""

  @property
  def v017(self): 
    """
    Changelog for version 0.1.7.

    Returns:
    str: The changelog.
    """
    return """
  # Changelog

All notable changes to tkr will be documented in this file

## [V0.1.7]

### Added

- tkr.ToolByName: Get a tool by its name (Tool.name) from tkr.abc.global_tools_by_name. | tkr.core.get_tool_by_name
- tkr.ToolByMethod: Get a list of tools using their methods (Tool.method) from tkr.abc.global_tools_by_method. | tkr.core.get_tool_by_method
- tkr.help / tkr.Help: tkr's help methods.

### Examples

Upgrading to V0.1.7
`pip install --upgrade`
or Install tkr
`pip install tkr==0.1.7`

```python
import tkr

def tkr_tool_test() -> list:
  return tkr.ToolProxy

mytool = tkr.Tool(
  name="mytool",
  version="0.0.1",
  method=tkr_tool_test
)
```
#### tkr.ToolByName
```python
tkr.ToolByName(name='mytool')
```

#### tkr.ToolByMethod
```python
tkr.ToolByMethod(method=tkr_tool_test)
```"""
  @property
  def v018(self) -> str:
    """
    Changelog for version 0.1.8.

    Returns:
    str: The changelog.
    """
    return """
# Changelog

All notable changes to tkr will be documented in this file

## [V0.1.8]

### Added
```diff
+ tkr.ext.tests.Driver: Pull code or file contents from toolkitr/tkr/<folder='test'>/<file='README.md'>
```

### Examples

Upgrading to V0.1.8
`pip install --upgrade tkr`
or Install tkr
`pip install tkr==0.1.8`

```python
import tkr
from tkr.ext import tests

driver: tests.Driver = tests.Driver(path='/abc/_tool.py', folder='tkr') # Defaults to test/README.md which provides info on the latest testing files.
print(driver)
```
If you want to update the driver to not create multiple instances do this:
```python
print(driver('otherfeature.py'))
```

# Links
- [Github](https://github.com/toolkitr/tkr)
- [PyPi](https://pypi.org/project/tkr)
- [Issues](https://github.com/toolkitr/tkr/issues)
- [Discussions](https://github.com/toolkitr/tkr/discussions)
"""
