# PyJSONCanvas

PyJSONCanvas is a Python library for working with JSON Canvas (previously known as Obsidian Canvas) files. It provides a simple and intuitive API for creating, editing, and manipulating canvas objects, nodes, and edges.

## Features

- Create, load, and save canvas files in JSON format
- Add, remove, and modify nodes (text, file, link, group)
- Add, remove, and modify edges with various styles and colors
- Validate canvas, nodes, and edges for integrity
- Get connections and adjacent nodes for a given node
- Extensive error handling and helpful exception messages

## Installation

You can install PyJSONCanvas using pip:

```
pip install PyJSONCanvas
```

## Usage

Here's a basic example of how to use PyJSONCanvas:

```python
from pyjsoncanvas import (
    Canvas,
    TextNode,
    FileNode,
    LinkNode,
    GroupNode,
    GroupNodeBackgroundStyle,
    Edge,
    Color,
)

# Create a new canvas
canvas = Canvas(nodes=[], edges=[])

# Add some nodes
text_node = TextNode(x=100, y=100, width=200, height=100, text="Hello, world!")
canvas.add_node(text_node)

file_node = FileNode(x=300, y=100, width=100, height=100, file="/path/to/file.png")
canvas.add_node(file_node)

# Add an edge
edge = Edge(
    fromNode=text_node.id,
    fromSide="bottom",
    toNode=file_node.id,
    toSide="top",
    color=Color("#FF0000"),
    label="Edge 1",
)
canvas.add_edge(edge)

# Save the canvas as JSON
json_str = canvas.to_json()

# Load the canvas from JSON
loaded_canvas = Canvas.from_json(json_str)

# Get a node
node = loaded_canvas.get_node(text_node.id)

# Get connections for a node
connections = loaded_canvas.get_connections(text_node.id)
```

## Documentation

The PyJSONCanvas library is well-documented, and you can find detailed information about all the available classes, methods, and exceptions in the docstrings and code comments.

## Contributing

We welcome contributions to PyJSONCanvas! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the [GitHub repository](https://github.com/cheeksthegeek/PyJSONCanvas).

## License

PyJSONCanvas is released under the [MIT License](https://opensource.org/licenses/MIT).

## Support

If you have any questions or need further assistance, please open an issue on the [GitHub repository](https://github.com/cheeksthegeek/PyJSONCanvas) or contact the maintainers.