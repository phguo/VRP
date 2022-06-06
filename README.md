# PyVRP

A Python package for plotting Vehicle Routing Problem (VRP) solutions.

## Usage

Install this package using `pip install PyVRP`, then

```Python
from pyvrp.draw import draw_vrp

pos = {1: (0, 0), 2: (1, 1), 3: (2, 3)}
routes = [[1, 2, 3, 1]]
draw_vrp(pos, routes, save_file=True)
```