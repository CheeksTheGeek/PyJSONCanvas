
# PyJSONCanvas Documentation

PyJSONCanvas is a Python library for working with JSON Canvas (previously known as Obsidian Canvas) files. It provides a simple and intuitive API for creating, editing, and manipulating canvas objects, nodes, and edges.

## Table of Contents

1. [Installation](#installation)
2. [Basic Usage](#basic-usage)
3. [Canvas](#canvas)
4. [Nodes](#nodes)
5. [Edges](#edges)
6. [Colors](#colors)
7. [Exceptions](#exceptions)

## Installation

You can install PyJSONCanvas using pip:

```
pip install PyJSONCanvas
```

## Basic Usage

Here's a basic example of how to use PyJSONCanvas:

```python
from pyjsoncanvas import Canvas, TextNode, FileNode, Edge, Color

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

## Canvas

The `Canvas` class is the main container for nodes and edges.

### Methods

- `to_json()`: Convert the canvas to a JSON string.
- `from_json(json_str)`: Create a canvas from a JSON string.
- `export(file_path)`: Save the canvas to a file.
- `validate()`: Validate the canvas structure.
- `get_node(node_id)`: Get a node by its ID.
- `get_edge(edge_id)`: Get an edge by its ID.
- `add_node(node)`: Add a node to the canvas.
- `add_edge(edge)`: Add an edge to the canvas.
- `remove_node(node_id)`: Remove a node from the canvas.
- `remove_edge(edge_id)`: Remove an edge from the canvas.
- `get_connections(node_id)`: Get all edges connected to a node.
- `get_edge_nodes(edge_id)`: Get the nodes connected by an edge.
- `get_adjacent_nodes(node_id)`: Get all nodes adjacent to a given node.

## Nodes

PyJSONCanvas supports four types of nodes:

1. `TextNode`: A node containing text.
2. `FileNode`: A node representing a file.
3. `LinkNode`: A node containing a URL.
4. `GroupNode`: A node that can contain other nodes.

All node types inherit from the `GenericNode` class and have the following common attributes:

- `id`: Unique identifier for the node.
- `type`: The type of the node (TextNode, FileNode, LinkNode, or GroupNode).
- `x`: X-coordinate of the node.
- `y`: Y-coordinate of the node.
- `width`: Width of the node.
- `height`: Height of the node.
- `color`: Color of the node (optional).

### TextNode

Additional attributes:
- `text`: The text content of the node.

### FileNode

Additional attributes:
- `file`: The path to the file.
- `subpath`: Subpath within the file (optional).

### LinkNode

Additional attributes:
- `url`: The URL of the link.

### GroupNode

Additional attributes:
- `label`: Label for the group (optional).
- `background`: Background image or color (optional).
- `backgroundStyle`: Style of the background (cover, ratio, or repeat).

## Edges

Edges represent connections between nodes.

### Attributes

- `id`: Unique identifier for the edge.
- `fromNode`: ID of the source node.
- `toNode`: ID of the target node.
- `fromSide`: Side of the source node where the edge starts (top, right, bottom, left).
- `toSide`: Side of the target node where the edge ends (top, right, bottom, left).
- `fromEnd`: Style of the edge start (none or arrow).
- `toEnd`: Style of the edge end (none or arrow).
- `color`: Color of the edge.
- `label`: Label for the edge (optional).

## Colors

Colors can be specified using either hex codes or preset values:

```python
color1 = Color("#FF0000")  # Red using hex code
color2 = Color("4")        # Green using preset value
```

## Exceptions

PyJSONCanvas defines several custom exceptions to handle various error scenarios. Here's a complete list of exceptions:

1. `JsonCanvasException`: Base exception for all JsonCanvas errors.
2. `InvalidJsonError`: Raised when the JSON is invalid or malformed.
3. `NodeNotFoundError`: Raised when a specified node is not found.
4. `EdgeNotFoundError`: Raised when a specified edge is not found.
5. `InvalidNodeTypeError`: Raised when a node has an invalid or unsupported type.
6. `InvalidNodeAttributeError`: Raised when a node attribute is invalid or missing.
7. `InvalidEdgeConnectionError`: Raised when an edge's connection points are invalid.
8. `InvalidEdgeAttributeError`: Raised when an edge attribute is invalid or missing.
9. `NodeIDConflictError`: Raised when two nodes have the same ID.
10. `EdgeIDConflictError`: Raised when two edges have the same ID.
11. `InvalidColorValueError`: Raised when a color value is invalid or not supported.
12. `InvalidPositionError`: Raised when a node's position is outside the allowed range.
13. `InvalidDimensionError`: Raised when a node's dimensions are invalid.
14. `InvalidGroupOperationError`: Raised for invalid operations on group nodes.
15. `OrphanEdgeError`: Raised when an edge refers to a non-existent node.
16. `UnsupportedFileTypeError`: Raised when a file node points to an unsupported file type.
17. `FileReadError`: Raised when there is an error reading a file.
18. `FileWriteError`: Raised when there is an error writing to a file.
19. `RenderingError`: Raised when there is an error during rendering.
20. `CanvasValidationError`: Raised when the canvas does not pass validation checks.

This documentation provides an overview of the PyJSONCanvas library. For more detailed information about specific classes, methods, and attributes, please refer to the docstrings and comments in the source code.