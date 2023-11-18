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

## [V0.2.0]

### Changed
```diff
Continued to further optimize and refactor code.

+ Fixed some tkr.Driver issues
+ Added tkr.tools / tkr.abc.global_tools
+ Added a save method to tkr.Driver: tkr.Driver.save(file)
```

### Examples

Upgrading to V0.2.0
`pip install --upgrade tkr`
or Install tkr
`pip install tkr==0.2.0`

```python
import tkr

mytool1: tkr.Tool = tkr.Tool(
    name='foo',
    method=lambda x: x+1
)

mytool2: tkr.Tool = tkr.Tool(
    name='bar',
    method=lambda y: y+2
)

print(tkr.tools)

# Output

[<Tool name=foo version=Tool.NoVersion id=Tool.Id.0x7f0db3431690 description=Tool.Description method=<function <lambda> at 0x7f0db34fbe20> type=TOOL.TKR.CLASSIC>, <Tool name=bar version=Tool.NoVersion id=Tool.Id.0x7f0db34300d0 description=Tool.Description method=<function <lambda> at 0x7f0db3277370> type=TOOL.TKR.CLASSIC>, ...]
```

tkr.Driver:

```python
import tkr

driver: tkr.Driver = tkr.Driver(
    path='/abc/_tool.py',  # Defaults to 'README.md' file
    folder='tkr'           # Defaults to 'test' folder
)
print(driver)
```
If you want to update the driver to not create multiple instances do this:
```python
print(driver('otherfeature', 'otherfolder'))
```
If you want to save the drivers file contents do this:
```python
driver.save('somefile')
```

# Links
- [Github](https://github.com/toolkitr/tkr)
- [PyPi](https://pypi.org/project/tkr)
- [Issues](https://github.com/toolkitr/tkr/issues)
- [Discussions](https://github.com/toolkitr/tkr/discussions)
