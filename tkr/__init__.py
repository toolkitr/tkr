"""
tkr is a Python package that allows for you to save functions to assigned 'Tools' with names, versions, descriptions, etc. Easily keep track of global tools and get a specific tool by name or method.

Classes:
- `Tool`: Represents a tool.
- `ToolProxy`: Represents a proxy to a tool.

Functions:
- `changelog`: Gets the changelog.
- `ToolByName`: Gets a tool by name.
- `byname`: Gets a tool by name.
- `ToolByMethod`: Gets a tool by method.
- `bymethod`: Gets a tool by method.
- `ToolByID`: Gets a tool by ID.
- `byid`: Gets a tool by ID.
- `Help`: Gets help/info about tkr.
- `help`: Gets help/info about tkr.
"""

__all__: tuple = (
  'Tool',
  'ToolProxy',
  'ToolVersion',
  'Tools',
  'tools',
  'changelog',
  'ToolByName',
  'byname',
  'ToolByMethod',
  'bymethod',
  'ToolByID',
  'byid',
  'Help',
  'help',
  'corepath',
  'Driver',
  'driver'
)

from . import core
from . import abc
from . import ext

__version__, __name__, __package__, __author__, __email__, __description__ = core.tkr_setup_hook()

Tool            =       abc.Tool
ToolProxy       =       abc.ToolProxy
ToolVersion     =       abc.VERSION
Tools           =       abc.global_tools
tools           =       abc.global_tools
changelog       =       core.get_changelog
ToolByName      =       core.get_tool_by_name
byname          =       core.get_tool_by_name
ToolByMethod    =       core.get_tool_by_method
bymethod        =       core.get_tool_by_method
ToolById        =       core.get_tool_by_id
byid            =       core.get_tool_by_id
Help            =       core.tkr_help_hook
help            =       core.tkr_help_hook
corepath        =       core.path
Driver          =       ext.tests.Driver
driver          =       ext.tests.Driver

__annotations__ =       {
              'Tool':         Tool,
              'ToolProxy':    ToolProxy,
              'ToolVersion':  ToolVersion,
              'Tools':        Tools,
              'tools':        tools,
              'changelog':    changelog,
              'ToolByName':   ToolByName,
              'byname':       byname,
              'ToolByMethod': ToolByMethod,
              'bymethod':     bymethod,
              'ToolById':     ToolById,
              'byid':         byid,
              'Help':         Help,
              'help':         help,
              'corepath':     corepath,
              'Driver':       Driver,
              'driver':       driver,
}
