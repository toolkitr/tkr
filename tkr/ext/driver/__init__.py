"""
The tkr.ext.driver folder contains the Driver class and its methods that pull code and content from the testing folder on tkr's github.

Classes:
- `Driver`: The github testing folder webdriver for tkr. 
"""

__all__: tuple = (
  'Driver',
)

import requests
from ... import resource

@resource.notdeprecated
class Driver:
  """
  Primary class for tkr github testing webdriver.

  Parameters:
  path (str): The file to pull from EX: file.py
  folder (str): The folder the file is in.
  """

  slots: tuple = ('__base', '__baseurl', '__file', '__content')
  def __init__(self, path: str='README.md', folder:str='test', *args, **kwargs) -> None:
    """
    Initialize Driver.
    """
    self.__base: str = 'https://raw.githubusercontent.com/toolkitr/tkr/main/'
    self.__baseurl: str = f'{self.__base}{folder}/'
    self.__file: str = f'{self.__baseurl}{path}'
    self.__content: object = self.__get_content()

  @resource.notdeprecated
  def __repr__(self) -> str:
    """
    Representation of the Driver.

    Returns:
    str: The driver content.
    """
    return self.__content

  @resource.notdeprecated
  def __str__(self) -> str:
    """
    String representation of the Driver.

    Returns:
    str: The driver content.
    """
    return self.__content

  @resource.notdeprecated
  def __get_content(self) -> str:
    """
    Get the content of the file.

    Returns:
    str: The content of the file.
    """
    try:
      return requests.get(self.__file).text
    except: 
      try: return requests.get(self.__file)
      except: return 'tkr.ext.Driver.FilePathError'

  @resource.notdeprecated
  def file(self, path: str, *args, **kwargs) -> str:
    """
    Create a new file.

    Parameters:
    path (str): The path of the file.

    Returns:
    str: The content of the file.
    """
    try:
      with open(path, 'w') as file:
        file.write(self.__content)
    except: return 'tkr.ext.Driver.FileError'
    return self.__content

  @resource.notdeprecated
  def save(self, path: str, *args, **kwargs) -> str:
    """
    Create a new file.

    Parameters:
    path (str): The path of the file.

    Returns:
    str: The content of the file.
    """
    return self.file(path)
    
  @resource.notdeprecated
  def __call__(self, path: str=None, folder:str='test', *args, **kwargs) -> str:
    """
    Get the content of the file.

    Parameters:
    path (str): The file to pull from EX: file.py
    folder (str): The folder the file is in.
    *args (object): The args to pass to the driver.
    **kwargs (object): The kwargs to pass to the driver.

    Returns:
    str: The content of the file.
    """
    if path is None: return self.__content
    else:
      self.__baseurl: str = f'{self.__base}{folder}/'
      self.__file: str = f'{self.__baseurl}{path}'
      self.__content: object = self.__get_content()
      return self.__content
