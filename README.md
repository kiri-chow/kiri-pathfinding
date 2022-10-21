# kiri-pathfinding

A toy module to generate a map and find the shortest path from two points on the map

## Usage

```python
from matplotlib import pyplot as plt
from kiri_pathfinding.map_generator import generate_map, draw_map
from kiri_pathfinding.pathfinding import PathFinding, draw_path

# genetate a map and find shortest path
data_map = generate_map(20, 20)
pathfinding = PathFinding(data_map)
path = pathfinding.find((0, 0), (19, 19))

# visualize
fig, ax = plt.subplots()
draw_map(data_map, ax)
draw_path(path, ax)
```

## Example

![example](/home/anthony/.config/Typora/typora-user-images/image-20221021165342297.png)

The image above visualizes the generated map and the found path from point (0, 0) to point (19, 19). The different colors on the map mean different terrains. The green means glass and others mean barriers with additional costs to pass.