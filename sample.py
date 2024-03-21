# sample.py
from pyjsoncanvas import (
    Canvas,
    TextNode,
    FileNode,
    LinkNode,
    GroupNode,
    GroupNodeBackgroundStyle,
    Edge,
    Color,
    InvalidJsonError,
    CanvasValidationError,
    NodeNotFoundError,
    EdgeNotFoundError,
)
from pprint import pprint


# Create a new canvas
canvas = Canvas(nodes=[], edges=[])

# Add some nodes
text_node = TextNode(x=100, y=100, width=200, height=100, text="Hello, world!")
canvas.add_node(text_node)

file_node = FileNode(x=300, y=100, width=100, height=100, file="/path/to/file.png")
canvas.add_node(file_node)

link_node = LinkNode(x=500, y=100, width=150, height=50, url="https://example.com")
canvas.add_node(link_node)

group_node = GroupNode(
    x=200,
    y=300,
    width=400,
    height=300,
    label="My Group",
    background="/path/to/background.jpg",
    backgroundStyle=GroupNodeBackgroundStyle.COVER,
)
canvas.add_node(group_node)

# Add some edges
edge1 = Edge(
    fromNode=text_node.id,
    fromSide="bottom",
    toNode=file_node.id,
    toSide="top",
    color=Color("#FF0000"),
    label="Edge 1",
)
canvas.add_edge(edge1)

edge2 = Edge(
    fromNode=file_node.id,
    fromSide="right",
    toNode=link_node.id,
    toSide="left",
    color=Color("4"),  # Green
)
canvas.add_edge(edge2)

# Save the canvas as JSON
json_str = canvas.to_json()
# save it to a file
with open("canvas.canvas", "w") as f:
    f.write(json_str)

# Load the canvas from JSON
try:
    loaded_canvas = Canvas.from_json(json_str)
except InvalidJsonError as e:
    pprint(f"Error loading canvas: {e}")

# Validate the canvas
try:
    loaded_canvas.validate()
except CanvasValidationError as e:
    print(f"Canvas validation failed: {e}")

# Get a node
try:
    node = loaded_canvas.get_node(text_node.id)
    print(f"Node found: {node}")
except NodeNotFoundError as e:
    print(f"Node not found: {e}")

# Get an edge
try:
    edge = loaded_canvas.get_edge(edge1.id)
    print(f"Edge found: {edge}")
except EdgeNotFoundError as e:
    print(f"Edge not found: {e}")

# Get connections for a node
connections = loaded_canvas.get_connections(text_node.id)
pprint(f"Connections for {text_node.id}: {connections}")

# Remove a node
print(loaded_canvas.remove_node(file_node.id))

# Get connections for a node
connections = loaded_canvas.get_connections(text_node.id)
pprint(f"Connections for {text_node.id}: {connections}")

# Get adjacent nodes for a node
adjacent_nodes = loaded_canvas.get_adjacent_nodes(text_node.id)
pprint(f"Adjacent nodes for {text_node.id}: {adjacent_nodes}")
