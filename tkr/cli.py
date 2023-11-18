__all__: tuple = (
  'main',
)

import json
import pathlib

def main(*args) -> None:
    path_abs: str = f'{pathlib.Path(__file__).parent.absolute()}/core/coreattrs.json'

    with open(path_abs, 'r') as file:
      data = json.load(file)

    data['1  `1  '] = 'value'

    with open(path_abs, 'w') as file:
      json.dump(data, file, indent=4)
if __name__ == '__main__':
    main()
