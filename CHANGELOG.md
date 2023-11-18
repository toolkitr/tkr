<div id="header">
  <img src="https://i.ibb.co/gr1sM66/image-removebg-preview-2023-11-16-T193131-291.png" width="400"/>
</div>

# [TKR - Python Toolkit](https://pypi.org/project/tkr/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/toolkitr/tkr/blob/main/LICENSE)
[![Python Versions](https://img.shields.io/badge/python-3.10%20|%203.11%20|%203.12%20-blue)](https://www.python.org/downloads/)

```Allow python developers to easily manage classes, methods, and more!```
<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/></a></p>

# Changelog

All notable changes to tkr will be documented in this file

## [V0.1.9]

### Changed
```diff
Refactored all code, optimized, and fixed small bugs.

+ tkr.core.coreattrs.json: Fixed file write bug.
- tkr.ext.exttests: Changed to tkr.ext.driver
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
