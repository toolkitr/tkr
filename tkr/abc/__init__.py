"""
The abc folder contains tools for interacting with tkr.

Classes:
- `Tool`: Represents a tool for performing a specific task.
- `ToolProxy`: Represents a tool that can be used to perform a specific task.

Usage:
- Import tkr.abc.Tool
"""

__all__: tuple = (
  "Tool",
  "ToolProxy",
)

import asyncio
import inspect
from ._tool import ToolProxy
from .. import resource

abc_types:              tuple =  (
                                 'TOOL.TKR.PROXY',
                                 'TOOL.TKR.CLASSIC'
)

VERSION:                str   =  abc_types[1]

global_tools_by_name:   dict  =  {} 
global_tools_by_method: dict  =  {}
global_tools_by_id:     dict  =  {}

abc_id:                 id    =  id

@resource.notdeprecated
class Tool(ToolProxy):
  """
  Primary class for creating Tools.

  Parameters:
  method (object): The method to wrap.
  name (str): The name of the tool.
  version (str): The version of the tool.
  description (str): The description of the tool.
  id (str): The id of the tool.
  """

  slots:                tuple  =  ('name', 'version', 'description', 'method', '__name__', '__version__', '__description__', '__method__', 'type', '__type__', 'id', '__id__')

  def __init__(self, method: object, name: str='Tool.DefaultName', version: str='Tool.NoVersion', description: str='Tool.Description', id: str=None, *args, **kwargs) -> None:
    """
    Initialize Tool.
    """
    if global_tools_by_name.get(name) is not None:
      tool_new_name: str = f'Tool.InUseNameDefault.{hex(abc_id(self))}'
      print(Exception(f'Tool.name=<"{name}"> is already in use. Using {tool_new_name}'))
      name: str = tool_new_name

    global_tools_by_name[name]: object = self

    if id is None:
      id: abc_id = f'Tool.Id.{hex(abc_id(self))}'
    global_tools_by_id[id]: object = self

    if method.__doc__ is None: 
      method.__doc__: str = f"""tkr.Tool method=<{method}> method_name=<{method.__name__}>"""


    self.id: abc_id =            id
    self.__id__: abc_id =        self.id
    self.name: str =             name
    self.__name__: str =         self.name
    self.version: str =          version
    self.__version__: str =      self.version
    self.description: str =      description
    self.__description__: str =  self.description
    self.desc: str =             self.description
    self.__desc__: str =         self.description
    self.method: str =           method
    self.__method__: str =       self.method
    self.func: str =             self.method
    self.__func__: str =         self.method
    self.type: str =             VERSION
    self.__type__: str =         self.type
    
    if global_tools_by_method.get(self.method) is not None:
      if isinstance(global_tools_by_method[self.method], list):
        global_tools_by_method[self.method].append(self)
    else:
      global_tools_by_method[self.method] = [self]

  @resource.notdeprecated
  def register(self, method: object = None, name: str='Tool.DefaultName', version: str='Tool.NoVersion', description: str='Tool.Description', type: str = abc_types[1], id: str=None, *args, **kwargs) -> ToolProxy:
    """
    Registers a tool.

    Parameters:
    method (object): The method to wrap.
    name (str): The name of the tool.
    version (str): The version of the tool.
    description (str): The description of the tool.
    type (str): The type of the tool.
    id (str): The id of the tool.

    Returns:
    ToolProxy: The tool.
    """
    if method is None: method = self.method
    self.__init__(method, name, version, description, id, *args, **kwargs)
    return self

  @resource.notdeprecated
  def update(self, method: object = None, name: str='Tool.DefaultName', version: str='Tool.NoVersion', description: str='Tool.Description', type: str = abc_types[1], id: str=None, *args, **kwargs) -> ToolProxy:
    """
    Updates a tool.

    Parameters:
    method (object): The method to wrap.
    name (str): The name of the tool.
    version (str): The version of the tool.
    description (str): The description of the tool.
    type (str): The type of the tool.
    id (str): The id of the tool.

    Returns:
    ToolProxy: The tool.
    """
    self.register(method=method, name=name, version=version, description=description, type=type, id=id, *args, **kwargs)
    return self

  @resource.notdeprecated
  def run(self, *args, **kwargs) -> object:
    """
    Runs the tool.

    Parameters:
    *args (object): The args to pass to the tool.
    **kwargs (object): The kwargs to pass to the tool.

    Returns:
    object: The result of the tool.
    """
    if inspect.iscoroutinefunction(self.method): out: object = asyncio.run(self.method(*args, **kwargs))
    else: out: object = self.method(*args, **kwargs)
    return out

  @resource.notdeprecated
  def info(self, *args, **kwargs) -> dict:
    """
    Info about the tool.

    Returns:
    dict: The info about the tool.
    """
    return {
      'name': self.name,
      'version': self.version,
      'id': self.id,
      'description': self.description,
      'method': self.method,
      'type': self.type
    }

  def __dict__(self, *args, **kwargs) -> dict:
    """
    Info about the tool.

    Returns:
    dict: The info about the tool.
    """
    return self.info()

  def __tuple__(self, *args, **kwargs) -> tuple:
    """
    Info about the tool.

    Returns:
    tuple: The info about the tool.
    """
    return (self.name, self.version, self.id, self.description, self.method, self.type)

  def __list__(self, *args, **kwargs) -> list:
    """
    Info about the tool.

    Returns:
    list: The info about the tool.
    """
    return [self.name, self.version, self.id, self.description, self.method, self.type]

  def __repr__(self, *args, **kwargs) -> str:
    """
    Info about the tool.

    Returns:
    repr: The info about the tool.
    """
    return f'<Tool name={self.name} version={self.version} id={self.id} description={self.description} method={self.method} type={self.type}>'

  def __str__(self, *args, **kwargs) -> str:
    """
    Info about the tool.

    Returns:
    str: The info about the tool.
    """
    return self.__repr__()

  def __int__(self, *args, **kwargs) -> int:
    """
    Info about the tool.

    Returns:
    int: The info about the tool. 
    """
    return int(str(self.version).replace('.', ''))

  def __eq__(self, other, *args, **kwargs) -> tuple:
    """
    Info about the tool.

    Returns:
    tuple: The info about the tool.
    """
    return self.name == other.name, self.version == other.version, self.id == other.id, self.description == other.description, self.method == other.method, self.type == other.type

  def __ne__(self, other, *args, **kwargs) -> tuple:
    """
    Info about the tool.

    Returns:
    tuple: The info about the tool.
    """
    return self.name != other.name, self.version != other.version, self.id != other.id, self.description != other.description, self.method != other.method, self.type != other.type

  def __call__(self, *args, **kwargs) -> object:
    """
    Runs the tool.

    Parameters:
    *args (object): The args to pass to the tool.
    **kwargs (object): The kwargs to pass to the tool.

    Returns:
    object: The result of the tool.
    """
    return self.run(*args, **kwargs)

  @resource.notdeprecated
  def help(self, print_help: bool=True, *args, **kwargs) -> str:
    """
    Help/Info about the tool.

    Parameters:
    print_help (bool): Whether to print the help.

    Return:
    str: The help/info about the tool.
    """
    help_str: str = """
    tkr.abc.Tool
    
    method: lambda methods, functions, classes, etc
    
    tlkr.abc.Tool.register(method<Optional>, name<Optional>, version<Optional>, description<Optional>, type<Optional>, id<Optional>)
    
    tlkr.abc.Tool.update = .register() # Same as tlkr.abc.Tool.register()
    
    print(tlkr.abc.Tool.__annotations__)
    
    tlkr.abc.Tool.run(*args, **kwargs) # Runs current method
    
    ### CURRENT METHOD CAN ALSO BE CAN WITH __CALL__###
    EXAMPLE: mytool = Tool(method=my_function)
    
    mytool() <- RUNS my_function
    """
    if print_help == True: print(help_str)
    else: return help_str
