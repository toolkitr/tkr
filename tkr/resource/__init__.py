"""
General resources used throughout tkr.

Functions:
- `deprecated`: Mark a function as deprecated.
- `notdeprecated`: Mark a function as not deprecated.
"""

__all__: tuple = (
  'deprecated',
  'notdeprecated',
)

def deprecated(func: object) -> object:
  """
  Allows for users to see if a method is deprecated

  Parameters:
  func (object): The deprecated function

  Returns:
  object: The deprecated function
  """
  func.deprecated = True
  return func

def notdeprecated(func: object) -> object:
  """
  Allows for users to see if a method is deprecated

  Parameters:
  func (object): Non-deprecated function

  Returns:
  object: Non-deprecated function
  """
  func.deprecated = False
  return func
