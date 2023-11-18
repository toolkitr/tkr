<div id="header">
  <img src="https://media.discordapp.net/attachments/1171675700055506989/1174869412571009204/image.png?ex=65692967&is=6556b467&hm=cf457d1688e9bce9eda1136c24eb9ba313c09f2819aaf20c54f68518420c3830&=&width=667&height=333" width="400"/>
</div>

# [TKR - Python Toolkit](https://pypi.org/project/tkr/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/toolkitr/tkr/blob/main/LICENSE)
[![Python Versions](https://img.shields.io/badge/python-3.10%20|%203.11%20|%203.12%20-blue)](https://www.python.org/downloads/)

```Allow python developers to easily manage classes, methods, and more!```
<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/></a></p>

# Changelog

All notable changes to tkr will be documented in this file

## [V0.1.8] (V0.1.8-6)

### Changed
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
